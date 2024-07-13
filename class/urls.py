from . import views 
from django.urls import path
from . views import Home

app_name = 'class'

urlpatterns = [
    path('',views.Home,name = 'home'),
    path('login/',views.Login,name='login'),
    path('signup',views.signup,name='signup'),
    path('signup/student_signup/',views.StudentSignUp,name="StudentSignUp"),
    path('signup/teacher_signup/',views.TeacherSignUp,name="TeacherSignUp"),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name="student_detail"),
    path('teacher/<int:pk>/',views.TeacherDetailView.as_view(),name="teacher_detail"),
    path('update/student/<int:pk>/',views.StudentUpdateView,name="student_update"),
    path('update/teacher/<int:pk>/',views.TeacherUpdateView,name="teacher_update"),
]
