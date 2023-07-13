from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class Service(models.Model):
    category = models.CharField(max_length=100,default='Hair Services')
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')
    image = models.ImageField(upload_to='service_images/', null=True)
    duration = models.DurationField()

    def __str__(self):
        return self.name
class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class StaffMember(models.Model):
    name = models.CharField(max_length=50)
    branches = models.ManyToManyField(Branch)
    image = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profession = models.CharField(max_length=100,null=True)
    address = models.TextField()
    def __str__(self):
        return self.name
    
class Packages(models.Model):
    VALIDITY_CHOICES = (
        ('1M', '1 month'),
        ('6M', '6 months'),
        ('1Y', '1 year'),
        # Add more validity options here
    )
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')
    services = models.ManyToManyField(Service)
    validity = models.CharField(max_length=2, choices=VALIDITY_CHOICES, default='1M')
    
    def __str__(self):
        return self.name
    

class ServiceUsage(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    usage_count = models.PositiveIntegerField(default=0, help_text='Number of times the service can be used within the validity period')
    def __str__(self):
        return f"{self.package} - {self.service} ({self.usage_count})"

class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.PROTECT)
    services = models.ManyToManyField(Service)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=220, null=True)
    cancel_time = models.TimeField(null=True, blank=True)
    cancellation_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    discounted_price = MoneyField(max_digits=12,decimal_places=2,default_currency='AED',null = True)
    amount_to_be_paid = MoneyField(max_digits=14,decimal_places=2,default_currency='AED',null = True)
    date = models.DateField(null=True)
    branch = models.ForeignKey('Branch', on_delete=models.PROTECT,null=True)
    tips = MoneyField(max_digits=12,decimal_places=2,default_currency='AED',default=0.00)

 # New fields
    PAYMENT_STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount_paid = MoneyField(max_digits=14, decimal_places=2, default_currency='AED', null=True, blank=True)

    def str(self):
        return f"{self.customer} - {self.services} with {self.staff_member} on {self.start_time}"

    

class Invoice(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT)
    tax = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    discounted_price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    tips = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    price_to_be_paid = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)

class FamilyMember(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    number = models.CharField(max_length=20)

    def str(self):
        return self.name

class Membership(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    family_members = models.ManyToManyField(FamilyMember)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.package.name} Membership"

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')

    def str(self):
        return self.name