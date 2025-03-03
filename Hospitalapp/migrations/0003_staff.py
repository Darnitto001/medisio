# Generated by Django 5.1.6 on 2025-02-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0002_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Phonenumber', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('hire_date', models.DateField()),
            ],
        ),
    ]
