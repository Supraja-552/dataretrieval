# Generated by Django 4.2.6 on 2023-12-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_no', models.IntegerField()),
                ('Ename', models.CharField(max_length=100)),
                ('Job', models.CharField(max_length=100)),
                ('Mgr', models.IntegerField()),
                ('Hiredate', models.DateField()),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField()),
                ('Dept_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]
