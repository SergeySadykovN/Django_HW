from django.contrib import admin
from .models import (User,
                     Post,
                     Comment,
                     Category)


admin.site.register(User)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'created', 'content')
#     list_filter = ('created', 'user')
#     raw_id_fields = ('user',)
#     date_hierarchy = 'created'
#     ordering = ('created',)


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
