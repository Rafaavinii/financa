# Generated by Django 4.1.7 on 2023-07-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='concluida',
            field=models.BooleanField(default=None),
        ),
    ]