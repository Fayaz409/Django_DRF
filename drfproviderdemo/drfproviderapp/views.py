from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from rest_framework import mixins,generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET','POST'])
def employee_list(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many = True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def employee_detail(request,pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # employee = Employee.objects.get(id=pk)
        serializer= EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeList(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get(self,request,pk):
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        try:
            employee = Employee.objects.get(id = pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 



class EmployeesList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

class EmployeesDetail(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self, request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)


class EmployeeLists(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCustomPagination(PageNumberPagination):
    page_size = 3

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]

    # pagination_class = EmployeeCustomPagination
    filterset_fields = ['first_name','last_name','salary']
    # filter_backends  = [filters.SearchFilter]
    search_fields = ['^first_name','^last_name']
    # search_fields = ['first_name','last_name','salary']
    # search_fields = ['=first_name','=last_name'],
