# Generated by Django 4.1.3 on 2022-12-15 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fm',
            options={'verbose_name_plural': 'Модель'},
        ),
        migrations.AlterField(
            model_name='fm',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]