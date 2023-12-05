from .models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmOrReadyOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrReadyOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return self.queryset.all()


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrReadyOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"
