from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import  Departments,Employee
from EmployeeApp.serializers import DepartmentsSerializer,EmployeeSerializer

# Create your views here.
@csrf_exempt
def deppartmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentsSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)

    elif request.method=='POST':
         department_data = JSONParser().parse(request)
         departments_serializer = DepartmentsSerializer(data=department_data)
         if departments_serializer.is_valid():
             departments_serializer.save()
             return JsonResponse("Added successfully!!",safe=False)
         return JsonResponse("Failerd to add.",safe=False)

    elif request.method =='PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentsSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated successfully.!!",safe=False)
        return JsonResponse("Failed to update.",safe=False)

    elif request.method=='DELETE':
         department=Departments.objects.get(DepartmentId=id)
         department.delete()
         return JsonResponse('Deleted successfully!!', safe=False)
