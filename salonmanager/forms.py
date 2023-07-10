from django import forms
from .models import Customer, FamilyMember

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


from django import forms
from .models import Packages, ServiceUsage, Service
from django.forms import inlineformset_factory

class PackageForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Packages
        fields = ('name', 'price', 'validity', 'services')

class ServiceUsageForm(forms.ModelForm):
    class Meta:
        model = ServiceUsage
        fields = ('service', 'usage_count')

ServiceUsageFormSet = inlineformset_factory(
    Packages,
    ServiceUsage,
    form=forms.ModelForm,
    fields=('service', 'usage_count'),
    extra=1,
)

from .models import FamilyMember, Membership
class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ['customer','name', 'age', 'number']

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['customer', 'package', 'family_members', 'start_date', 'end_date']