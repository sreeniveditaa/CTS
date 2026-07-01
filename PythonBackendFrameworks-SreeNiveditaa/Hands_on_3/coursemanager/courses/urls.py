from rest_framework.routers import DefaultRouter # pyright: ignore[reportMissingImports]
from .views import (
    DepartmentViewSet,
    CourseViewSet,
    StudentViewSet,
    EnrollmentViewSet
)

router = DefaultRouter()

router.register("departments", DepartmentViewSet)
router.register("courses", CourseViewSet)
router.register("students", StudentViewSet)
router.register("enrollments", EnrollmentViewSet)

urlpatterns = router.urls