# Generated by Django 3.0 on 2020-05-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200516_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_blog',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]