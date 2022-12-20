# Generated by Django 4.1.4 on 2022-12-19 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import json.decoder
import json.encoder


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='products/images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('full_title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1000)),
                ('language', models.CharField(choices=[('uzb', 'Uzb'), ('uzb/rus', 'Uzb Rus'), ('rus', 'Rus'), ('cyr', 'Cyr'), ('eng', 'Eng')], default='uzb', max_length=15)),
                ('volume', models.IntegerField()),
                ('format', models.CharField(choices=[('60х84 1/16', 'Format 1'), ('60×90 1/16', 'Format 2'), ('70×100 1/16', 'Format 3'), ('70×90 1/32', 'Format 4'), ('84х108 1/32', 'Format 5')], default='60х84 1/16', max_length=15)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('cover', models.CharField(choices=[('hard', 'Hard'), ('soft', 'Soft')], default='hard', max_length=15)),
                ('info', models.JSONField(decoder=json.decoder.JSONDecoder, encoder=json.encoder.JSONEncoder)),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='orders.book')),
            ],
            options={
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='orders.book')),
            ],
            options={
                'db_table': 'wishlists',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.cart')),
            ],
            options={
                'db_table': 'orders',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.category'),
        ),
    ]