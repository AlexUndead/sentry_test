from django.urls import path

def trigger_error(request):
    devision_by_zero = 1 / 0

urlpatterns = [
    path('sentry-test/', trigger_error),
]
