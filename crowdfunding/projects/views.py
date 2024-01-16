

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
from .models import Project, Pledge
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer
from django.http import Http404


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
         serializer.save(owner=request.user)
         return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
         

class ProjectDetail(APIView):
    permission_classes = [
       permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly
    ]


    def get_object(self, pk):
       try:
          project = Project.objects.get(pk=pk)
          self.check_object_permissions(self.request, project)
          return project
       except Project.DoesNotExist:
          raise Http404
       
    def get(self, request, pk):
       project = self.get_object(pk)
       serializer = ProjectDetailSerializer(project)
       return Response (serializer.data) 

    def put(self, request, pk):
       project = self.get_object(pk)
       serializer = ProjectDetailSerializer(
          instance=project, 
          data=request.data,
          partial=True) 
       if serializer.is_valid():
          serializer.save()
            