from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(UniversityModel)
class UniversityAdmin(admin.ModelAdmin):
    model = UniversityModel
    fields = ['name']

@admin.register(FacultyModel)
class FacultyAdmin(admin.ModelAdmin):
    model = FacultyModel
    fields = ['name', 'university']

@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    model = GroupModel
    fields = ['name', 'faculty']

@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    model = TeacherModel
    fields = ['first_name', 'last_name', 'group']

@admin.register(SubjectModel)
class SubjectAdmin(admin.ModelAdmin):
    model = SubjectModel
    fields = ['name', 'teacher']

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    model = StudentModel
    fields = ['first_name', 'last_name', 'subject']