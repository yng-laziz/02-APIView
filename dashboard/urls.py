from django.urls import path
from .views import *
urlpatterns = [
    path('university/', UniversityCreateListApiView.as_view()),
    path('university/<int:pk>', UniversityRetrieveUpdateDestroyAPIView.as_view()),
    path('faculty/', FacultyCreateListApiView.as_view()),
    path('faculty/<int:pk>', FacultyRetrieveUpdateDestroyAPIView.as_view()),
    path('group/', GroupCreateListApiView.as_view()),
    path('group/<int:pk>', GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('teacher/', TeacherCreateListApiView.as_view()),
    path('teacher/<int:pk>', TeacherRetrieveUpdateDestroyAPIView.as_view()),
    path('subject/', SubjectCreateListApiView.as_view()),
    path('subject/<int:pk>', SubjectRetrieveUpdateDestroyAPIView.as_view()),
    path('student/', StudentCreateListApiView.as_view()),
    path('student/<int:pk>', StudentRetrieveUpdateDestroyAPIView.as_view()),
]
