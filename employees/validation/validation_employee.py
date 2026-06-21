
from employees.models import Employee
from setup.validation.global_validation import validate_email
from setup.models import Role
from accounts.models import User

def validate_employee_create(data):
    json_error = []
    
    # employee acount
    email = data.get("email")
    if not email:
        json_error.append("Email is required")
    elif not validate_email(email):
        json_error.append("Invalid Email")
    else:
        if User.objects.filter(email=email).exists():
            json_error.append("Email already exists")
    
    username = data.get("username")
    if not username:
        json_error.append("Username is required")
    else:
        if User.objects.filter(username__iexact=username).exists():
            json_error.append("Username already exists")
    
    role = data.get("role")
    if not role:
        json_error.append("Role is required")
    else:
        if Role.objects.filter(id=role).exists():
            pass
        else:
            json_error.append("Invalide Role")
    
    employee_account_data = {
        "email": email,
        "username": username,
        "role_id": role,
    }
    
    # employee profile
    first_name = data.get("firstName")
    if not first_name:
        json_error.append("First name is required")
    elif len(first_name) < 2:
        json_error.append("First Name Minimum 2 characters required")
        
    middle_name = data.get("middleName")
    
    last_name = data.get("lastName")
    if not last_name:
        json_error.append("Last name is required")
    elif len(first_name) < 2:
        json_error.append("Last Name Minimum 2 characters required")
    
    employee_profile_data = {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
    }
    
    return employee_account_data, employee_profile_data, json_error
        