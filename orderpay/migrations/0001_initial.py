# Generated by Django 2.1.2 on 2018-11-12 23:39

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.EmailField(default=None, max_length=254, verbose_name=django.contrib.auth.models.User)),
            ],
        ),
    ]
