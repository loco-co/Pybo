# Generated by Django 3.1.3 on 2022-04-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_auto_20220408_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
