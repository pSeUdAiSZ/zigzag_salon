from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


from .models import Branch

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'address', 'phone_number', 'email')


from .models import StaffMember

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['name', 'branches', 'image']


from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'price', 'image', 'duration']

from .models import Packages

class PackageForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = ['name', 'price', 'services', 'customer']

