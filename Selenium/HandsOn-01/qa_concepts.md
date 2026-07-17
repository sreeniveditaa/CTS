# Hands-On 1 - QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

### 1. Test Cases for Different Testing Levels

#### Unit Testing
**Description:**
Verify that the `createCourse()` service method correctly creates a new course object when valid data is provided.

**Example Test Case:**
- Input: Course Name = "Java Programming", Course Code = "CS101"
- Expected Result: A course object is created successfully without interacting with the database.

**Testing Type:** Functional Testing

---

#### Integration Testing

**Description:**
Verify that the `POST /api/courses/` endpoint correctly stores course details in the database.

**Example Test Case:**
- Send a POST request with valid course details.
- Verify that the response status is **201 Created**.
- Verify that the course exists in the database.

**Testing Type:** Functional Testing

---

#### System Testing

**Description:**
Verify the complete course creation workflow.

**Example Test Case:**
1. Send a request to create a course.
2. Retrieve all courses.
3. Verify the newly created course appears in the list.

**Testing Type:** Functional Testing

---

#### User Acceptance Testing (UAT)

**Description:**
A college administrator creates a new course using the application.

**Example Test Case:**
- Login as Admin.
- Create a course.
- Verify students can view and enroll in the course.

**Testing Type:** Functional Testing

---

### 2. Functional vs Non-Functional Testing

| Testing Type | Description |
|--------------|-------------|
| Functional Testing | Verifies whether the application performs the required functionality correctly. |
| Non-Functional Testing | Verifies how well the application performs under different conditions. |

### Example of Non-Functional Testing

**Performance Testing**

- Send 100 simultaneous requests to the Course Management API.
- Verify that the response time remains below 2 seconds.
- Ensure the server remains stable without failures.

---

### 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|-------------------|
| Tests functionality without looking at the source code. | Tests internal code, logic, branches, and conditions. |
| Focuses on inputs and outputs. | Focuses on program implementation. |
| Performed mainly by QA Engineers. | Performed mainly by Developers. |

**QA Tester:** Usually performs **Black-Box Testing**

**Developer:** Usually performs **White-Box Testing**

---

### 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create course with valid data | API running | Send valid course details | HTTP 201 Created | | |
| TC002 | Create course with duplicate course code | Existing course code present | Send duplicate code | Appropriate error message | | |
| TC003 | Create course with missing required fields | API running | Leave course name empty | HTTP 400 Bad Request | | |

---

# Task 2 - Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Rejected
The defect is rejected because it is not valid, cannot be reproduced, or is not considered a bug.

### Deferred
The defect is valid but postponed to a future release due to low priority or project constraints.

---

## 6. Severity and Priority Classification

### a) POST /api/courses/ returns 500 Internal Server Error

**Severity:** Critical

**Priority:** P1

**Justification:**
The API is completely unusable for course creation and must be fixed immediately.

---

### b) Course names longer than 150 characters are silently truncated

**Severity:** Medium

**Priority:** P2

**Justification:**
Data integrity is affected, but the application continues to function.

---

### c) Swagger documentation contains a typo

**Severity:** Low

**Priority:** P4

**Justification:**
The functionality is unaffected. Only documentation needs correction.

---

### d) Login occasionally returns 401 for valid credentials

**Severity:** High

**Priority:** P1

**Justification:**
Intermittent login failures impact user experience and indicate system instability.

---

## 7. Sample Defect Report

| Field | Details |
|--------|---------|
| Defect ID | BUG-001 |
| Title | POST /api/courses returns 500 Internal Server Error |
| Environment | Windows 11, Chrome 138, Python 3.12 |
| Build Version | v1.0 |
| Severity | Critical |
| Priority | P1 |
| Steps to Reproduce | 1. Start API 2. Send POST request with valid course data 3. Observe response |
| Expected Result | Course should be created successfully with HTTP 201 |
| Actual Result | API returns HTTP 500 Internal Server Error |
| Attachments | Screenshot of 500 error |

---

## 8. Difference Between Severity and Priority

| Severity | Priority |
|----------|----------|
| Measures the impact of a defect on the system. | Measures how urgently the defect should be fixed. |

### Example

A spelling mistake on the CEO's dashboard.

- **Severity:** Low (system works correctly)
- **Priority:** High (needs immediate correction because it is highly visible)

Another example:

A rarely used reporting feature crashes.

- **Severity:** High (major functionality affected)
- **Priority:** Low (few users are impacted and the fix can wait)

---

# Conclusion

This hands-on covered:
- QA Testing Levels
- Functional and Non-Functional Testing
- Black-Box and White-Box Testing
- Formal Test Case Writing
- Defect Lifecycle
- Severity vs Priority
- Defect Reporting