from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_adminuser_last_login_alter_adminuser_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tes',
        ),
    ]
