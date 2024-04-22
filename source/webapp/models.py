from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MinValueValidator


STATUS_CHOICES = [
    ('in_stock', 'В наличии'),
    ('for_order', 'На заказ 30%'),
]


class Room(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название комнаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,
                            verbose_name='Название категории мебели')
    room = models.ForeignKey('webapp.Room', on_delete=models.CASCADE,
                             verbose_name='Комната', related_name='categories')

    def __str__(self):
        return f'{self.room.name} --- {self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    room = models.ForeignKey('webapp.Room', on_delete=models.CASCADE, related_name='products', default=1)
    category = ChainedForeignKey(
        Category,  # Модель, на которую указывает ключ
        chained_field="room",  # Поле в текущей модели, которое влияет на выбор в связанном поле
        chained_model_field="room",  # Поле в связываемой модели, которое фильтруется по значению chained_field
        show_all=False,  # Показывать ли все объекты, когда значение chained_field не выбрано
        auto_choose=True,  # Автоматически выбирать элемент, если он единственный доступный
        sort=True,  # Сортировать ли доступные значения в выпадающем списке
        related_name='products'
    )
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    amount = models.IntegerField(verbose_name="Остаток", validators=(MinValueValidator(0),))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock', verbose_name='Наличие')
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2, validators=(MinValueValidator(0),))
    picture = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Изображение')

    def __str__(self):
        return f'{self.name} - {self.amount}'

    def save(self, *args, **kwargs):
        # Обновляем статус на основе количества
        if self.amount == 0:
            self.status = 'for_order'
        else:
            self.status = 'in_stock'
        super().save(*args, **kwargs)  # Вызываем оригинальный метод save

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
