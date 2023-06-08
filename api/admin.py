from django.contrib import admin
from base.models import Student, Bootcamp

# Register your models here.

# this will show which models to display in admin panel from Student database
class FileAdmin(admin.ModelAdmin):
    list_display = ["student_id","tableau","sql","r","python","big_data","spss", "data_cleaning", "data_visualization","modeling","programming", "technical_average","communication","problem_solving","critical_thinking", "leadership","soft_average", "bootcamp"]
admin.site.register(Student, FileAdmin)

class StudentInline(admin.TabularInline):
    model = Student
    extra = 0

class BootcampAdmin(admin.ModelAdmin):
    list_display = ["bootcamp_id"]
    inlines = [StudentInline]

admin.site.register(Bootcamp, BootcampAdmin)