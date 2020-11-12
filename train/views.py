from django.http import JsonResponse
from django.middleware.csrf import CsrfViewMiddleware
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from train.serializers import RequestTrainSerializer, ResponseTrainSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TrainView(View):
    def post(self, request):
        data = JSONParser().parse(request)
        train_data = RequestTrainSerializer(data=data)
        if train_data.is_valid():
            result = train_data.validated_data['leftTrain'] + train_data.validated_data['rightTrain']
            response = ResponseTrainSerializer(data={'sumTrain': result})
            return JsonResponse(response.initial_data)
