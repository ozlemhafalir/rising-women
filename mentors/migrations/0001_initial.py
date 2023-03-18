# Generated by Django 3.2.18 on 2023-03-18 13:56

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentors.category')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('verified', models.BooleanField(default=False)),
                ('bio', models.TextField(max_length=1000)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('website', models.CharField(blank=True, max_length=250, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=250, null=True)),
                ('joined', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentors.category')),
                ('subcategory', models.ManyToManyField(blank=True, related_name='subcategories', to='mentors.Subcategory')),
            ],
        ),
    ]
