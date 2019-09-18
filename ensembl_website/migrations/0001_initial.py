# Generated by Django 2.1.7 on 2019-09-18 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import ensembl_production.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpLink',
            fields=[
                ('help_link_id', models.AutoField(primary_key=True, serialize=False)),
                ('page_url', django_mysql.models.SizedTextField(blank=True, null=True, size_class=1)),
            ],
            options={
                'db_table': 'help_link',
            },
        ),
        migrations.CreateModel(
            name='HelpRecord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('help_record_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('keyword', django_mysql.models.SizedTextField(blank=True, null=True, size_class=1)),
                ('data', models.TextField()),
                ('status', django_mysql.models.EnumField(choices=[('draft', 'draft'), ('live', 'live'), ('dead', 'dead')])),
                ('helpful', models.IntegerField(blank=True, null=True)),
                ('not_helpful', models.IntegerField(blank=True, null=True)),
                ('created_by', ensembl_production.models.SpanningForeignKey(blank=True, db_column='created_by', db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='helprecord_created_by', related_query_name='helprecord_creates', to=settings.AUTH_USER_MODEL)),
                ('modified_by', ensembl_production.models.SpanningForeignKey(blank=True, db_column='modified_by', db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='helprecord_modified_by', related_query_name='helprecord_updates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'help_record',
            },
        ),
        migrations.CreateModel(
            name='FaqRecord',
            fields=[
            ],
            options={
                'verbose_name': 'FAQ',
                'proxy': True,
                'indexes': [],
            },
            bases=('ensembl_website.helprecord',),
        ),
        migrations.CreateModel(
            name='LookupRecord',
            fields=[
            ],
            options={
                'verbose_name': 'Lookup',
                'proxy': True,
                'indexes': [],
            },
            bases=('ensembl_website.helprecord',),
        ),
        migrations.CreateModel(
            name='MovieRecord',
            fields=[
            ],
            options={
                'verbose_name': 'Movie',
                'proxy': True,
                'indexes': [],
            },
            bases=('ensembl_website.helprecord',),
        ),
        migrations.CreateModel(
            name='ViewRecord',
            fields=[
            ],
            options={
                'verbose_name': 'Page',
                'proxy': True,
                'indexes': [],
            },
            bases=('ensembl_website.helprecord',),
        ),
        migrations.AddField(
            model_name='helplink',
            name='help_record',
            field=models.OneToOneField(blank=True, db_column='help_record_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='ensembl_website.ViewRecord'),
        ),
    ]
