# Generated by Django 4.0.6 on 2022-07-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_testitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='testitem',
            name='activated',
            field=models.BooleanField(default=False, verbose_name='cho biết đang ở trang nào'),
        ),
    ]
