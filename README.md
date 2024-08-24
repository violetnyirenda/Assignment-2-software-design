# Student Management System

This project is a simple Student Management System developed in Python. The system was refactored to follow SOLID principles and other software design best practices.

## Features

- **Add Student:** Add new students to the database.
- **Delete Student:** Remove students from the database by their ID.
- **Update Student Information:** Update the details of an existing student.
- **View All Students:** Display all students in the database.
- **Interactive Menu:** A user-friendly text-based menu for easy interaction with the system.

## Design Principles

This system was refactored to adhere to the following software design principles:

- **SOLID Principles:**
  - **Single Responsibility Principle (SRP):** Each class has a single responsibility.
  - **Open/Closed Principle (OCP):** The system is open for extension but closed for modification.
  - **Liskov Substitution Principle (LSP):** Derived classes can replace base classes without affecting the program's correctness.
  - **Interface Segregation Principle (ISP):** Interfaces are specific to what the client needs.
  - **Dependency Inversion Principle (DIP):** High-level modules depend on abstractions rather than low-level modules.

- **DRY (Don't Repeat Yourself):** Repeated code has been consolidated to reduce redundancy.
- **KISS (Keep It Simple Stupid):** The code is simplified and easy to understand.
- **YAGNI (You Ain't Gonna Need It):** The system includes only necessary features, avoiding unnecessary complexity.

## How to Run

1. **Clone the repository:**

   git clone https://github.com/yourusername/student-management-system.git

2. **Navigate to the project directory:**
   cd student-management-system

3. **Run the system:**
   python student_management_system.py

4. **Follow the menu prompts:** 
   The system will display a menu with options to add, delete, update, and view students.