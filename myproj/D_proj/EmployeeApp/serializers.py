from rest_framework import serializers
from EmployeeApp.models import Departments,Employee

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmenId',
                'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
          model = Employee
          fields = ('EmployeeId',
                    'EmployeeName',
                    'Department',
                    'DateOfJoining',
                    'PhotoFileName')  
