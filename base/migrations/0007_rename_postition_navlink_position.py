# Generated by Django 4.0.6 on 2022-07-30 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_navlink_postition_alter_navlink_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navlink',
            old_name='postition',
            new_name='position',
        ),
    ]