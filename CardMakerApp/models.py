# Create your models here.
from django.db import models
from django.db.models.fields import EmailField

PODER_DE_ATAQUE= [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10","10")
    ]
TIPO= [
    ("Equipment", "Equipment"),
    ("Spell", "Spell"),
    ("Fighter", "Fighter"),
    ]

CLASSE= [
    ("Necromancer", "Necromancer"),
    ("Forest Folk", "Forest Folk"),
    ("Fighter", "Fighter"),
    ("Mage", "Mage"),
    ("Royal Kingdom", "Royal Kingdom"),
    ("Neutral", "Neutral"),
    ]
# Create your models here.

#Nome( topo da direita), Poder de ataque (topo da esquerda), Raça (tipo fiend do yugioh), efeito (textao), e...
#tipo e classe
#mas qual eh o tipo e qual eh a class?
class Carta(models.Model):
    nome = models.CharField(max_length=100, help_text='Digite o nome da carta')
    #poder = models.IntegerField(verbose_name='Poder de ataque', help_text='Digite o poder de ataque da carta')
    poder = models.CharField(max_length=2, choices = PODER_DE_ATAQUE, help_text='Escolha o poder de ataque')
    raca = models.CharField(verbose_name='Raça',max_length=100, help_text='Digite a raça da carta')
    efeito = models.CharField(max_length=100, help_text='Digite o efeito da carta')
    tipo = models.CharField(max_length=100, choices = TIPO, help_text='Escolha o tipo')
    classe = models.CharField(max_length=100, choices = CLASSE, help_text='Escolha a classe')

    def __str__(self):
        return self.nome + ' / ' + str(self.poder) + ' / ' + self.tipo + " " + self.classe

class Usuario(models.Model):
    username = models.CharField(max_length=100, help_text='Digite o nome de usuário')
    password = models.CharField(max_length=100, help_text='Digite a sua senha')
    email = models.EmailField(max_length=200, help_text='Entre com o seu email')

    def __str__(self):
        return self.username + " " + self.email