from rest_framework import viewsets, permissions
from .models import Project, Task
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer, RegisterSerializer

# This view is for the /api/auth/me endpoint
class UserDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return projects belonging to the current user
        return self.request.user.projects.all()

    def perform_create(self, serializer):
        # Automatically assign the current user to the project
        serializer.save(user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return tasks belonging to the current user
        queryset = self.request.user.tasks.all()
        
        # Filter by project if projectId is in the URL
        project_id = self.kwargs.get('project_pk')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
            
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,) # Allow anyone to register
    serializer_class = RegisterSerializer