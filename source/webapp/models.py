from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название комнаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

