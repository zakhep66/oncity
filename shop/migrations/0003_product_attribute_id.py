# Generated by Django 4.2.3 on 2023-11-06 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attribute_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.attribute'),
        ),
    ]