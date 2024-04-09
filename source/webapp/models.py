from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название комнаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название категории мебели')
    rooms = models.ManyToManyField(Room, verbose_name='Категории мебели', related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
