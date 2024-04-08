from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consumer.views import ConsumerViewSet, CalculatorAPIView, CalculatorInterfaceView, ConsumersAPIView, ConsumersInterfaceView

router = DefaultRouter()
router.register(r'consumers', ConsumerViewSet)

urlpatterns = [
	path('api/calculator/', CalculatorAPIView.as_view(), name="calculator"),
	path('calculator/', CalculatorInterfaceView.as_view(), name='calculator_interface'),
	path('api/consumers/', ConsumersAPIView.as_view(), name='consumers'),
	path('consumers/', ConsumersInterfaceView.as_view(), name='consumers_interface'),
]
