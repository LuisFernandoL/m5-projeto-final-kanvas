# Generated by Django 4.2.3 on 2023-10-24 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_students_alter_course_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='status_date',
            new_name='start_date',
        ),
    ]
