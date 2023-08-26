# Generated by Django 3.2.6 on 2021-10-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GGDC', '0005_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='leaving_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='hod',
            field=models.CharField(blank=True, choices=[('HOD', 'HOD'), ('Staff', 'Staff')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Retired', 'Retired'), ('Transferred', 'Transferred')], max_length=30),
        ),
    ]
