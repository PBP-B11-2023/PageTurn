# Generated by Django 4.2.6 on 2023-10-28 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('laporan_buku_rusak', '0005_remove_product_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='katalog.book'),
            preserve_default=False,
        ),
    ]