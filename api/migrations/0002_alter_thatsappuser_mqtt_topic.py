# Generated by Django 3.2 on 2021-05-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thatsappuser',
            name='mqtt_topic',
            field=models.CharField(blank=True, max_length=1000, verbose_name='topic'),
        ),
    ]