# Generated by Django 3.2.6 on 2021-09-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firstyearform',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('caste', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('date', models.DateField()),
            ],
        ),
    ]
