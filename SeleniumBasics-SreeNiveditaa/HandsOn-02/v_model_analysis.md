# Hands-On 2 - SDLC vs TDLC, V-Model & Agile QA Integration

## Task 1: V-Model Mapping

### 1. V-Model Diagram

```
                    SDLC (Development)

        Requirements
             |
             |
        System Design
             |
             |
     Architecture Design
             |
             |
        Module Design
             |
             |
            Coding
             |
             |
-----------------------------------------------
             |
             |
        Unit Testing
             |
             |
    Integration Testing
             |
             |
       System Testing
             |
             |
    Acceptance Testing

                  TDLC (Testing)
```

### SDLC ↔ TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements Analysis | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Execution of all tests | Executable Application |

---

## 2. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**
- Module is completely developed.
- Code review completed.
- Unit test cases prepared.

**Exit Criteria**
- All unit tests executed.
- No critical defects remain.
- Code coverage meets project standards.

---

### Integration Testing

**Entry Criteria**
- Unit testing completed successfully.
- Modules integrated.

**Exit Criteria**
- All interfaces verified.
- Integration defects resolved.

---

### System Testing

**Entry Criteria**
- Entire application integrated.
- Test environment ready.
- System test cases prepared.

**Exit Criteria**
- All system test cases executed.
- No Critical or High severity defects.
- Test summary report completed.

---

### Acceptance Testing

**Entry Criteria**
- System testing completed.
- Client receives release candidate.

**Exit Criteria**
- Customer approves the application.
- Business requirements satisfied.
- Product ready for deployment.

---

## 3. QA Engagement During Development

QA should participate before testing begins.

### During Requirements Analysis

- Review requirements for clarity.
- Identify missing or ambiguous requirements.
- Prepare acceptance criteria.
- Suggest test scenarios.

### During System Design

- Review design documents.
- Prepare test strategy.
- Identify integration risks.
- Plan automation approach.

---

# Task 2 - Agile QA & Shift-Left Testing

## 4. Problems with Waterfall Testing

### Problem 1
Defects are discovered very late, making them expensive to fix.

### Problem 2
Developers may need to rewrite large portions of code if requirements were misunderstood.

### Problem 3
Testing takes place only after development is complete, delaying product release.

---

## 5. QA Role in Agile Ceremonies

### Sprint Planning

- Review user stories.
- Define acceptance criteria.
- Estimate testing effort.
- Identify automation opportunities.

---

### Daily Stand-up

- Share testing progress.
- Report blockers.
- Coordinate with developers.
- Update defect status.

---

### Sprint Review

- Validate completed features.
- Demonstrate tested functionality.
- Verify acceptance criteria.

---

### Sprint Retrospective

- Discuss lessons learned.
- Suggest process improvements.
- Improve automation coverage.
- Reduce recurring defects.

---

## 6. Shift-Left Testing Practices

### a) Requirement Review

QA reviews requirements before development begins to ensure they are clear, complete, and testable.

---

### b) Writing Test Cases Before Code

Prepare test cases or BDD scenarios before development starts so developers understand expected behavior.

---

### c) Static Code Analysis

Use tools to detect coding issues, security vulnerabilities, and code quality problems before execution.

---

### d) API Contract Testing

Validate API request and response formats before integrating frontend and backend components.

---

## 7. Acceptance Criteria (Given-When-Then)

### Scenario 1 - Successful Course Creation

**Given**
The college administrator is logged in.

**When**
The administrator enters valid course details and clicks Create.

**Then**
The course is created successfully and a confirmation message is displayed.

---

### Scenario 2 - Duplicate Course Code

**Given**
A course with the same course code already exists.

**When**
The administrator attempts to create another course with the same code.

**Then**
The system displays an error message stating that the course code already exists.

---

### Scenario 3 - Missing Required Fields

**Given**
The administrator opens the Create Course page.

**When**
Required fields such as Course Name or Course Code are left empty and the form is submitted.

**Then**
The system displays validation errors and does not create the course.

---

# Conclusion

This hands-on covered:

- SDLC Phases
- TDLC Phases
- V-Model Mapping
- Entry & Exit Criteria
- Agile QA Integration
- Shift-Left Testing
- Gherkin Acceptance Criteria