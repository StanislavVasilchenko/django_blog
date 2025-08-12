from django.contrib import admin

from publish.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
