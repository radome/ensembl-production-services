# Generated by Django 2.1.15 on 2020-02-20 15:26

from django.db import migrations, models
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_prodinf_portal', '0006_update_admin_menus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('cred_id', models.AutoField(primary_key=True, serialize=False)),
                ('cred_name', models.CharField(max_length=150, unique=True, verbose_name='Name')),
                ('cred_url', models.CharField(max_length=255, verbose_name='Access Url')),
                ('user', models.CharField(max_length=100, verbose_name='User Name')),
                ('credentials', fernet_fields.fields.EncryptedCharField(max_length=255, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Credential',
                'verbose_name_plural': 'Credentials',
            },
        ),
    ]
