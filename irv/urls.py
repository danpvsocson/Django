
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home/index.html"), name='home'),
    path('page2/', TemplateView.as_view(template_name="home/page2.html"), name='page2'),
]
