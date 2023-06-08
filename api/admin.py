from django.contrib import admin
from base.models import Student

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ["student_id","tableau","sql","r","python","big_data","spss", "data_cleaning", "data_visualization","modeling","programming", "technical_average","communication","problem_solving","critical_thinking", "leadership","soft_average","bootcamp_id"]
admin.site.register(Student, FileAdmin)