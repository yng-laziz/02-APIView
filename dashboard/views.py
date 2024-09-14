from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UniversityCreateListApiView(APIView):
    def get(self, request):
        university = UniversityModel.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UniversitySerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UniversityRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return UniversityModel.objects.get(pk=pk)
        except UniversityModel.DoesNotExist:
            return None

    def get(self, request, pk):
        university = self.get_object(pk)
        if university is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)

    def put(self, request, pk):
        university = self.get_object(pk)
        if university is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UniversitySerializer(university, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        university = self.get_object(pk)
        if university is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FacultyCreateListApiView(APIView):
    def get(self, request):
        faculty = FacultyModel.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FacultySerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FacultyRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return FacultyModel.objects.get(pk=pk)
        except FacultyModel.DoesNotExist:
            return None

    def get(self, request, pk):
        faculty = self.get_object(pk)
        if faculty is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    def put(self, request, pk):
        faculty = self.get_object(pk)
        if faculty is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        faculty = self.get_object(pk)
        if faculty is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GroupCreateListApiView(APIView):
    def get(self, request):
        group = GroupModel.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GroupSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GroupRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return GroupModel.objects.get(pk=pk)
        except GroupModel.DoesNotExist:
            return None

    def get(self, request, pk):
        group = self.get_object(pk)
        if group is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk):
        group = self.get_object(pk)
        if group is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        group = self.get_object(pk)
        if group is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    







class TeacherCreateListApiView(APIView):
    def get(self, request):
        teacher = TeacherModel.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return TeacherModel.objects.get(pk=pk)
        except TeacherModel.DoesNotExist:
            return None

    def get(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






class SubjectCreateListApiView(APIView):
    def get(self, request):
        subject = SubjectModel.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SubjectSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return SubjectModel.objects.get(pk=pk)
        except SubjectModel.DoesNotExist:
            return None

    def get(self, request, pk):
        subject = self.get_object(pk)
        if subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk):
        subject = self.get_object(pk)
        if subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subject = self.get_object(pk)
        if subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






class StudentCreateListApiView(APIView):
    def get(self, request):
        student = StudentModel.objects.all()
        serializer = StudentModel(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            return None

    def get(self, request, pk):
        student = self.get_object(pk)
        if student is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        if student is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        if student is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)