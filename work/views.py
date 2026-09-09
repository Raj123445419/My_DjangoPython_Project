from django.shortcuts import render, redirect, get_object_or_404
from .models import ShopProduct
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
    data = ShopProduct.objects.filter(category='shop')

    return render(request, 'home.html', {
        'product': data
    })

def shop(request):

    data = ShopProduct.objects.filter(category='shop')

    return render(
        request,
        'shop.html',
        {'product': data}
    )


def shop1(request):

    data = ShopProduct.objects.filter(category='shop1')

    return render(
        request,
        'shop1.html',
        {'product': data}
    )


def shop2(request):

    data = ShopProduct.objects.filter(category='shop2')

    return render(
        request,
        'shop2.html',
        {'product': data}
    )


def shop3(request):

    data = ShopProduct.objects.filter(category='shop3')

    return render(
        request,
        'shop3.html',
        {'product': data}
    )


def shop4(request):

    data = ShopProduct.objects.filter(category='shop4')

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

    product = get_object_or_404(ShopProduct, id=id)

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

    return render(request, 'Cart.html', {

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

        # 1. Search in ShopProduct (links directly to dynamic manga detail page)
        shop_matches = ShopProduct.objects.filter(
            name__icontains=query
        )

        for sp in shop_matches:
            products.append({
                'name': sp.name,
                'image': sp.image.url if sp.image else '',
                'page': f'/manga/{sp.id}/',
                'chapter': f'{sp.chapter} Chapters',
                'price': sp.price,
            })

        # 2. Search Product for backward compatibility
        legacy_matches = Product.objects.filter(
            name__icontains=query
        )

        for product in legacy_matches:
            if not any(p['name'].lower() == product.name.lower() for p in products):
                products.append({
                    'name': product.name,
                    'image': product.image.url if product.image else '',
                    'page': product.page,
                    'chapter': '',
                    'price': '',
                })

    return JsonResponse({
        'products': products
    })


# MANGA INDIVIDUAL DETAIL & CHAPTERS PAGE
def manga_detail(request, id):
    product = get_object_or_404(ShopProduct, id=id)

    # Extract total chapters count accurately (handles 1130, 1,130, 1130+, etc.)
    clean_chapter_str = str(product.chapter).replace(',', '').strip()
    digits = re.findall(r'\d+', clean_chapter_str)
    total_chapters = int(digits[0]) if digits else 12
    if total_chapters < 1:
        total_chapters = 1

    chapter_list = list(range(1, total_chapters + 1))

    # Recommended / Related manga from same category
    related_products = ShopProduct.objects.filter(category=product.category).exclude(id=product.id)[:4]

    return render(request, 'manga_detail.html', {
        'product': product,
        'total_chapters': total_chapters,
        'chapter_list': chapter_list,
        'related_products': related_products,
    })


# DEDICATED HIGH-PERFORMANCE MANGA READER
def manga_chapter_reader(request, id, chapter_num):
    product = get_object_or_404(ShopProduct, id=id)

    # Extract total chapters count accurately
    clean_chapter_str = str(product.chapter).replace(',', '').strip()
    digits = re.findall(r'\d+', clean_chapter_str)
    total_chapters = int(digits[0]) if digits else 12
    if total_chapters < 1:
        total_chapters = 1

    chapter_list = list(range(1, total_chapters + 1))

    # Validate chapter_num
    if chapter_num < 1:
        chapter_num = 1
    elif chapter_num > total_chapters:
        chapter_num = total_chapters

    # Check if this manga is strictly One Piece
    is_one_piece = ('one' in product.name.lower() and 'piece' in product.name.lower()) or (product.name.strip().lower() == 'one piece')

    pages = []
    has_full_chapter = False

    if is_one_piece and chapter_num == 1:
        has_full_chapter = True
        # Page 1: p.jpg.jpeg
        pages.append({
            'page_num': 1,
            'url': '/static/img/p.jpg.jpeg',
            'title': f'{product.name} - Chapter {chapter_num} Page 1'
        })
        # Pages 2 to 52: p (1).jpg.jpeg ... p (51).jpg.jpeg
        for i in range(1, 52):
            pages.append({
                'page_num': i + 1,
                'url': f'/static/img/p ({i}).jpg.jpeg',
                'title': f'{product.name} - Chapter {chapter_num} Page {i + 1}'
            })
    else:
        # For Dragon Ball, Naruto, etc. or other chapters, show that manga's own cover image
        pages.append({
            'page_num': 1,
            'url': product.image.url if product.image else '/static/img/back.jpg',
            'title': f'{product.name} - Chapter {chapter_num} Preview'
        })

    prev_chapter = chapter_num - 1 if chapter_num > 1 else None
    next_chapter = chapter_num + 1 if chapter_num < total_chapters else None

    return render(request, 'manga_reader.html', {
        'product': product,
        'chapter_num': chapter_num,
        'total_chapters': total_chapters,
        'chapter_list': chapter_list,
        'pages': pages,
        'total_pages': len(pages),
        'has_full_chapter': has_full_chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter,
    })