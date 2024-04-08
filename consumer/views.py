from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status, response, request
from .models import Consumer
from .serializers import ConsumerSerializer
from rest_framework.response import Response
from django.views.generic import TemplateView
from calculator import calculator

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
	
class CalculatorAPIView(APIView):
    def post(self, request):
        data = request.data
        consumption_month1 = int(data.get('consumption_month1'))
        consumption_month2 = int(data.get('consumption_month2'))
        consumption_month3 = int(data.get('consumption_month3'))
        distributor_tax = float(data.get('distributor_tax'))
        tax_type = data.get('tax_type')
        
        result = calculator([consumption_month1, consumption_month2, consumption_month3], distributor_tax, tax_type)  # Use o módulo importado corretamente
        return Response({
            'annual_savings': result[0],
            'monthly_savings': result[1],
            'applied_discount': result[2],
            'coverage': result[3]
        }, status=status.HTTP_200_OK)
	
    def get(self, request):
        return Response({'result': 'hello'}, status=status.HTTP_200_OK)

class CalculatorInterfaceView(TemplateView):
    template_name = 'calculator_interface.html'
	
class ConsumersAPIView(APIView):
    def post(self, request):
        data = request.data
        discount_rule_id = int(data.get("DiscountRule"))
        
        consumer = Consumer.objects.create(
            name=data.get('name'),
            document=data.get('document'),
            zip_code=data.get('zip_code'),
            city=data.get('city'),
            state=data.get("state"),
            consumption = int(data.get("consumption")),
            distributor_tax=float(data.get("distributor_tax")),
        )
        
        return Response({
            "message": "OK"
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        consumers = Consumer.objects.all()
        serializer = ConsumerSerializer(consumers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConsumersInterfaceView(TemplateView):
    template_name = 'list_consumers.html'
