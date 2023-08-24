from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin): # allows to make changes in the admin fields.
    # readonly_fields = ("slug",) # creates a slug field that is read only.
    prepopulated_fields = {"slug": ("title",)} # creates a slug field that is automatically populated.
    list_filter = ("author", "rating") # adds a filter to the admin page.
    list_display = ("title", "author", "rating") # adds a list display to the admin page.

admin.site.register(Book, BookAdmin)
admin.site.register(Author)

