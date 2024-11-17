from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('education/', views.education, name='education')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
