from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Content


class IsAdmOrReadyOnlyContent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Content):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
            or request.user.is_superuser
        )
