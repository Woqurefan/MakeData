# Generated by Django 3.2.13 on 2022-05-10 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_alter_db_tool_stime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_tool',
            name='stime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
