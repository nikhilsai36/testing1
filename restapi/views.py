from.models import Student, Group
from .serializers import StudentSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def details(request):
    grp = Group.objects.all()
    serializer = GroupSerializer(grp, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
def update(request, id):
    grp = Group.objects.get(id=id)
    serializer = GroupSerializer(instance=grp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def dele(request, id):
    grp = Group.objects.get(id=id)
    grp.delete()
    return Response('Deleted')









@api_view(['GET'])
def studetails(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def stucreate(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
def stuupdate(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def studelete(request, id):
    event = Student.objects.get(id=id)
    event.delete()
    return Response('Deleted')
