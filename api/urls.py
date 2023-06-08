from django.urls import path
from . import views
from api.views import UploadFileView, base

urlpatterns = [
    path('', base, name='get_student'),
    path('index/', base, name='get_student'),
    path('all-students/', views.getData),
    path('student-details/', views.student_details, name='student_details'),  # Add this line
    path('upload-csv/', UploadFileView.as_view(), name='upload-file'),
    path('add-student/', views.addStudent)
]