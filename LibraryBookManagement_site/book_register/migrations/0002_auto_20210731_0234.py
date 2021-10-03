# Generated by Django 3.1.7 on 2021-07-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('name', 'author', 'genre', 'height', 'publisher')},
        ),
    ]
