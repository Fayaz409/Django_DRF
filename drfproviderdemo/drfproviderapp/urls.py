from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api/viewset-employees',EmployeeViewSet)
router.register('api/viewset-departments',DepartmentViewset)
router.register('api/viewset-countries',CountryViewset)

# urlpatterns = [
# ]

urlpatterns = [
    path('',include(router.urls)),
   path('api/fbv-employees/',employee_list,name='employees-list'),
   path('api/fbv-employees/<int:pk>',employee_detail,name='employee-detail'),
   path('api/employee-list/',EmployeeList.as_view()),
   path('api/employee-list/<int:pk>',EmployeeDetail.as_view()),
   path('api/employees-list/',EmployeesList.as_view()),
   path('api/employees-list/<int:pk>',EmployeesDetail.as_view()),
   path('api/employees-lists/',EmployeeLists.as_view()),
   path('api/employees-lists/<int:pk>',EmployeeDetails.as_view()),
   # path('/api/all-emplyees/<int:pk>',EmployeeViewSet.as_view()),
   

]