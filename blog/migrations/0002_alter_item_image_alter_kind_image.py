# Generated by Django 5.0.4 on 2024-05-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='img/item'),
        ),
        migrations.AlterField(
            model_name='kind',
            name='image',
            field=models.ImageField(upload_to='img/kind'),
        ),
    ]
