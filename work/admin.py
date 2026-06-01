from django.contrib import admin

from work.models import Codata, page, ShopProduct, sidata, Product , DeletedAccount

# Register your models here.



admin.site.register(Codata)
admin.site.register(sidata)
admin.site.register(Product)
admin.site.register(page)
admin.site.register(ShopProduct)
admin.site.register(DeletedAccount)