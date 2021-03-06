# Generated by Django 4.0.2 on 2022-03-20 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='businessArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Business Area',
                'verbose_name_plural': 'Business Areas',
                'db_table': 't_business_area',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='contractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Contract Type',
                'verbose_name_plural': 'Contract Types',
                'db_table': 't_contract_type',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='educationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Education Level',
                'verbose_name_plural': 'Education Levels',
                'db_table': 't_education_level',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Industry',
                'verbose_name_plural': 'Industries',
                'db_table': 't_industry',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'db_table': 't_language',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'db_table': 't_role',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='skillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Skill Category',
                'verbose_name_plural': 'Skill Categories',
                'db_table': 't_skill_category',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='socialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=30)),
                ('image_url', models.CharField(blank=True, max_length=300, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Social Network',
                'verbose_name_plural': 'Social Networks',
                'db_table': 't_social_network',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 't_tags',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('skill_category', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='infocore.skillcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'db_table': 't_skill',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=300)),
                ('account_type', models.CharField(choices=[('Free', 'Free'), ('Professional', 'Professional'), ('Premium', 'Premium'), ('Trial', 'Trial')], default='Free', max_length=30)),
                ('is_active', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('observations', models.TextField(blank=True, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'db_table': 't_account',
                'ordering': ['-start_date'],
                'managed': True,
            },
        ),
    ]
