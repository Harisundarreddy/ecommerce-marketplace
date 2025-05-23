from django.contrib import admin
from marketplace.models import Product,CustomOrder,ChatMessage

# Register your models here.


class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_message', 'created_at', 'is_admin', 'unseen')
    readonly_fields = ('is_admin', 'unseen')
    fields = ('user', 'message') 

    def save_model(self, request, obj, form, change):
        obj.is_admin = True
        obj.unseen = True
        super().save_model(request,obj,form,change)

    def short_message(self,obj):
        return obj.message[:50]
    

admin.site.register(ChatMessage,ChatAdmin)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'location', 'pod_customizable', 'created_at')
    search_fields = ('name', 'category', 'location')
    list_filter = ('category', 'location', 'pod_customizable')

@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'custom_text', 'custom_image', 'created_at')
    search_fields = ('product__name', 'custom_text')
    list_filter = ('created_at',)