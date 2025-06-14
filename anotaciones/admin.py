from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'author', 'date')
    search_fields = ('titulo', 'subtitulo', 'author__username')
    list_filter = ('author', 'date')
