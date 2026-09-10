from django.contrib import admin
from work.models import (
    Codata, page, ShopProduct, sidata, Product, DeletedAccount,
    UserOrder, OrderItem, ReadingHistory, OrderReturnRequest
)

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('manga_name', 'chapter', 'price', 'quantity', 'subtotal')


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'full_name', 'country', 'phone', 'total_amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'country', 'created_at', 'payment_method')
    search_fields = ('order_number', 'full_name', 'email', 'phone', 'country', 'shipping_address')
    list_editable = ('status',)
    inlines = [OrderItemInline]
    ordering = ('-created_at',)


@admin.register(sidata)
class sidataAdmin(admin.ModelAdmin):
    list_display = ('Fullname', 'country', 'email', 'phonnumber', 'Age')
    search_fields = ('Fullname', 'email', 'phonnumber', 'country')
    list_filter = ('country',)

    def save_model(self, request, obj, form, change):
        from django.db.models import Q
        super().save_model(request, obj, form, change)
        if obj.country:
            clean_c = obj.country.strip()
            UserOrder.objects.filter(
                Q(user=obj) | 
                (Q(email__iexact=obj.email) if obj.email else Q(pk__in=[])) | 
                (Q(phone=obj.phonnumber) if obj.phonnumber else Q(pk__in=[]))
            ).update(country=clean_c, user=obj)


@admin.register(OrderReturnRequest)
class OrderReturnRequestAdmin(admin.ModelAdmin):
    list_display = ('order', 'request_type', 'is_damaged', 'reason', 'status', 'refund_payment_method', 'created_at')
    list_filter = ('status', 'request_type', 'is_damaged', 'refund_payment_method', 'created_at')
    search_fields = ('order__order_number', 'order__full_name', 'order__phone', 'reason', 'description', 'admin_reply')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(ReadingHistory)
class ReadingHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'manga_name', 'last_chapter', 'last_read_at')
    list_filter = ('last_read_at',)
    search_fields = ('user__Fullname', 'user__email', 'manga_name')
    ordering = ('-last_read_at',)


admin.site.register(Codata)
admin.site.register(Product)
admin.site.register(page)
admin.site.register(ShopProduct)
admin.site.register(DeletedAccount)