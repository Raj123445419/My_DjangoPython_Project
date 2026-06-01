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