from setup.models import Role, MenuRole
from setup.validation.global_validation import validate_bool

def validate_menu_role_create(data):
    json_error = []

    role_id = data.get("role")
    if not role_id:
        json_error.append("Role is required")
    else:
        if not Role.objects.filter(id=role_id).exists():
            json_error.append("Invalide Role")
            
    menu_name = data.get("menu_name")
    if not menu_name:
        json_error.append("Menu name is required")
    elif MenuRole.objects.filter(menu__iexact=menu_name).exists():   
        json_error.append("Menu name already exists")
    
    is_view = data.get("is_view")
    is_view, error = validate_bool(is_view, "Allow View")
    if error:
        json_error.append(error)
        
    is_edit = data.get("is_edit")
    is_edit, error = validate_bool(is_edit, "Allow edit")
    if error:
        json_error.append(error)
    
    is_add = data.get("is_add")
    is_add, error = validate_bool(is_add, "Allow add")
    if error:
        json_error.append(error)
    
    is_delete = data.get("is_delete")
    is_delete, error = validate_bool(is_delete, "Allow delete")
    if error:
        json_error.append(error)
    
    menu_role_data = {
        "role_id": role_id,
        "menu": menu_name,
        "is_view": is_view,
        "is_edit": is_edit,
        "is_add": is_add,
        "is_delete": is_delete,
    }
    
        
    return menu_role_data, json_error