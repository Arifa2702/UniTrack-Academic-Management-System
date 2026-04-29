from django.shortcuts import render, redirect
from .forms import StudentForm, ResultForm, CourseForm, AttendanceForm
from .models import Student, Result, Course, Attendance


def home(request):
    return render(request, 'home.html')


def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'add_student.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
from .forms import ResultForm
from .models import Result


def add_result(request):
    form = ResultForm()

    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result_list')

    return render(request, 'add_result.html', {'form': form})


def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_list.html', {'results': results})
def calculate_gpa(request, student_id):
    results = Result.objects.filter(student_id=student_id)

    total_points = 0
    total_courses = results.count()

    grade_map = {
        'A+': 4.00,
        'A': 3.75,
        'A-': 3.50,
        'B+': 3.25,
        'B': 3.00,
        'B-': 2.75,
        'C+': 2.50,
        'C': 2.25,
        'D': 2.00,
        'F': 0.00
    }

    for result in results:
        total_points += grade_map.get(result.grade, 0)

    gpa = total_points / total_courses if total_courses > 0 else 0

    return render(request, 'gpa.html', {
        'gpa': round(gpa, 2)
    })

def search_student(request):
    query = request.GET.get('q')
    students = Student.objects.filter(name__icontains=query)

    return render(request, 'student_list.html', {
        'students': students
    })
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'edit_student.html', {'form': form})
def add_course(request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')

    return render(request, 'add_course.html', {'form': form})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})
def add_attendance(request):
    form = AttendanceForm()

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    return render(request, 'add_attendance.html', {'form': form})


def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance_list.html', {
        'attendance_records': attendance_records
    })