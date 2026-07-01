-- ===========================
-- Task 2: Verify Normalisation
-- ===========================

-- 1NF:
-- All tables contain atomic (single) values in each column.
-- There are no repeating groups or multiple values stored in a single field.
-- Example violation: Storing multiple phone numbers in one column (9876543210,9123456789).

-- 2NF:
-- Every table uses a primary key, and all non-key attributes depend on the whole primary key.
-- In the enrollments table, student_id and course_id together uniquely identify an enrollment.
-- enrollment_date and grade depend on the complete enrollment record, not just one key.

-- 3NF:
-- There are no transitive dependencies in the schema.
-- Department details such as dept_name are stored only in the departments table.
-- The students table stores only department_id as a foreign key.
-- This avoids data redundancy and maintains database consistency.

-- 3NF Analysis for Enrollments:
-- The enrollments table contains only enrollment-specific information.
-- grade and enrollment_date depend directly on the enrollment record.
-- No non-key attribute depends on another non-key attribute.
-- Therefore, the enrollments table satisfies Third Normal Form (3NF).
