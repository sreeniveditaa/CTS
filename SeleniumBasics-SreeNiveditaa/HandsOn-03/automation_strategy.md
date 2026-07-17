# Hands-On 3 - Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

### 1. Criteria for Deciding Whether to Automate a Test Case

#### Criterion 1: Repetitive Execution
Tests that are executed frequently, such as regression tests, should be automated.

**Application:**
The POST `/api/courses/` endpoint is tested after every code change, making it an ideal automation candidate.

---

#### Criterion 2: Stable Functionality

Features that do not change frequently are good candidates for automation.

**Application:**
The course creation API has stable functionality and can be automated.

---

#### Criterion 3: High Business Impact

Critical business functionalities should always be automated.

**Application:**
Creating courses is one of the core features of the Course Management System.

---

#### Criterion 4: Data-Driven Testing

Tests requiring multiple input combinations are easier and faster through automation.

**Application:**
The POST endpoint can be tested with valid, invalid, empty, and duplicate course data.

---

#### Criterion 5: Regression Testing

Regression tests are repeated many times during development.

**Application:**
Every application update requires verifying that course creation still works correctly.

---

## 2. Manual vs Automated Testing Decisions

| Test Case | Decision | Justification |
|-----------|----------|---------------|
| Regression test for all CRUD endpoints | Automate | Executed frequently after every build |
| Exploratory testing of a new search feature | Manual | Requires human creativity and observation |
| Performance test with 100 concurrent users | Automate | Requires automated load generation tools |
| UI test for login form | Automate | Repeated often and follows fixed steps |
| Verify Swagger API documentation | Manual | Involves reviewing documentation quality |
| Smoke test after deployment | Automate | Fast verification before release |

---

## 3. Test Automation ROI

### Definition

Return on Investment (ROI) measures whether the time and effort spent developing automation are recovered through reduced manual testing effort.

---

### Calculation

Automation Development Time = **4 hours**

Manual Execution Time = **30 minutes (0.5 hours)**

Break-even Point

```
4 ÷ 0.5 = 8 executions
```

Therefore,

**Automation starts saving time after the 8th execution.**

---

### Maintenance Overhead

After the 10th execution, each automated run requires:

20% × 30 minutes = **6 minutes**

Effective execution time:

30 + 6 = **36 minutes**

Even with maintenance, automation remains significantly faster than repeatedly performing manual regression testing.

---

## 4. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes to the application.

### Example

A Selenium script attempts to click a button before it has fully loaded, causing intermittent failures.

### How to Prevent Flaky Tests

1. Use Explicit Waits instead of `time.sleep()`.
2. Use reliable locators such as ID or CSS selectors.
3. Keep test data independent and ensure proper environment setup.

---

# Task 2 - Automation Framework Types

## 5. Framework Comparison

| Framework | Description | Advantage | Disadvantage | Example Use |
|------------|-------------|-----------|--------------|-------------|
| Linear | Test scripts are executed sequentially. | Easy to learn | Difficult to maintain | Small prototype project |
| Modular | Application divided into reusable modules. | High code reuse | Initial setup takes time | Login module reused across Course Management tests |
| Data-Driven | Test data stored externally (Excel, CSV, JSON). | Easy to test multiple inputs | Data management required | Testing course creation with many input combinations |
| Keyword-Driven | Keywords define test actions. | Non-programmers can contribute | Complex framework development | Business users defining high-level test steps |
| Hybrid | Combines Modular, Data-Driven, and Keyword-Driven approaches. | Highly reusable and scalable | More complex to develop | Large enterprise Selenium projects |

---

## 6. Recommended Framework

### Recommendation

**Hybrid Framework**

### Justification

The team needs to:

- Test login using 50 different username/password combinations.
- Reuse login functionality across multiple test cases.
- Support both technical and non-technical team members.

A Hybrid framework combines:

- Modular Framework for reusable page components.
- Data-Driven Framework for multiple login credentials.
- Keyword-Driven Framework for readable test cases.

This combination provides excellent scalability, maintainability, and flexibility.

---

## 7. Hybrid Framework Folder Structure

```
CourseManagementAutomation/

│
├── config/
│      config.py
│
├── test_data/
│      login_data.csv
│      course_data.xlsx
│
├── pages/
│      login_page.py
│      course_page.py
│
├── tests/
│      test_login.py
│      test_course.py
│
├── utilities/
│      browser.py
│      logger.py
│      screenshots.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
│
└── pytest.ini
```

### Folder Description

**config/**
- Stores application configuration such as URLs and browser settings.

**test_data/**
- Contains CSV, Excel, or JSON files used for Data-Driven Testing.

**pages/**
- Implements the Page Object Model (POM).
- Contains locators and reusable page methods.

**tests/**
- Stores all test scripts.

**utilities/**
- Contains helper classes such as browser initialization, logging, waits, and screenshots.

**reports/**
- Stores HTML execution reports.

**screenshots/**
- Stores screenshots captured during failures.

---

# Conclusion

This hands-on covered:

- Automation Decision Criteria
- Manual vs Automated Test Selection
- Test Automation ROI
- Flaky Tests
- Automation Framework Types
- Hybrid Framework Recommendation
- Selenium Automation Project Structure