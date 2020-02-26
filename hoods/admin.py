from django.contrib import admin
from .models import Post, Profile, Neighborhood, Business

# Register your models here.
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Neighborhood)
