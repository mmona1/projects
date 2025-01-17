# Generated by Django 4.2.4 on 2023-08-31 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0007_cartitem_menuitem_delete_items_delete_prodect_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('amound', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='prodect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200)),
                ('limit', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.AddField(
            model_name='items',
            name='prodect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.prodect'),
        ),
    ]
