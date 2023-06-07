from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Student
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET'])
def getData(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)