# Generated by Django 2.2.6 on 2020-03-27 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='出版日期'),
        ),
    ]
