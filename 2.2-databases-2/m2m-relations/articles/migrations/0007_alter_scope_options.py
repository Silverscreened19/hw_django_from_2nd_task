# Generated by Django 4.1.7 on 2023-03-18 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['tag__name'], 'verbose_name': 'Тег'},
        ),
    ]