# Generated by Django 5.0.4 on 2024-06-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_expriences_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expriences',
            name='details',
            field=models.TextField(default=None, max_length=5000),
        ),
    ]