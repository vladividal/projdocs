# Generated by Django 4.0.2 on 2022-03-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='linkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Link Type',
                'verbose_name_plural': 'Link Types',
                'db_table': 't_link_type',
                'ordering': ['name'],
                'managed': True,
            },
        ),
    ]