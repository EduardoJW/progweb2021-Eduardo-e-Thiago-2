# Generated by Django 3.2.6 on 2021-11-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardMakerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='poder',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], help_text='Escolha o poder de ataque', max_length=2),
        ),
    ]