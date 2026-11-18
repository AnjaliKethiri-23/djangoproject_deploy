from django.contrib import admin

# Register your models here.
from hr_department.models import emp_table

class emp_admin(admin.ModelAdmin):
    list_display = ['eid', 'emp_name', 'emp_salary']
    ordering = ['eid']
    list_filter = ['emp_salary']
    search_fields = ['eid', 'emp_name']
admin.site.register(emp_table, emp_admin)
    