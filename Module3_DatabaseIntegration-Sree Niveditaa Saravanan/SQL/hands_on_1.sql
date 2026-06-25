-- ==========================================================
-- Hands-On 1
-- Task 1: Create Database Tables
-- Name: Sree Niveditaa
-- ==========================================================

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    FOREIGN KEY (student_id)
        REFERENCES students(student_id),
    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);

CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- ==========================================================
-- Task 2: Verify Normalization
-- ==========================================================

-- 1NF:
-- All columns store atomic (single) values.
-- Example violation: Storing multiple phone numbers in one column
-- such as '9876543210,9123456789' would violate 1NF.

-- 2NF:
-- All non-key attributes are fully dependent on the primary key.
-- In the enrollments table, student_id and course_id identify
-- each enrollment, and enrollment_date and grade depend on
-- that enrollment only.

-- 3NF:
-- There are no transitive dependencies.
-- Department details are stored only in the departments table.
-- Students store only department_id, avoiding duplicate
-- department information and maintaining 3NF.

-- Conclusion:
-- The schema satisfies 1NF, 2NF, and 3NF.

-- ==========================================================
-- Task 3: ALTER TABLE
-- ==========================================================

-- Add phone_number column
ALTER TABLE students
ADD phone_number VARCHAR(15);

-- Add max_seats column
ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

-- Add CHECK constraint
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

-- Rename hod_name column
ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

-- Drop phone_number column
ALTER TABLE students
DROP COLUMN phone_number;