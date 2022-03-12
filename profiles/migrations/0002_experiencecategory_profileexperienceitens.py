# Generated by Django 4.0.2 on 2022-03-02 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='experienceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Experience Category',
                'verbose_name_plural': 'Experience Categories',
                'db_table': 't_experience_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='profileExperienceItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.TextField(blank=True, null=True)),
                ('sequence', models.IntegerField()),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('experience_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.experiencecategory')),
                ('profile_experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profileexperience')),
            ],
            options={
                'verbose_name': 'Profile Experience Item',
                'verbose_name_plural': 'Profile Experiences Itens',
                'db_table': 't_profile_experience_itens',
                'ordering': ['sequence'],
                'managed': True,
            },
        ),
    ]