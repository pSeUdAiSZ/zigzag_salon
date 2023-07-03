from django import forms
from .models import Service,Customer,StaffMember,Branch

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('category', 'name', 'price', 'image', 'duration')
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone_number', 'email', 'profession', 'address')
class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ('name', 'branches', 'image')
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'address', 'phone_number', 'email')