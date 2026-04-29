# UniTrack Academic Management System

UniTrack is a Django-based Academic Management System designed to manage student records, courses, results, GPA calculation, and attendance efficiently.

## Features

- Student Management (Add, Edit, Delete, Search)
- Course Management
- Result Management
- GPA Calculation
- Attendance Tracking
- Admin Panel Access
- User-friendly Dashboard Interface

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap

## Project Modules

### Student Module
Manage student information including name, ID, department, and email.

### Course Module
Manage course details such as course name, code, and credit.

### Result Module
Store and manage student results and grades.

### GPA Calculation Module
Calculate GPA based on student grades.

### Attendance Module
Track and manage student attendance records.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Arifa2702/UniTrack-Academic-Management-System.git
```

2. Navigate to project directory:

```bash
cd UniTrack-Academic-Management-System
```

3. Create virtual environment:

```bash
python -m venv venv
```

4. Activate virtual environment:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install django
```

6. Run migrations:

```bash
python manage.py migrate
```

7. Start server:

```bash
python manage.py runserver
```

## Future Improvements

- Authentication System
- Export Reports as PDF
- Notification System
- Advanced Analytics Dashboard

## Author

Arifa Akter Shorna
