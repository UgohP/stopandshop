# Generated by Django 5.1.1 on 2024-09-15 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperMarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.FloatField()),
                ('haggle', models.CharField(choices=[('Negotiable', 'Negotiable'), ('Unnegotiable', 'Unnegotiable')], default='Negotiable', max_length=50)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('market_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_vendors', to='users.vendor')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
