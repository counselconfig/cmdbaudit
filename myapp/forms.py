from django import forms
from myapp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "Reference_No",
            "Serial_No",
            "CMDB_item_type",
            "User_name",
            "Email_address",
            "Organisation",
        ]
        widgets = {
            "Reference_No": forms.TextInput(attrs={"class": "form-control"}),
            "Serial_No": forms.TextInput(attrs={"class": "form-control"}),
            "CMDB_item_type": forms.TextInput(attrs={"class": "form-control"}),
            "User_name": forms.TextInput(attrs={"class": "form-control"}),
            "Email_address": forms.EmailInput(attrs={"class": "form-control"}),
            "Organisation": forms.TextInput(attrs={"class": "form-control"}),
        }
