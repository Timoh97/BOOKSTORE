# Generated by Django 3.2.9 on 2022-01-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_books_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(default='Author name..', max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(default='Title of the book', max_length=100),
        ),
    ]
