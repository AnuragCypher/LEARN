# Generated by Django 5.0.1 on 2024-02-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_one', '0006_alter_post_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
