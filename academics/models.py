from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    credit = models.FloatField()

    def __str__(self):
        return self.course_name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.FloatField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    date = models.DateField()   
    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent')
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.date}"