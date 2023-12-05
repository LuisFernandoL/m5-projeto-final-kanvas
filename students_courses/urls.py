from django.urls import path
from . import views

urlpatterns = [
    path("courses/<course_id>/students/", views.StudentsInCourseDetailView.as_view()),
]
