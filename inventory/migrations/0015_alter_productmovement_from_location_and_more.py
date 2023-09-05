# Generated by Django 4.2.4 on 2023-09-04 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_productmovement_from_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmovement',
            name='from_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movements_from', to='inventory.location'),
        ),
        migrations.AlterField(
            model_name='productmovement',
            name='to_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movements_to', to='inventory.location'),
        ),
    ]
