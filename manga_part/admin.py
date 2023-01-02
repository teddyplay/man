from django.contrib import admin
from .models import Manga
from .models import Genre
from .models import Type_of_manga
from .models import Comment




admin.site.register(Genre)

admin.site.register(Manga)

admin.site.register(Type_of_manga)

admin.site.register(Comment)







