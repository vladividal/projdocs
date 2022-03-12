# Generated by Django 4.0.2 on 2022-03-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Project Status',
                'verbose_name_plural': 'Project Status',
                'db_table': 't_project_status',
                'ordering': ['name'],
                'managed': True,
            },
        ),
    ]