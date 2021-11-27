# Generated by Django 3.2.6 on 2021-11-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardMakerApp', '0004_alter_carta_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='classe',
            field=models.CharField(choices=[('Necromancer', 'Necromancer'), ('Forest Folk', 'Forest Folk'), ('Fighter', 'Fighter'), ('Mage', 'Mage'), ('Royal Kingdom', 'Royal Kingdom'), ('Neutral', 'Neutral')], help_text='Digite a classe da carta', max_length=100),
        ),
        migrations.AlterField(
            model_name='carta',
            name='tipo',
            field=models.CharField(choices=[('Equipment', 'Equipment'), ('Spell', 'Spell'), ('Fighter', 'Fighter')], help_text='Digite o tipo da carta', max_length=100),
        ),
    ]
