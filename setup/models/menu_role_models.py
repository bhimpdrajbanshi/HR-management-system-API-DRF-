from django.db import models
from setup.models import BaseModel
from setup.models import Role

class MenuRole(BaseModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    menu = models.CharField(max_length=200)
   
    is_view = models.BooleanField(default=False)
    is_add = models.BooleanField(default=False)
    is_edit = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = "menu_role"