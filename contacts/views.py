from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions

class ContactViewSet(viewsets.ModelViewSet):
    """
    viewset automatically provides list, create, retrieve, update and destroy actions
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Create your views here.
