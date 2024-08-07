# Generated by Django 4.2.14 on 2024-07-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('details', models.TextField(default=None, max_length=5000)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Expriences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('details', models.TextField(default=None, max_length=5000)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=350)),
                ('details', models.TextField(default=None, max_length=1000)),
                ('url', models.URLField(default=None)),
                ('image', models.ImageField(default=None, upload_to='media/Images')),
            ],
        ),
    ]