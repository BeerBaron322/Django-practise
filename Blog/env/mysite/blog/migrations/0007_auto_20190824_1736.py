# Generated by Django 2.2.4 on 2019-08-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190824_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='G:\\python-projects\\Blog\\env\\mysite\\media\\post_images\\default.jpg', upload_to='post_images'),
        ),
    ]
