from django.db import models

# Create your models here.



class Codata(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Address=models.CharField(max_length=70)
    Email=models.EmailField(max_length=30)
    Country=models.CharField(max_length=70)
    PhonNumber=models.CharField(max_length=10)
    Date=models.DateField(max_length=12)

    def __str__(self):
        return self.FirstName


class sidata(models.Model):
    Fullname=models.CharField(max_length=50)
    Age=models.CharField(max_length=6)
    country=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=6)
    phonnumber=models.CharField(max_length=11)


    def __str__(self):
        return self.Fullname

    pass



class page(models.Model):
    nam=models.CharField(max_length=30)
    eml=models.EmailField(max_length=30)
    pas=models.CharField(max_length=12)


    def __str__(self):
        return self.nam

    pass




class ShopProduct(models.Model):

    CATEGORY_CHOICES = (
        ('shop', 'Shop'),
        ('shop1', 'Shop1'),
        ('shop2', 'Shop2'),
        ('shop3', 'Shop3'),
        ('shop4', 'Shop4'),
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    name = models.CharField(max_length=50)

    chapter = models.CharField(max_length=10)

    price = models.CharField(max_length=10)

    image = models.ImageField(upload_to='anime/')

    def __str__(self):

        return self.name






class DeletedAccount(models.Model):

    reason = models.TextField()

    suggestion = models.TextField()

    email = models.EmailField()

    password = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email











class Product(models.Model):

    name = models.CharField(max_length=200)

    image = models.ImageField(upload_to='products/')

    page = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserOrder(models.Model):

    STATUS_CHOICES = (
        ('Placed', 'Order Placed'),
        ('Processing', 'Processing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Return Requested', 'Return Requested'),
        ('Replacement Requested', 'Replacement Requested'),
        ('Return Approved', 'Return Approved'),
        ('Replacement Approved', 'Replacement Approved'),
        ('Returned & Refunded', 'Returned & Refunded'),
        ('Replacement Dispatched', 'Replacement Dispatched'),
    )

    user = models.ForeignKey(sidata, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    shipping_address = models.TextField()
    country = models.CharField(max_length=50, default='India')
    preferred_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Placed')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_method = models.CharField(max_length=60, default='Cash on Delivery (COD)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.order_number} - {self.full_name} ({self.status})"


class OrderItem(models.Model):

    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, related_name='items')
    manga_name = models.CharField(max_length=100)
    chapter = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.quantity}x {self.manga_name} in #{self.order.order_number}"


class ReadingHistory(models.Model):

    user = models.ForeignKey(sidata, on_delete=models.CASCADE, related_name='reading_history')
    manga = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
    manga_name = models.CharField(max_length=100)
    last_chapter = models.IntegerField(default=1)
    last_read_at = models.DateTimeField(auto_now=True)
    manga_image = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['-last_read_at']
        unique_together = ('user', 'manga')

    def __str__(self):
        return f"{self.user.Fullname} read {self.manga_name} (Ch {self.last_chapter})"


class OrderReturnRequest(models.Model):

    REQUEST_TYPE_CHOICES = (
        ('Return', 'Return (Refund)'),
        ('Replacement', 'Replacement (Exchange)'),
    )

    REASON_CHOICES = (
        ('Damaged Product / Pages Torn', 'Damaged Product / Pages Torn'),
        ('Defective Printing / Missing Pages', 'Defective Printing / Missing Pages'),
        ('Wrong Manga Volume Delivered', 'Wrong Manga Volume Delivered'),
        ('Language / Edition Mismatch', 'Language / Edition Mismatch'),
        ('Other Issue', 'Other Issue'),
    )

    STATUS_CHOICES = (
        ('Pending Verification', 'Pending Verification'),
        ('Approved for Return & Refund', 'Approved for Return & Refund'),
        ('Approved for Replacement', 'Approved for Replacement'),
        ('Replacement Dispatched', 'Replacement Dispatched'),
        ('Rejected - Damage Required for Return', 'Rejected - Damage Required for Return (Replacement Eligible)'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    )

    order = models.OneToOneField(UserOrder, on_delete=models.CASCADE, related_name='return_request')
    user = models.ForeignKey(sidata, on_delete=models.SET_NULL, null=True, blank=True)
    request_type = models.CharField(max_length=30, choices=REQUEST_TYPE_CHOICES, default='Return')
    reason = models.CharField(max_length=100, choices=REASON_CHOICES)
    is_damaged = models.BooleanField(default=False, help_text="True if item arrived damaged")
    description = models.TextField(help_text="Detailed explanation from customer")
    refund_payment_method = models.CharField(max_length=60, default='Cash on Pickup', help_text="Cash on Pickup / UPI / Bank Transfer")
    refund_details = models.CharField(max_length=150, blank=True, null=True, help_text="UPI ID or Phone or Account Number for refund")
    damage_image = models.ImageField(upload_to='return_proofs/', null=True, blank=True)
    status = models.CharField(max_length=70, choices=STATUS_CHOICES, default='Pending Verification')
    admin_reply = models.TextField(blank=True, null=True, help_text="Admin verification decision and reply message to customer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.request_type} Request for Order #{self.order.order_number} ({self.status})"