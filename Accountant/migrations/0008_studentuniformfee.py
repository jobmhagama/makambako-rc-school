# Generated by Django 4.0.1 on 2022-03-10 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accountant', '0007_alter_studentfee_created_at_studentfoodfee'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUniformFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cno', models.IntegerField()),
                ('Shirt', models.BooleanField()),
                ('trouser', models.BooleanField()),
                ('sweater', models.BooleanField()),
                ('Cap', models.BooleanField()),
                ('tracksuit', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(max_length=2000)),
                ('amount', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accountant.student')),
            ],
        ),
    ]
