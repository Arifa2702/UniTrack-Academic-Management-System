from django.urls import path
from .views import home, add_student, student_list, add_result, result_list, calculate_gpa, search_student, delete_student,edit_student,add_course, course_list,add_attendance, attendance_list



urlpatterns = [
    path('', home, name='home'),
    path('add-student/', add_student, name='add_student'),
    path('students/', student_list, name='student_list'),
    path('add-result/', add_result, name='add_result'),
    path('results/', result_list, name='result_list'),
    path('gpa/<int:student_id>/', calculate_gpa, name='calculate_gpa'),
    path('search/', search_student, name='search_student'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student'),
    path('edit-student/<int:student_id>/', edit_student, name='edit_student'),
    path('add-course/', add_course, name='add_course'),
    path('courses/', course_list, name='course_list'),
    path('add-attendance/', add_attendance, name='add_attendance'),
    path('attendance/', attendance_list, name='attendance_list'),
      
]