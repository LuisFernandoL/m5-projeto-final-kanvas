from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Course


class IsAdmOrReadyOnly(permissions.BasePermission):
    def has_permission(
        self,
        req: Request,
        view: View,
    ):
        if req.method in permissions.SAFE_METHODS:
            return True
        return req.user.is_authenticated and req.user.is_superuser

    def has_object_permission(self, request, view, obj: Course):
        return request.user in obj.students.all() or request.user.is_superuser
