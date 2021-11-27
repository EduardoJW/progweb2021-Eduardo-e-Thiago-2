# Generated by Django 3.2.6 on 2021-11-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardMakerApp', '0002_alter_carta_poder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='tipo',
            field=models.CharField(choices=[('equipment', 'Equipment'), ('spell', 'Spell'), ('fighter', 'Fighter')], help_text='Digite o tipo da carta', max_length=100),
        ),
    ]
