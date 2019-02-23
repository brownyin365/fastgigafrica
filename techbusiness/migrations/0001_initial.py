# Generated by Django 2.1.2 on 2018-11-12 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Posttech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('response_time', models.DateTimeField(blank=True)),
                ('slug', models.SlugField(max_length=250)),
                ('requirement', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gallery', models.ImageField(blank=True, null=True, upload_to='')),
                ('delivery', models.CharField(default=0, max_length=120)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbusiness.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewtech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price_rating', models.IntegerField(null=True)),
                ('location_rating', models.IntegerField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbusiness.Category')),
            ],
        ),
        migrations.AddField(
            model_name='posttech',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbusiness.Sub_Category'),
        ),
    ]