# Generated by Django 4.1.3 on 2022-12-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_vacancy_image_vac_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='image_vac_post',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Photo Post Vacancy'),
        ),
    ]