from django.db import models

class FM(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    desc = models.CharField(max_length=1200, verbose_name='Description')
    image1 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 1')
    image2 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 2')
    image3 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 3')
    image4 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 4')
    image5 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 5')
    slug = models.SlugField(unique=True, verbose_name='URL')
    is_pub = models.BooleanField(default=False, verbose_name='Published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Model'