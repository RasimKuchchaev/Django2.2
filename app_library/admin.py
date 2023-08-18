from django.contrib import admin
from app_library.models import Publisher, Author, Book


# class BookInline(admin.TabularInline):
class BookInline(admin.StackedInline):
    model = Book

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['is_active', 'city']
    inlines = [BookInline]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'biography']


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

