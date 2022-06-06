from django.db import models


class Person(models.Model):
    img = models.ImageField(upload_to='images/', blank=True, verbose_name="Фото профиля", max_length=900)
    name = models.CharField(max_length=20, verbose_name="Введите имя")
    age = models.DateField(verbose_name="Введите дату рожддения")
    address = models.CharField(max_length=100, verbose_name='Введите адресс проживания')
