# Generated by Django 2.2.4 on 2019-08-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190824_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='static/images/logo.jpg', upload_to='post_images'),
        ),
    ]
