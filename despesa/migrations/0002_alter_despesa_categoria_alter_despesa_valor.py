# Generated by Django 4.1.7 on 2023-07-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('alimentacao', 'Alimentação'), ('moradia', 'Moradia'), ('educacao', 'Educação'), ('lazer', 'Lazer'), ('saude', 'Saude'), ('outro', 'Outro')], max_length=50),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='valor',
            field=models.FloatField(),
        ),
    ]
