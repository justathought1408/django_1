# Generated by Django 4.1.3 on 2022-12-17 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_fm_vac'),
    ]

    operations = [
        migrations.AddField(
            model_name='fm',
            name='image_vac',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Vacancy Photo'),
        ),
    ]