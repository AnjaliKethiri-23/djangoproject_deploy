from django import forms 
from hr_department.models import emp_table

class employee_form(forms.ModelForm):
    class Meta:
        fields = '__all__'          # ['eid', 'emp_name', 'emp_salary']
        model = emp_table
        
        