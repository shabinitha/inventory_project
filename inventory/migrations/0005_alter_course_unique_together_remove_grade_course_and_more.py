# Generated by Django 4.2.4 on 2023-09-04 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_course_person_grade'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='grade',
            name='course',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='person',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RemoveField(
            model_name='person',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
