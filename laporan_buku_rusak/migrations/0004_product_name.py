# Generated by Django 4.2.6 on 2023-10-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laporan_buku_rusak', '0003_remove_product_name_product_book_product_is_rusak'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
