# Generated by Django 4.0.1 on 2022-03-02 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_student',
            new_name='is_cit',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='course',
            new_name='is_sv',
        ),
    ]