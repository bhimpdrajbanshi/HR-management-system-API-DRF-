from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

class SessionExpiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Skip login page
        if request.path == reverse("login"):
            return self.get_response(request)

        # Session expired
        if (
            request.session.session_key and
            not request.user.is_authenticated
        ):
            messages.error(
                request,
                "Your session has expired. Please log in again."
            )

            return redirect("login")

        return self.get_response(request)