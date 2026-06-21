from django.urls import path
from . import views
from .views import *

urlpatterns = [

    # path("department/list/", views.department_list, name="department_list" ),
    
    # path("role/", views.role, name="role" ),
    # path("role/create/", views.role_create, name="role_create" ),
    # path("role/list/", views.role_list, name="role_list" ),
    
    # path("departments/", DepartmentListView.as_view(), name="department_list"),
    # path("roles/", RoleListView.as_view(), name="role_list"),
    # path("roles/create/", RoleCreateView.as_view(), name="role_create"),
    
    path("api/departments/", DepartmentListView.as_view(), name="department_list"),
    path("api/roles/", RoleListView.as_view(), name="role_list"),
    path("api/roles/create/", RoleCreateView.as_view(), name="role_create"),
]