from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


class Word(models.Model):
    word_text = models.CharField(max_length=100)

    pub_date = models.DateTimeField('date published')


class Translation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    text = models.CharField(max_length=100)

    correct = models.BooleanField(default=False)


class Message(models.Model):
    chat = models.ForeignKey(
        Word,
        verbose_name='Чат под слово-перевод',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)
