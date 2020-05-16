# Generated by Django 3.0 on 2020-05-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200516_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_blog',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='all_blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/blog/images/'),
        ),
    ]
