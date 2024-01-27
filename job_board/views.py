from django.shortcuts import render

# Rest FrameWork
from rest_framework.response import Response
from rest_framework import viewsets

# Model and Serializer
from .models import JobBoard
from .serializers import JobBoardSerializer

# Filter and Pagination
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

# Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Paginate(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


class JobViewSet(viewsets.ModelViewSet):
    queryset = JobBoard.objects.all()
    serializer_class = JobBoardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["location", "job_title"]
    pagination_class = Paginate
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
