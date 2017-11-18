from django.contrib import admin
from .models import Post            # include the Post model

# Register your models here.
admin.site.register(Post)           # register the model to admin