from django.urls import path
from . import views
from api.views import UploadFileView, base

urlpatterns = [
    path('', base, name='get_student'),
    path('index/', base, name='get_student'),
    path('all-students/', views.getData),
    path('student-details/', views.student_details, name='student_details'),  
    path('student-data/<int:student_id>/', views.getStudentData, name='student_data'),
    path('upload-csv/', UploadFileView.as_view(), name='upload-file'),
    path('add-student/', views.addStudent),
    path('bootcamp-data/<int:bootcamp_id>/', views.getBootcampData, name='bootcamp_data'),
]
