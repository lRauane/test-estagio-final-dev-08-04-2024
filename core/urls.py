from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consumer.views import ConsumerViewSet, CalculatorAPIView, CalculatorInterfaceView

router = DefaultRouter()
router.register(r'consumers', ConsumerViewSet)

urlpatterns = [
	path('api/calculator/', CalculatorAPIView.as_view(), name="calculator"),
	path('calculator/', CalculatorInterfaceView.as_view(), name='calculator_interface'),
]
