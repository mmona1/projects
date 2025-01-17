# Generated by Django 4.2.4 on 2023-09-09 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0011_remove_product_description_remove_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='items',
            name='prodect',
        ),
        migrations.AddField(
            model_name='product',
            name='content_type',
            field=models.CharField(choices=[('burger', 'Burger'), ('pizza', 'Pizza'), ('pasta', 'Pasta'), ('fries', 'Fries')], default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discounted_price',
            field=models.DecimalField(decimal_places=0, default='0', max_digits=5),
        ),
        migrations.AddField(
            model_name='product',
            name='offer_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='subtitle',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='items',
        ),
        migrations.DeleteModel(
            name='prodect',
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.product_category'),
        ),
    ]
