# Generated by Django 4.0.2 on 2022-03-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_contracttype_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='skillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name or description')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Skill Category',
                'verbose_name_plural': 'Skill Categories',
                'db_table': 't_skill_category',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Course descriprion'),
        ),
        migrations.AlterField(
            model_name='education',
            name='education_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.educationlevel', verbose_name='Education Level'),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_name',
            field=models.CharField(max_length=200, verbose_name='Institution Name'),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_url',
            field=models.CharField(max_length=500, verbose_name='Institution/Course URL'),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='skill',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name or description'),
        ),
    ]