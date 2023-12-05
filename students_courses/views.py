from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from courses.models import Course
from rest_framework.generics import RetrieveUpdateAPIView
from courses.permissions import IsAdmOrReadyOnly
from .serializers import CourseStudentSerializer
from rest_framework.views import Response



class StudentsInCourseDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrReadyOnly]

    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"

