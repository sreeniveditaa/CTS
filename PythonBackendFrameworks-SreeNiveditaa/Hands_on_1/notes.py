"""
=========================================================
HANDS-ON 01
Task 1: Web Framework Foundations
=========================================================
"""

# =========================================================
# 1. Request-Response Cycle
# =========================================================

"""
Request Flow:

Browser
   |
   |  GET /api/courses/
   v
URL Router (urls.py)
   |
   v
View (views.py)
   |
   v
Model (models.py)
   |
   v
Database Query
   |
   v
Model returns data
   |
   v
View prepares response
   |
   v
HttpResponse / JsonResponse
   |
   v
Browser displays response
"""

# =========================================================
# 2. Middleware
# =========================================================

"""
Middleware sits between the incoming request and the view,
and also between the view and the outgoing response.

Request
    ↓
Middleware
    ↓
View
    ↓
Middleware
    ↓
Response

Examples of built-in middleware:

1. SecurityMiddleware
   - Adds security-related HTTP headers.
   - Helps protect against common attacks.

2. SessionMiddleware
   - Enables session management.
   - Stores and retrieves user session data.
"""

# =========================================================
# 3. WSGI vs ASGI
# =========================================================

"""
WSGI (Web Server Gateway Interface)

• Supports synchronous applications.
• Handles one request at a time.
• Suitable for traditional Django applications.

ASGI (Asynchronous Server Gateway Interface)

• Supports asynchronous programming.
• Handles multiple requests concurrently.
• Supports WebSockets and real-time applications.

By default, Django uses WSGI.

Use ASGI when:
- Building chat applications
- Live notifications
- WebSockets
- Real-time dashboards
"""

# =========================================================
# 4. MVC vs MVT
# =========================================================

"""
MVC

Model
View
Controller

MVT (Django)

Model     -> Model
View      -> Template
Controller -> Django View

Mapping:

MVC Model       = Django Model

MVC View        = Django Template

MVC Controller  = Django View

Django follows the MVT architecture.
"""