from django.urls import path
from . import views
from .views import *

urlpatterns = [
    
    path("api/menu-roles/list/", MenuRoleListView.as_view(), name="menu_role_list"),
    path("api/menu-roles/create/", MenuRoleCreateView.as_view(), name="menu_role_create"),
    
    path("api/departments/", DepartmentListView.as_view(), name="department_list"),
    path("api/roles/list/", RoleListView.as_view(), name="role_list"),
    path("api/roles/create/", RoleCreateView.as_view(), name="role_create"),
   
]
