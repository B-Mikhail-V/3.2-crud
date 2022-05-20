from django.contrib import admin

from logistic.models import StockProduct, Product, Stock


class StockProductInline(admin.TabularInline):
    model = StockProduct
    # formset = StockProductInlineFormset
    extra = 0

@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]

@admin.register(Stock)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]