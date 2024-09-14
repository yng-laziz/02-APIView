from rest_framework import serializers
from .models import *

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyModel
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'
    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
    