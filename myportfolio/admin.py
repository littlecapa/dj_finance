from django.contrib import admin
from django import forms

# Register your models here.

from .models import shareIds, SearchHistory, Category, Link, blogEntry, blog_shares, attrNames, strategy, strategyShares, transaction, upload
from .forms import BlogEntryAdminForm

admin.site.register(shareIds)
admin.site.register(transaction)
admin.site.register(upload)
admin.site.register(SearchHistory)
admin.site.register(blog_shares)
admin.site.register(attrNames)
admin.site.register(strategy)
admin.site.register(strategyShares)

class BlogEntryAdmin(admin.ModelAdmin):
    form = BlogEntryAdminForm
    
admin.site.register(blogEntry, BlogEntryAdmin)

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