# Generated by Django 3.1.3 on 2022-04-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0011_auto_20220420_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
