from django.contrib import admin

# Register your models here.

from .models import MainShares, Category, Link, SearchHistory

admin.site.register(MainShares)
admin.site.register(SearchHistory)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'url')
    list_filter = ('category',)  # Add a filter by category

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Order the queryset by the priority of the associated category
        queryset = queryset.order_by('category__priority')
        return queryset