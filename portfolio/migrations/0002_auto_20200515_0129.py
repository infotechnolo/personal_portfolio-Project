# Generated by Django 3.0 on 2020-05-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='media/portfolio/images/'),
        ),
    ]