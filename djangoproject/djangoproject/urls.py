from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/polls/')),  # Redirect root to /polls/
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]