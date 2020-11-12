from rest_framework import serializers


class RequestTrainSerializer(serializers.Serializer):
    leftTrain = serializers.IntegerField()
    rightTrain = serializers.IntegerField()

class ResponseTrainSerializer(serializers.Serializer):
    sumTrain = serializers.IntegerField()

