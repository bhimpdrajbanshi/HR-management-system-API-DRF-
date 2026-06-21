from rest_framework import status


# status massge
SUCCESS = "Success"
CREATED = "Created successfully"

INVALID_DATA = "Invalid data"
UNAUTHORIZED = "Unauthorized access"
NOT_FOUND = "Record not found"

SERVER_ERROR = "Internal server error"


# status code
SUCCESS = status.HTTP_200_OK
CREATED = status.HTTP_201_CREATED

BAD_REQUEST = status.HTTP_400_BAD_REQUEST
UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
FORBIDDEN = status.HTTP_403_FORBIDDEN
NOT_FOUND = status.HTTP_404_NOT_FOUND

SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR