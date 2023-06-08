from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, FileUploadSerializer
from django.shortcuts import render
from rest_framework import generics, status
import io, csv, pandas as pd
from rest_framework.response import Response
from base.models import Student, Bootcamp
import math
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)

        for _, row in reader.iterrows():
            for key, value in row.items():
                if value == '-' or math.isnan(value):
                    row[key] = 0
            
            bootcamp_id = row['Bootcamp_id']
            bootcamp, _ = Bootcamp.objects.get_or_create(bootcamp_id=bootcamp_id)

            
            new_file = Student(
                student_id = row['Student_id'],
                tableau = row['Tableau'],
                sql = row['SQL'],
                r = row['R'],
                python = row['Python'],
                big_data = row['Big Data'],
                spss = row['SPSS'],
                data_cleaning =row['Data Cleaning'],
                data_visualization =row['Data Visualization'],
                modeling=row['Modeling'],
                programming=row['Programming'],
                technical_average=row['Technical Average'],
                communication=row['Communication'],
                problem_solving=row['Problem Solving'],
                critical_thinking=row['Critical Thinking'],
                leadership=row['Leadership'],
                soft_average=row['Soft Average'],
                bootcamp=bootcamp,
                )
            new_file.save()

        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

@api_view(['GET'])
def getBootcampData(request, bootcamp_id):
    try:
        students = Student.objects.filter(bootcamp_id=bootcamp_id)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({'error': 'No students found for the specified bootcamp'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getStudentData(request, student_id):
    try:
        student = Student.objects.get(student_id=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def student_details(request):
    student_id = request.GET.get('student_id')
    try:
        student = Student.objects.get(student_id=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def base(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data, many=True)
    context = {
        'data': serializer.data
    }
    return render(request, 'getData.html', context)

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