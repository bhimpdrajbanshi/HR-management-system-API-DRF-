from setup.models import Role

def validate_role_create(data):
    json_error = []

    role_name = data.get("role_name")
    if not role_name:
        json_error.append("Role name is required")
    elif len(role_name) < 2:
        json_error.append("Minimum 2 characters required")
    else:
        if Role.objects.filter(role_name__iexact=role_name).exists():
            json_error.append("Role already exists")
    status = "active"
    # if status not in ["active", "inactive"]:
    #     json_error.append("Invalid status")
    return role_name, status, json_error