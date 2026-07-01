-- ===========================
-- Task 3: Alter and Extend the Schema
-- ===========================

-- 10. Add phone_number column to students table
ALTER TABLE students
ADD phone_number VARCHAR(15);

-- 11. Add max_seats column to courses table
ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

-- 12. Add CHECK constraint for grade
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL);

-- 13. Rename hod_name to head_of_dept
ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

-- 14. Drop phone_number column
ALTER TABLE students
DROP COLUMN phone_number;

-- Verify the changes
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
