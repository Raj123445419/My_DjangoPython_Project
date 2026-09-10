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
    list_display = ('order_number', 'full_name', 'phone', 'total_amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'payment_method')
    search_fields = ('order_number', 'full_name', 'email', 'phone', 'shipping_address')
    list_editable = ('status',)
    inlines = [OrderItemInline]
    ordering = ('-created_at',)


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
admin.site.register(sidata)
admin.site.register(Product)
admin.site.register(page)
admin.site.register(ShopProduct)
admin.site.register(DeletedAccount)