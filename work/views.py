from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    ShopProduct, Codata, Product, page, sidata, DeletedAccount,
    UserOrder, OrderItem, ReadingHistory, OrderReturnRequest
)
import re
import random
from django.utils import timezone
from urllib import request 
from django.http import JsonResponse
from django.contrib import messages
from django.utils.safestring import mark_safe

def get_current_user(request):
    email = request.session.get('email')
    fullname = request.session.get('fullname')
    if email:
        user = sidata.objects.filter(email__iexact=email).first()
        if user:
            return user
    if fullname:
        return sidata.objects.filter(Fullname=fullname).first()
    return None


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
            request.session['email'] = k
            request.session['phone'] = m

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
            u_obj = user.first()
            request.session['fullname'] = u_obj.Fullname
            request.session['email'] = u_obj.email
            request.session['phone'] = u_obj.phonnumber

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
    query = request.GET.get('q', '').strip()
    products = []
    seen_names = set()

    if query:
        # 1. Search in ShopProduct (Primary catalog with chapters and prices)
        shop_matches = ShopProduct.objects.filter(
            name__icontains=query
        )

        for sp in shop_matches:
            name_clean = sp.name.strip().lower()
            if name_clean not in seen_names:
                seen_names.add(name_clean)

                # Format chapters count cleanly
                ch_val = str(sp.chapter).strip()
                if 'chapter' not in ch_val.lower() and 'vol' not in ch_val.lower():
                    ch_display = f"{ch_val} Chapters"
                else:
                    ch_display = ch_val

                # Format price cleanly
                price_val = str(sp.price).replace('$', '').replace('₹', '').replace('%', '').strip()
                price_display = f"${price_val}" if price_val else "$10"

                products.append({
                    'name': sp.name,
                    'image': sp.image.url if sp.image else '',
                    'page': f'/manga/{sp.id}/',
                    'chapter': ch_display,
                    'price': price_display,
                })

        # 2. Search Product for backward compatibility & ensure chapter/price are populated
        legacy_matches = Product.objects.filter(
            name__icontains=query
        )

        for product in legacy_matches:
            name_clean = product.name.strip().lower()
            if name_clean not in seen_names:
                seen_names.add(name_clean)

                matching_sp = ShopProduct.objects.filter(name__icontains=product.name.strip()).first()
                if matching_sp:
                    ch_val = str(matching_sp.chapter).strip()
                    if 'chapter' not in ch_val.lower() and 'vol' not in ch_val.lower():
                        ch_display = f"{ch_val} Chapters"
                    else:
                        ch_display = ch_val
                    price_val = str(matching_sp.price).replace('$', '').replace('₹', '').replace('%', '').strip()
                    price_display = f"${price_val}" if price_val else "$10"
                    target_page = f'/manga/{matching_sp.id}/'
                    target_image = matching_sp.image.url if matching_sp.image else (product.image.url if product.image else '')
                else:
                    ch_display = "12 Chapters"
                    price_display = "$10"
                    target_page = product.page if product.page else '/Shop/'
                    target_image = product.image.url if product.image else ''

                products.append({
                    'name': product.name,
                    'image': target_image,
                    'page': target_page,
                    'chapter': ch_display,
                    'price': price_display,
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

    # Track reading history if user is logged in
    curr_user = get_current_user(request)
    if curr_user:
        try:
            ReadingHistory.objects.update_or_create(
                user=curr_user,
                manga=product,
                defaults={
                    'manga_name': product.name,
                    'last_chapter': 1,
                    'manga_image': product.image.url if product.image else ''
                }
            )
        except Exception as e:
            print(f"Reading history error: {e}")

    return render(request, 'manga_detail.html', {
        'product': product,
        'total_chapters': total_chapters,
        'chapter_list': chapter_list,
        'related_products': related_products,
    })


# DEDICATED HIGH-PERFORMANCE MANGA READER
def manga_chapter_reader(request, id, chapter_num=1):
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
            'url': product.image.url if product.image else '/media/anime/first.jpg',
            'title': f'{product.name} - Chapter {chapter_num} Preview'
        })

    prev_chapter = chapter_num - 1 if chapter_num > 1 else None
    next_chapter = chapter_num + 1 if chapter_num < total_chapters else None

    # Track reading history with exact chapter
    curr_user = get_current_user(request)
    if curr_user:
        try:
            ReadingHistory.objects.update_or_create(
                user=curr_user,
                manga=product,
                defaults={
                    'manga_name': product.name,
                    'last_chapter': int(chapter_num),
                    'manga_image': product.image.url if product.image else ''
                }
            )
        except Exception as e:
            print(f"Reading history error: {e}")

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


# USER PROFILE DASHBOARD
def user_profile(request):
    user = get_current_user(request)
    if not user:
        messages.warning(request, "Please Login or Signup to view your Profile 🔐")
        return redirect('/Account/')

    # Reading History
    reading_history = ReadingHistory.objects.filter(user=user).select_related('manga').order_by('-last_read_at')
    last_read = reading_history.first()

    # Orders
    orders = UserOrder.objects.filter(user=user).prefetch_related('items').order_by('-created_at')

    # Total Read & Orders Stats
    total_read_manga = reading_history.count()
    total_orders = orders.count()

    return render(request, 'profile.html', {
        'user_obj': user,
        'reading_history': reading_history,
        'last_read': last_read,
        'orders': orders,
        'total_read_manga': total_read_manga,
        'total_orders': total_orders,
    })


# PLACE ORDER (COD & ONLINE)
def place_order(request):
    if request.method != "POST":
        return redirect('/Cart/')

    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "Your cart is empty! Add manga to cart first 🛒")
        return redirect('/Cart/')

    customer_name = request.POST.get('customer_name', '').strip()
    email = request.POST.get('email', '').strip()
    phone = request.POST.get('phone', '').strip()
    shipping_address = request.POST.get('shipping_address', '').strip()
    preferred_date = request.POST.get('preferred_date', '').strip() or None
    payment_method = request.POST.get('payment_method', 'Cash on Delivery (COD)').strip() or 'Cash on Delivery (COD)'

    if not customer_name or not phone or not shipping_address:
        messages.error(request, "Please provide your Full Name, Phone Number, and Delivery Address ⚠️")
        return redirect('/Cart/')

    user = get_current_user(request)

    # Calculate Grand Total
    grand_total = 0
    for key, item in cart.items():
        clean_price = str(item.get('price', 0)).replace('₹', '').replace('$', '').replace('%', '').strip()
        try:
            price = float(clean_price)
        except ValueError:
            price = 10.0
        qty = int(item.get('quantity', 1))
        grand_total += (price * qty)

    # Generate Unique Order Number
    order_num = f"MAB-{random.randint(10000, 99999)}"
    while UserOrder.objects.filter(order_number=order_num).exists():
        order_num = f"MAB-{random.randint(10000, 99999)}"

    # Create Order
    order = UserOrder.objects.create(
        order_number=order_num,
        user=user,
        full_name=customer_name,
        email=email or (user.email if user else ''),
        phone=phone,
        shipping_address=shipping_address,
        country=user.country if (user and user.country) else 'India',
        preferred_date=preferred_date,
        total_amount=grand_total,
        status='Placed',
        payment_method=payment_method
    )

    # Create Order Items
    for key, item in cart.items():
        clean_price = str(item.get('price', 0)).replace('₹', '').replace('$', '').replace('%', '').strip()
        try:
            price = float(clean_price)
        except ValueError:
            price = 10.0
        qty = int(item.get('quantity', 1))
        subtotal = price * qty

        OrderItem.objects.create(
            order=order,
            manga_name=item.get('name', 'Manga Edition'),
            chapter=item.get('chapter', 'Volume 1'),
            price=price,
            quantity=qty,
            subtotal=subtotal,
            image=item.get('image', '')
        )

    # Clear Cart Session
    request.session['cart'] = {}

    messages.success(
        request,
        mark_safe(
            f"🎉 <b>Order Placed Successfully!</b><br>"
            f"Order ID: <b>#{order.order_number}</b> | Total: <b>${order.total_amount:.2f}</b><br>"
            f"Payment Mode: <b>{order.payment_method}</b>. You can track your shipment live below! 🚀"
        )
    )

    return redirect('/MyOrders/')


# LIVE ORDER TRACKING & MANAGEMENT
def my_orders(request):
    user = get_current_user(request)
    user_email = request.session.get('email')
    user_phone = request.session.get('phone')

    orders = []
    if user:
        orders = UserOrder.objects.filter(user=user).prefetch_related('items').order_by('-created_at')
    elif user_email:
        orders = UserOrder.objects.filter(email__iexact=user_email).prefetch_related('items').order_by('-created_at')
    elif user_phone:
        orders = UserOrder.objects.filter(phone=user_phone).prefetch_related('items').order_by('-created_at')

    # Order search by ID
    search_q = request.GET.get('track', '').strip()
    if search_q:
        searched = UserOrder.objects.filter(order_number__icontains=search_q).prefetch_related('items')
        if searched.exists():
            orders = searched

    return render(request, 'manage_order.html', {
        'orders': orders,
        'user_obj': user,
        'search_q': search_q
    })


# UPDATE DELIVERY ADDRESS & DETAILS
def update_order(request, order_id):
    if request.method != "POST":
        return redirect('/MyOrders/')

    order = get_object_or_404(UserOrder, id=order_id)

    if order.status not in ['Placed', 'Processing']:
        messages.error(request, f"Order #{order.order_number} cannot be modified because it is {order.get_status_display()} ⚠️")
        return redirect('/MyOrders/')

    new_address = request.POST.get('shipping_address', '').strip()
    new_phone = request.POST.get('phone', '').strip()

    if not new_address or not new_phone:
        messages.error(request, "Delivery Address and Contact Number cannot be empty ⚠️")
        return redirect('/MyOrders/')

    order.shipping_address = new_address
    order.phone = new_phone
    order.save()

    messages.success(request, f"Order #{order.order_number} delivery details updated successfully! ✅")
    return redirect('/MyOrders/')


# CANCEL ORDER (ONLY ALLOWED BEFORE DISPATCH)
def cancel_order(request, order_id):
    if request.method != "POST":
        return redirect('/MyOrders/')

    order = get_object_or_404(UserOrder, id=order_id)

    # Prevent cancellation once out for delivery or delivered
    if order.status in ['Out for Delivery', 'Delivered']:
        messages.error(
            request,
            f"Order #{order.order_number} is already '{order.status}'. Cancellation is not possible after dispatch! You can apply for return/replacement once received ⚠️"
        )
        return redirect('/MyOrders/')

    if order.status not in ['Placed', 'Processing']:
        messages.error(request, f"Order #{order.order_number} cannot be cancelled as it is already {order.get_status_display()} ⚠️")
        return redirect('/MyOrders/')

    order.status = 'Cancelled'
    order.save()

    messages.warning(request, f"Order #{order.order_number} has been cancelled successfully 🛑")
    return redirect('/MyOrders/')


# SUBMIT RETURN / REPLACEMENT REQUEST (AFTER DELIVERY)
def submit_return_request(request, order_id):
    if request.method != "POST":
        return redirect('/MyOrders/')

    order = get_object_or_404(UserOrder, id=order_id)

    eligible_statuses = ['Delivered', 'Return Requested', 'Replacement Requested', 'Return Approved', 'Replacement Approved']
    if order.status not in eligible_statuses:
        messages.error(request, f"Return or Replacement can only be requested after the order is Delivered ⚠️")
        return redirect('/MyOrders/')

    request_type = request.POST.get('request_type', 'Return').strip()
    reason = request.POST.get('reason', '').strip()
    is_damaged = request.POST.get('is_damaged') == 'on' or request.POST.get('is_damaged') == 'true'
    description = request.POST.get('description', '').strip()
    refund_payment_method = request.POST.get('refund_payment_method', 'Cash on Pickup').strip()
    refund_details = request.POST.get('refund_details', '').strip()
    damage_image = request.FILES.get('damage_image')

    if not reason or not description:
        messages.error(request, "Please select a reason and provide description for your request ⚠️")
        return redirect('/MyOrders/')

    user = get_current_user(request) or order.user

    # Create or update return request record
    return_obj, created = OrderReturnRequest.objects.update_or_create(
        order=order,
        defaults={
            'user': user,
            'request_type': request_type,
            'reason': reason,
            'is_damaged': is_damaged,
            'description': description,
            'refund_payment_method': refund_payment_method,
            'refund_details': refund_details,
            'status': 'Pending Verification',
        }
    )

    if damage_image:
        return_obj.damage_image = damage_image
        return_obj.save()

    # Update order status
    order.status = 'Return Requested' if request_type == 'Return' else 'Replacement Requested'
    order.save()

    damage_note = " (Damage Claimed for Cash Refund)" if (request_type == 'Return' and is_damaged) else ""
    messages.success(
        request,
        mark_safe(
            f"📬 <b>{request_type} Request Submitted for Order #{order.order_number}!{damage_note}</b><br>"
            f"Reason: <b>{reason}</b> | Mode: <b>{refund_payment_method}</b><br>"
            f"Backend Admin will verify the reason. Check Admin reply & decision right on this page! 💬"
        )
    )

    return redirect(f'/MyOrders/?track={order.order_number}')
