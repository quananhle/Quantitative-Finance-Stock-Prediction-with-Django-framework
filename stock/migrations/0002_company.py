# Generated by Django 2.2.20 on 2022-05-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
            ],
        ),
    ]
