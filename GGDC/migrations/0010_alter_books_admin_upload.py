# Generated by Django 3.2.6 on 2021-10-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GGDC', '0009_auto_20211023_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='admin_upload',
            field=models.FileField(upload_to='books/'),
        ),
    ]