# Generated by Django 4.1.3 on 2022-12-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_fm_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fm',
            name='desc',
            field=models.CharField(max_length=980, verbose_name='Описание'),
        ),
    ]
