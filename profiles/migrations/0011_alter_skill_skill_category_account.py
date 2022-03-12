# Generated by Django 4.0.2 on 2022-03-05 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0010_skill_skill_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='profiles.skillcategory', verbose_name='Category'),
        ),
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=300)),
                ('account_type', models.CharField(choices=[('Free', 'Free'), ('Professional', 'Professional'), ('Premium', 'Premium'), ('Trial', 'Trial')], default='Free', max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
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
