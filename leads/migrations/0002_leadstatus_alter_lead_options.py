# Generated by Django 4.0.2 on 2022-03-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='leadStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Lead Status',
                'verbose_name_plural': 'Lead Status',
                'db_table': 't_lead_status',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='lead',
            options={'managed': True, 'ordering': ['-start_date'], 'verbose_name': 'Lead', 'verbose_name_plural': 'Leads'},
        ),
    ]