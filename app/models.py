from django.db import models

class FM(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    desc = models.CharField(max_length=1200, verbose_name='Описание')
    image1 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Фото 1')
    image2 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Фото 2')
    image3 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Фото 3')
    image4 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Фото 4')
    image5 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Фото 5')
    slug = models.SlugField(unique=True, verbose_name='Адрес записи')
    is_pub = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name_plural = 'Модель'