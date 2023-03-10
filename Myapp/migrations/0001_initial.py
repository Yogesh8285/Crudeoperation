# Generated by Django 3.1.5 on 2023-03-01 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('Birth_date', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.education')),
            ],
        ),
    ]
