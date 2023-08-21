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
    fieldsets = (
        ('Основные сведения', {
            'fields': ('first_name', 'second_name', 'last_name', 'country', 'city')
        }),
        ('Биографические данные', {
            'fields': ('university', 'birth_date', 'biography'),
            'description': 'Различные данные из биографии автора',
            'classes': ['collapse']
        }),
        ('Контакты', {
            'fields': ('email', 'phone', 'personal_page', 'facebook', 'twiter'),
            'description': 'Различные способы связатся с автором',
        }),

    )


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    actions = ['mark_as_published', 'mark_as_draft', 'mark_as_review']

    def mark_as_published(self, request, queryset):
        queryset.update(status='p')

    def mark_as_draft(self, request, queryset):
        queryset.update(status='d')

    def mark_as_review(self, request, queryset):
        queryset.update(status='r')

    mark_as_published.short_description = 'Перевести в статус Опубликовано'
    mark_as_draft.short_description = 'Перевести в статус Черновик'
    mark_as_review.short_description = 'Перевести в статус Ревью'


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

