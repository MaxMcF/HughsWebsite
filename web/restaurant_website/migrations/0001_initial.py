# Generated by Django 2.2.5 on 2019-09-22 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='Untitled', max_length=180)),
                ('price', models.FloatField(blank=True, null=True)),
                ('product_description', models.CharField(default='Untitled', max_length=180)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('transaction_amount', models.FloatField(blank=True, null=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transaction', to='restaurant_website.Product')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='restaurant_website.Transaction')),
            ],
        ),
    ]
