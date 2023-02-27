# Generated by Django 4.1.7 on 2023-02-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(editable=False, max_length=100, unique=True)),
            ],
        ),
    ]
