# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django.contrib.auth.models import User
# from django.contrib import messages

# def login_view(request):
#     # Show session expired message
#     if request.method == "GET" and request.GET.get("next"):
#         messages.warning(
#             request,
#             "Your session has expired. Please log in again."
#         )

#     if request.method == "POST":

#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         user = authenticate(
#             email=email,
#             password=password
#         )

#         if user:
#             login(request, user)
#             return redirect("dashboard/")

#         messages.error(request, "Invalid username or password")
#     return render(request, "accounts/login.html")


# def register_view(request):

#     form = RegisterForm(request.POST or None)

#     if form.is_valid():

#         user = form.save(commit=False)

#         user.set_password(form.cleaned_data["password"])

#         user.save()

#         messages.success(request, "Account Created")

#         return redirect("login")

#     return render(
#         request,
#         "accounts/register.html",
#         {"form": form}
#     )


# def logout_view(request):
#     logout(request)
#     return redirect("login")


# def profile_view(request):

#     return render(
#         request,
#         "accounts/profile.html"
#     )


# def forgot_password(request):

#     if request.method == "POST":

#         email = request.POST.get("email")

#         messages.success(
#             request,
#             "Password reset link sent."
#         )

#     return render(
#         request,
#         "accounts/forgot_password.html"
#     )


# def reset_password(request):

#     if request.method == "POST":

#         password = request.POST.get("password")

#         confirm = request.POST.get("confirm")

#         if password == confirm:

#             messages.success(
#                 request,
#                 "Password Changed Successfully"
#             )

#             return redirect("login")

#     return render(
#         request,
#         "accounts/reset_password.html"
#     )


# def change_password(request):

#     if request.method == "POST":

#         old = request.POST.get("old")

#         new = request.POST.get("new")

#         confirm = request.POST.get("confirm")

#         if new == confirm:

#             user = request.user

#             if user.check_password(old):

#                 user.set_password(new)

#                 user.save()

#                 update_session_auth_hash(
#                     request,
#                     user
#                 )

#                 messages.success(
#                     request,
#                     "Password Updated"
#                 )

#                 return redirect("profile")

#     return render(
#         request,
#         "accounts/change_password.html"
#     )