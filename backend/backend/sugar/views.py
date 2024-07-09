from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import generics

from .serializers import СarbohydratesSerializer
from .models import Сarbohydrates



class СarbohydratesAPI(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = СarbohydratesSerializer(Сarbohydrates.objects.filter(user=request.user.id), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = СarbohydratesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"success": True})
        
        return Response(serializer.errors)


