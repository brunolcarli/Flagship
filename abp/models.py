from django.db import models

class Quote(models.Model):
    '''
    Define a estrutura de um Quote, para
    lembrar um pérola eternamente.
    '''
    quote = models.CharField(max_length=600, null=False, blank=False)


class Battle(models.Model):
    battling_trainer = models.ForeignKey(
        'abp.Trainer',
        on_delete=models.CASCADE
    )
    battling_leader = models.ForeignKey(
        'abp.Leader',
        on_delete=models.CASCADE
    )
    winner = models.CharField(max_length=100)
    fight_date = models.DateField(auto_now_add=True)


class Badges(models.Model):
    '''
    Define todas as insignias da liga
    '''
    BADGES = (
        ('Normal', 'Normal'),
        ('Rock', 'Rock'),
        ('Electric', 'Electric'),
        ('Ghost', 'Ghost'),
        ('Ice', 'Ice'),
        ('Poison', 'Poison'),
        ('Water', 'Water'),
        ('Dark', 'Dark'),
        ('Grass', 'Grass'),
        ('Dragon', 'Dragon'),
    )

    reference = models.CharField(
        max_length=9,
        choices=BADGES,
        unique=True,
        null=True
    )


class Trainer(models.Model):
    '''
    Define a estrutura de um Treinador (participante da liga).
    '''
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True
    )
    nickname = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True
    )
    num_badges = models.IntegerField(default=0)
    num_wins = models.IntegerField(default=0)
    num_losses = models.IntegerField(default=0)
    num_battles = models.IntegerField(default=0)
    battles = models.ManyToManyField(Battle)
    elite_tryouts = models.IntegerField(default=0)
    badges = models.ManyToManyField(Badges, null=True)


class Leader(models.Model):
    '''
    Define a estrutuda de um Lider da liga.
    Um lider pode representar um Gym Leader ou um Elite Four.
    '''
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True
    )
    nickname = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True
    )
    num_badges = models.IntegerField(default=0)
    num_wins = models.IntegerField(default=0)
    num_losses = models.IntegerField(default=0)
    num_battles = models.IntegerField(default=0)
    battles = models.ManyToManyField(Battle)
