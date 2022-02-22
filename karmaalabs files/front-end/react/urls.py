from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from .views import ReactView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('wel/', ReactView.as_view(), name="page"),
]
