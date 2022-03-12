# Generated by Django 4.0.2 on 2022-03-12 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Module Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Module descriprion')),
                ('sequence', models.IntegerField(verbose_name='Sequence')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Project Module',
                'verbose_name_plural': 'Project Modules',
                'db_table': 't_project_module',
                'ordering': ['name'],
                'managed': True,
            },
        ),
    ]
