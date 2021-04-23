from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
class StudentAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response('Deleted')

    def patch(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
