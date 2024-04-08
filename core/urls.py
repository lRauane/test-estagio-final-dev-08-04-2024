from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consumer.views import ConsumerViewSet, CalculatorAPIView

router = DefaultRouter()
router.register(r'consumers', ConsumerViewSet)

urlpatterns = [
	path('api/calculator/', CalculatorAPIView.as_view(), name="calculator"),
]
