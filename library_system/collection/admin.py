from django.contrib import admin
from .models import author, book, borrowRecord

# Register your models
admin.site.register(author)
admin.site.register(book)
admin.site.register(borrowRecord)
