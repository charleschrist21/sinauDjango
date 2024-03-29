from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from ..models import Courses
from ..serializers import CoursesSerializer

# class CoursesViewSet(viewsets.ModelViewSet):
    
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializer

class CoursesViewSetSearch(viewsets.ModelViewSet):

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    search_fields = ('title',)
    filter_fields = ('title',) 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
