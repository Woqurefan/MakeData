# Generated by Django 3.2.13 on 2022-05-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_rename_db_cases_db_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_tool',
            name='stime',
            field=models.CharField(default='', max_length=20),
        ),
    ]
