# Generated by Django 5.0 on 2023-12-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laporan_buku_rusak', '0002_laporan_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laporan',
            name='is_rusak',
        ),
    ]
