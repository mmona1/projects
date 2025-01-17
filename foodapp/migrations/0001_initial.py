# Generated by Django 4.2.3 on 2023-08-10 05:45

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
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200)),
                ('limit', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.category')),
            ],
        ),
    ]
