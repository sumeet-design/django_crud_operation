# Generated by Django 4.0.4 on 2023-10-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('standard', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=11)),
            ],
        ),
    ]
