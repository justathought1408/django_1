# Generated by Django 4.1.3 on 2022-12-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_fm_options_alter_fm_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fm',
            name='image',
        ),
        migrations.AddField(
            model_name='fm',
            name='image1',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Фото 1'),
        ),
        migrations.AddField(
            model_name='fm',
            name='image2',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Фото 2'),
        ),
        migrations.AddField(
            model_name='fm',
            name='image3',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Фото 3'),
        ),
        migrations.AddField(
            model_name='fm',
            name='image4',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Фото 4'),
        ),
    ]
