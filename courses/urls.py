from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.CourseView.as_view()),
    path("courses/<course_id>/", views.CourseDetailView.as_view()),
]
