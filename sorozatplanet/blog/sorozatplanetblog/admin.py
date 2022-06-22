from django.contrib import admin
from .models import Post

admin.site.register(Post) #az admin felületről elérhetők a posztok
