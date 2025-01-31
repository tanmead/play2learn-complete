from django.contrib import admin
from common.admin import Play2LearnAdmin

from .models import Review

@admin.register(Review)
class ReviewAdmin(Play2LearnAdmin):
    model = Review
    list_display = ['review', 'first_name', 'last_name', 'created', 'user']
