# Generated by Django 4.2.4 on 2023-09-04 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_productlocation'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=None,
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=None,
        ),
        migrations.DeleteModel(
            name='ProductLocation',
        ),
        migrations.RemoveField(
            model_name='productmovement',
            name='from_location',
        ),
        migrations.RemoveField(
            model_name='productmovement',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productmovement',
            name='to_location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductMovement',
        ),
    ]