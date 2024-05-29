from django.contrib.auth import get_user_model
from django.db.models import Sum, F, ExpressionWrapper as E

from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MinValueValidator


class Room(models.Model):
    name = models.CharField(max_length=20,
                            null=False,
                            blank=False,
                            verbose_name='Название комнаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Category(models.Model):
    name = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            verbose_name='Название категории мебели')
    room = models.ForeignKey('webapp.Room',
                             on_delete=models.CASCADE,
                             verbose_name='Комната',
                             related_name='categories')

    def __str__(self):
        return f'{self.room.name} --- {self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    room = models.ForeignKey('webapp.Room',
                             on_delete=models.CASCADE,
                             related_name='products',
                             default=1)
    category = ChainedForeignKey(
        Category,  # Модель, на которую указывает ключ
        chained_field="room",  # Поле в текущей модели, которое влияет на выбор в связанном поле
        chained_model_field="room",  # Поле в связываемой модели, которое фильтруется по значению chained_field
        show_all=False,  # Показывать ли все объекты, когда значение chained_field не выбрано
        auto_choose=True,  # Автоматически выбирать элемент, если он единственный доступный
        sort=True,  # Сортировать ли доступные значения в выпадающем списке
        related_name='products'
    )
    name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            verbose_name='Название')
    description = models.TextField(max_length=2000,
                                   null=True,
                                   blank=True,
                                   verbose_name='Описание')
    amount = models.IntegerField(verbose_name="Остаток",
                                 validators=(MinValueValidator(0),))
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=7,
                                decimal_places=2,
                                validators=(MinValueValidator(0),))
    picture = models.ImageField(null=True,
                                blank=True,
                                upload_to='product_pics',
                                verbose_name='Изображение')

    def __str__(self):
        return f'{self.room.name} --- {self.name} - {self.amount}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Basket(models.Model):
    product = models.ForeignKey('webapp.Product',
                                related_name='basket',
                                on_delete=models.CASCADE,
                                verbose_name='Продукт')
    amount = models.IntegerField(verbose_name='Количество',
                                 validators=[MinValueValidator(0),])

    @classmethod
    def get_with_total(cls):
        # запрос так быстрее
        total_output_field = models.DecimalField(max_digits=10, decimal_places=2)
        total_exp = E(F('amount') * F('product__price'), output_field=total_output_field)
        return cls.objects.annotate(total=total_exp)

    @classmethod
    def get_with_product(cls):
        return cls.get_with_total().select_related('product')

    @classmethod
    def get_basket_total(cls, ids=None):
        # запрос так быстрее
        basket_products = cls.get_with_total()
        if ids is not None:
            basket_products = basket_products.filter(pk__in=ids)
        total = basket_products.aggregate(basket_total=Sum('total'))
        return total['basket_total']

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.amount)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    products = models.ManyToManyField('webapp.Product',
                                      through='webapp.OrderProduct',
                                      through_fields=['order', 'product'],
                                      related_name='orders',
                                      blank=True,
                                      verbose_name='Продукты')
    name = models.CharField(max_length=100,
                            verbose_name='Имя')
    phone = models.CharField(max_length=20,
                             verbose_name='Телефон')
    address = models.CharField(max_length=100,
                               verbose_name='Адрес')
    comment = models.TextField(max_length=500,
                               verbose_name='Комментарий',
                               blank=True,
                               null=True)
    date_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата и время создания')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='orders',
                             null=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    def format_time(self):
        return self.date_create.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product',
                                related_name='order_entries',  # все записи заказов, в которых участвует данный продукт
                                on_delete=models.CASCADE,
                                verbose_name='Продукт')
    amount = models.IntegerField(verbose_name='Количество',
                                 validators=[MinValueValidator(0)])
    total = models.DecimalField(verbose_name='Итоговый прайс',
                                max_digits=7,
                                decimal_places=2,
                                validators=(MinValueValidator(0),),
                                default=0,
                                null=True,
                                blank=True)
    order = models.ForeignKey('webapp.Order',
                              related_name='order_products',  # все продукты в заказе
                              on_delete=models.CASCADE,
                              verbose_name='Заказ'
                              )

    def __str__(self):
        return f'{self.pk}: {self.amount} units of {self.product.name}'


class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE,
                                 related_name='delivery',
                                 verbose_name='Заказ')
    delivery_date = models.DateTimeField(verbose_name='Дата доставки',
                                         null=True,
                                         blank=True)
    name = models.CharField(verbose_name='Ответственный за доставку',
                            max_length=100)
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'В пути'),
            ('delivered', 'Доставлено'),
            ('cancelled', 'Отменено')
        ],
        default='pending',
        verbose_name='Статус'
    )
    photo = models.ImageField(upload_to='delivery_photos/',
                              blank=True,
                              null=True,
                              verbose_name='Фотография')

    def __str__(self):
        return f'Доставка заказа №{self.order.pk}'

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
