# Generated by Django 3.2 on 2021-05-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_thatsappuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thatsappuser',
            name='avatar',
            field=models.URLField(blank=True, null=True, verbose_name='avatar url'),
        ),
    ]
