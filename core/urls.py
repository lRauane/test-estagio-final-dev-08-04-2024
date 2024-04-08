from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consumer.views import ConsumerViewSet

router = DefaultRouter()
router.register(r'consumers', ConsumerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include(router.urls))
]
