from django.contrib import admin

# Register your models here.
from web.models import Expense, Income, Token


class ExpenseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('text', {'fields': ['text']}),
        ('Date', {'fields': ['date']}),
        ('amount', {'fields': ['amount']}),
        ('user', {'fields': ['user']}),
    ]
    list_filter = ['date', 'amount', 'user']
    list_display = ('text', 'amount', 'date')
    list_per_page = 5
    search_fields = ['text']


class IncomeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('text', {'fields': ['text']}),
        ('Date', {'fields': ['date']}),
        ('amount', {'fields': ['amount']}),
        ('user', {'fields': ['user']}),
    ]
    list_filter = ['date', 'amount', 'user']
    list_display = ('text', 'amount', 'date')
    list_per_page = 5
    search_fields = ['text']


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')
    search_fields = ['user']


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Token,TokenAdmin)
