# Generated by Django 3.0 on 2020-05-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200516_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_blog',
            name='date',
            field=models.DateField(),
        ),
    ]
