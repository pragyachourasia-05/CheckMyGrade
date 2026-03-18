# CheckMyGrade Application
**DATA 200 - Lab 1 | San Jose State University**  
**Student:** Pragya Chourasia  
**Professor:** Paramdeep Saini

---

## Overview
CheckMyGrade is a console-based Python application for managing and evaluating student grades using Object-Oriented Programming. Data is stored using CSV files (array-style approach).

---

## Project Structure
```
CheckMyGrade/
├── main.py               # Main application entry point
├── student.py            # Student class
├── professor.py          # Professor class
├── course.py             # Course class
├── grades.py             # Grades class
├── login_user.py         # LoginUser class
├── security.py           # TextSecurity (Caesar cipher encryption)
├── csv_manager.py        # All CSV read/write operations
├── test_checkmygrade.py  # Unit tests
├── students.csv          # Student records
├── professors.csv        # Professor records
├── courses.csv           # Course records
└── login.csv             # Login credentials (encrypted passwords)
```

---

## Features
- Add, delete, modify, and search student/professor/course records
- Sort students by marks or email (ascending & descending)
- Calculate average and median marks per course
- Generate reports by course, student, or professor
- Login system with Caesar cipher password encryption
- Unit tested with 1000 student records

---

## How to Run

**Run the application:**
```bash
python main.py
```

**Run unit tests:**
```bash
python test_checkmygrade.py
```

---

## Unit Test Results
| Test | Result | Time |
|------|--------|------|
| Add 1000 students | PASS | - |
| Search (1000 records) | PASS | 0.00274s |
| Sort by marks | PASS | 0.00522s |
| Sort by email | PASS | 0.00453s |
| Student modify/delete | PASS | - |
| Course CRUD | PASS | - |
| Professor CRUD | PASS | - |

**Total: 9 tests passed in 21.695s**

---

## Requirements
- Python 3.x
- No external libraries required (uses built-in `csv`, `os`, `unittest`)
