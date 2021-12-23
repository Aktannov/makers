from django.urls import path

from account.views import RegistrationView, ActivationView, LoginView, ForgotPasswordView, LogoutView, \
    ForgotPasswordFinalView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_final/', ForgotPasswordFinalView.as_view()),
]
