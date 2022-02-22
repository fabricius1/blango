from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ['title', 'slug', 'published_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)