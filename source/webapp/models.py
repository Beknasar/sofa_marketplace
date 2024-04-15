from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Room(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название комнаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название категории мебели')
    room = models.ForeignKey('webapp.Room', on_delete=models.CASCADE,
                               verbose_name='Категории мебели', related_name='categories')
    parent = ChainedForeignKey(
        'self',  # Ссылка на экземпляр того же класса
        on_delete=models.CASCADE,  # При удалении родителя удалять все дочерние элементы
        related_name='children',  # Имя для обратной связи
        null=True,  # Разрешить пустые значения для верхнего уровня категорий
        blank=True,  # Разрешить оставлять это поле пустым при заполнении форм
        verbose_name="Родительская категория",  # Человеко-понятное имя в админке
        chained_field='room',
        chained_model_field='room',
        show_all=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

