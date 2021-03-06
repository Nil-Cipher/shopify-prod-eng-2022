# Generated by Django 4.0.1 on 2022-01-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_count', models.PositiveIntegerField()),
                ('product_SKU', models.CharField(max_length=30)),
                ('product_weight', models.FloatField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
