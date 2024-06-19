from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Paragraph
from .serializers import ParagraphSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ParagraphCreateView(generics.CreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]

class ParagraphSearchView(generics.ListAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        word = self.request.query_params.get('word', '').lower()
        if word:
            return Paragraph.objects.filter(words__icontains=word)
        else:
            return Paragraph.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
