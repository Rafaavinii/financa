# Generated by Django 4.1.7 on 2023-07-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0002_alter_despesa_categoria_alter_despesa_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('alimentacao', 'Alimentação'), ('moradia', 'Moradia'), ('educacao', 'Educação'), ('lazer', 'Lazer'), ('saude', 'Saude'), ('viagem', 'Viagem'), ('entreterimento', 'Entreterimento'), ('roupas', 'Roupas'), ('cartao', 'Cartão'), ('outro', 'Outro')], max_length=50),
        ),
    ]
