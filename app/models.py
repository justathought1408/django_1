from django.db import models
from django import forms
from django.contrib import admin
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class FM(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    price = models.IntegerField(default=0)
    desc = RichTextField(max_length=5000, blank=True, null=True)
    image1 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 1')
    image2 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 2')
    image3 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 3')
    image4 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 4')
    image5 = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo 5')
    slug = models.SlugField(unique=True, verbose_name='URL', blank=True)
    is_pub = models.BooleanField(default=False, verbose_name='Published')
    added = models.DateTimeField(auto_now_add=True, verbose_name='Added')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    # vac = models.ForeignKey('Vacancy', on_delete=models.PROTECT, null=True)

    @admin.display(description='Photo')
    def images_count(self) :
        i = 0
        images = [self.image1, self.image2, self.image3, self.image4, self.image5]
        for img in  images :
            if img:
                i += 1
        return i

    def __str__(self):
        photos_count = 0
        images = [self.image1, self.image2, self.image3, self.image4, self.image5]
        for i in  images :
            if i:
                photos_count += 1

        return f'{self.title} ; Photos: {photos_count}'

    class Meta:
        verbose_name_plural = 'Model'

class Vacancy(models.Model):
    title_vac = models.CharField(max_length=100, verbose_name='Title', db_index=True)
    image_vac = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, verbose_name='Photo Vacancy (3:1)')
    text_vac = RichTextField(max_length=5000, blank=True, null=True)
    is_pub_vac = models.BooleanField(default=False, verbose_name='Vacancy Published')
    slug_vac = models.SlugField(unique=True, verbose_name='URL', blank=True)
    added_vac = models.DateTimeField(auto_now_add=True, verbose_name='Added')
    updated_vac = models.DateTimeField(auto_now=True, verbose_name='Updated')
    is_top = models.BooleanField(default=False, verbose_name='At the top of the page')

    def __str__(self):
        return self.title_vac