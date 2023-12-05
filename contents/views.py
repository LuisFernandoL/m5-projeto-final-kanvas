from .models import Content
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ContentSerializer
from rest_framework.permissions import IsAuthenticated
from courses.permissions import IsAdmOrReadyOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound
from courses.models import Course
from .permissions import IsAdmOrReadyOnlyContent


class ContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrReadyOnly]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})
        serializer.save(course=course)


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrReadyOnlyContent]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_object(self) -> Content:
        content = Content.objects.filter(pk=self.kwargs["content_id"]).first()
        course = Course.objects.filter(pk=self.kwargs["course_id"]).exists()
        if not content:
            raise NotFound({"detail": "content not found."})
        if not course:
            raise NotFound({"detail": "course not found."})
        self.check_object_permissions(self.request, content)
        return content
