"""
URL configuration for mywork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.ind),
    # path('Home',views.home),
    # path('Shop',views.shop),
    # path('Shop1',views.shop1),
    # path("Shop2",views.shop2),
    # path('Shop3',views.shop3),
    # path('Shop4',views.shop4),
    # path('Aboutus',views.aboutus),
    # path('Contect',views.contect),
    # path('Account',views.account),
    # path('Sign',views.sign),
    # path('codata',views.codata),
    # path('sipage',views.sipage),
    # path('search/', views.live_search, name='live_search'),
    # path('logincheck',views.logincheck),
    # path('Logout',views.logout),
    # path('Cart', views.cart, name='art'),
    # path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
 

    path('admin/', admin.site.urls),

    path('', views.ind, name='ind'),

    path('Home/', views.home, name='home'),
    path('Shop/', views.shop, name='shop'),

    path('Shop1/', views.shop1),
    path('Shop2/', views.shop2),
    path('Shop3/', views.shop3),
    path('Shop4/', views.shop4),

    path('Aboutus/', views.aboutus, name='aboutus'),
    path('Contect/', views.contect, name='contect'),
    path('Account/', views.account, name='account'),

    path('Sign/', views.sign),
    path('codata/', views.codata),
    path('sipage/', views.sipage),

    path('search/', views.live_search, name='live_search'),

    path('logincheck/', views.logincheck),
    path('Logout/', views.logout, name='logout'),

    path('Cart/', views.cart, name='cart'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),

    path('increase/<str:key>/', views.increase_quantity),   
    path('decrease/<str:key>/', views.decrease_quantity),
    path('remove-cart-item/<int:id>/', views.remove_cart_item),
    path('DeleteAccount/', views.DeleteAccount, name='DeleteAccount'),

]



# for shop img backeand add

# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)












if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )