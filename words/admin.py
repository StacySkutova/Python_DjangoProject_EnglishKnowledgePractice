from django.contrib import admin

from .models import Word, Translation, Message

admin.site.register(Word)

admin.site.register(Translation)

admin.site.register(Message)
