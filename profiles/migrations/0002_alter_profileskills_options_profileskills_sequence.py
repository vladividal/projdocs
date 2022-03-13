# Generated by Django 4.0.2 on 2022-03-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileskills',
            options={'managed': True, 'ordering': ['sequence'], 'verbose_name': 'Profile Skill', 'verbose_name_plural': 'Profile Skills'},
        ),
        migrations.AddField(
            model_name='profileskills',
            name='sequence',
            field=models.IntegerField(default=1),
        ),
    ]