# Generated by Django 4.1.5 on 2023-02-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]