from django.shortcuts import render, redirect, get_object_or_404
from .models import shopproduct, shopproduct
import re
from urllib import request 
from django.http import JsonResponse
from django.contrib import messages
from django.utils.safestring import mark_safe
from work.models import Codata, Product, page, sidata
from .models import DeletedAccount

# Create your views here.


def ind(request):
      return render(request, 'index.html')

def home(request):

    data = shopproduct.objects.filter(category='shop')

    return render(
        request,
        'Home.html',
        {'product': data}
    )

def shop(request):

    data = shopproduct.objects.filter(category='shop')

    return render(
        request,
        'shop.html',
        {'product': data}
    )


def shop1(request):

    data = shopproduct.objects.filter(category='shop1')

    return render(
        request,
        'shop1.html',
        {'product': data}
    )


def shop2(request):

    data = shopproduct.objects.filter(category='shop2')

    return render(
        request,
        'shop2.html',
        {'product': data}
    )


def shop3(request):

    data = shopproduct.objects.filter(category='shop3')

    return render(
        request,
        'shop3.html',
        {'product': data}
    )


def shop4(request):

    data = shopproduct.objects.filter(category='shop4')

    return render(
        request,
        'shop4.html',
        {'product': data}
    )

def aboutus(request):
      return render (request,'aboutus.html')

def contect(request):
      return render(request,'contect.html')

def account(request):
      return render(request,'account.html')

def sign(request):
      return render(request,'sign.html')

def addtocart(request, id):

    product = get_object_or_404(shopproduct, id=id)

    cart = request.session.get('cart', {})

    product_id = str(product.id)

    # CLEAN PRICE
    price = str(product.price).replace('₹', '').replace('$', '').replace('%', '').strip()

    if product_id in cart:

        cart[product_id]['quantity'] += 1

        messages.success(
            request,
            f"{product.name} quantity updated in cart 🛒"
        )

    else:

        cart[product_id] = {

            'name': product.name,

            'chapter': product.chapter,

            'price': price,

            'image': product.image.url,

            'quantity': 1,
        }

        messages.success(
            request,
            f"{product.name} added to cart successfully 🛒"
        )

    request.session['cart'] = cart

    # SAME PAGE REDIRECT
    return redirect(request.META.get('HTTP_REFERER', '/'))



def cart(request):

    cart = request.session.get('cart', {})

    grand_total = 0

    for key, item in cart.items():

        # CLEAN PRICE
        price = str(item['price'])

        price = price.replace('₹', '')
        price = price.replace('$', '')
        price = price.replace('%', '')
        price = price.strip()

        # CONVERT
        price = float(price)

        quantity = int(item['quantity'])

        item['total'] = price * quantity

        grand_total += item['total']

    return render(request, 'cart.html', {

        'cart': cart,

        'grand_total': grand_total,
    })

pass

def codata(request):
      a=request.POST.get('Fname')
      b=request.POST.get('Lname')
      c=request.POST.get('Address')
      d=request.POST.get('Email')
      e=request.POST.get('Country')
      f=request.POST.get('Fnumber')
      g=request.POST.get('Date')

      obj=Codata(FirstName=a,LastName=b,Address=c,Email=d,Country=e,PhonNumber=f,Date=g)
      obj.save()

      return redirect ('/Contect/')


def sipage(request):

      h = request.POST.get('funame')
      i = request.POST.get('age')
      j = request.POST.get('contur')
      k = request.POST.get('email')
      l = request.POST.get('password')
      m = request.POST.get('phnumber')

      # Empty field check
      if h == "" or i == "" or j == "" or k == "" or l == "" or m == "":

            messages.error(
                  request,
                  "All Fields Are Required ⚠️"
            )

            return redirect('/Sign')

      # Account already exists
      elif sidata.objects.filter(email=k).exists():

            messages.warning(
                  request,
                  "You Already Have An Account. Please Login 🔐"
            )

            return redirect('/Account/')

      # New account save
      else:

            obj = sidata(
                  Fullname=h,
                  Age=i,
                  country=j,
                  email=k,
                  password=l,
                  phonnumber=m
            )

            obj.save()
            request.session['fullname'] = h

            messages.success(
                  request,
                  "Welcome To The Anime World 🌌"
            )

            return redirect('/Home/')







def logincheck(request):

      # CHECK USER ALREADY LOGIN
      if request.session.get('fullname'):

            messages.warning(
                  request,
                  "Another User Is Already Logged In ⚠️ Please Log Out First 🔐"
            )

            return redirect('/Home')

      # GET DATA
      n = request.POST.get('mail')
      o = request.POST.get('pass')
      p = request.POST.get('phnumber')

      # EMPTY FIELD CHECK
      if not n or not o or not p:

            messages.error(
                  request,
                  'All Fields Are Required ⚠️'
            )

            return redirect('/Account')

      # LOGIN CHECK (CASE INSENSITIVE EMAIL)
      user = sidata.objects.filter(
            email__iexact=n,
            password=o,
            phonnumber=p
      )

      # LOGIN SUCCESS
      if user.exists():

            # SAVE SESSION
            request.session['fullname'] = user.first().Fullname

            messages.success(
                  request,
                  'Welcome Back Which Manga Are We Completing Today My Master 👑'
            )

            return redirect('/Home/')

      # LOGIN FAILED
      else:

            messages.warning(
                  request,
                  mark_safe(
                        'Signup Required Before Entering The Anime World 🌌.<br>'
                        '<center>Click on Don’t have an account?</center>'
                  )
            )

            return redirect('/Account/')













def logout(request):

    # CHECK USER LOGIN OR NOT
    if not request.session.get('fullname'):

        messages.error(
            request,
            "No User Is Logged In ⚠️"
        )

        return redirect('/Home')

    # LOGOUT
    request.session.flush()

    messages.success(
        request,
        "Logout Successful 👋"
    )

    return redirect('/Home/')




def increase_quantity(request, key):

    cart = request.session.get('cart', {})

    if key in cart:

        cart[key]['quantity'] += 1

    request.session['cart'] = cart

    return redirect('/Cart/')


def decrease_quantity(request, key):

    cart = request.session.get('cart', {})

    if key in cart:

        if cart[key]['quantity'] > 1:

            cart[key]['quantity'] -= 1

        else:

            del cart[key]

    request.session['cart'] = cart

    return redirect('/Cart/')



def remove_cart_item(request, id):

    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:

        item_name = cart[product_id]['name']

        del cart[product_id]

        messages.success(
            request,
            f"{item_name} removed from cart successfully 🗑️"
        )

    request.session['cart'] = cart

    return redirect('/Cart/')







def DeleteAccount(request):

    if request.method == "POST":


        print(request.POST)

        a = request.POST.get('email')
        b = request.POST.get('password')
        c = request.POST.get('phnumber')

        # CHECK INDIVIDUALLY
        email_wrong = not sidata.objects.filter(
            email__iexact=a
        ).exists()

        password_wrong = not sidata.objects.filter(
            password__iexact=b
        ).exists()

        phone_wrong = not sidata.objects.filter(
            phonnumber__iexact=c
        ).exists()


        # ALL WRONG
        if email_wrong and password_wrong and phone_wrong:

            messages.error(
                request,
                "Wrong Email, Password and Phone Number ❌"
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))


        # EMAIL + PASSWORD WRONG
        elif email_wrong and password_wrong:

            messages.error(
                request,
                "Wrong Email and Password ❌"
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))


        # EMAIL + NUMBER WRONG
        elif email_wrong and phone_wrong:

            messages.error(
                request,
                "Wrong Email and Phone Number ❌"
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))


        # PASSWORD + NUMBER WRONG
        elif password_wrong and phone_wrong:

            messages.error(
                request,
                "Wrong Password and Phone Number ❌"
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))


        # ONLY EMAIL WRONG
        elif email_wrong:

            messages.error(
                request,
                "Wrong Email ❌"
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))


        # ONLY PASSWORD WRONG
        elif password_wrong:

            messages.error(
                request,
                "Wrong Password ❌"
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))


        # ONLY PHONE WRONG
        elif phone_wrong:

            messages.error(
                request,
                "Wrong Phone Number ❌"
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))


        # FINAL ACCOUNT MATCH
        user = sidata.objects.filter(
            email__iexact=a,
            password__iexact=b,
            phonnumber__iexact=c
        )

        if user.exists():

            DeletedAccount.objects.create(

        reason=request.POST.get('reason') or 'Not Selected',

        suggestion=request.POST.get('suggestion'),

        email=a,

        password=b,

        phone=c

    )

            user.delete()

            request.session.flush()

            messages.success(
                request,
                "Your Account Has Been Deleted Successfully 🗑️"
            )

            return redirect('/')


        else:

            messages.error(
                request,
                "These Details Do Not Belong To The Same Account ❌"
            )

            return redirect('/')


















# LIVE SEARCH
def live_search(request):

    query = request.GET.get('q')

    products = []

    if query:

        search = Product.objects.filter(
            name__icontains=query
        )

        for product in search:

            products.append({

                'name': product.name,

                'image': product.image.url,

                'page': product.page

            })

    return JsonResponse({
        'products': products
    })