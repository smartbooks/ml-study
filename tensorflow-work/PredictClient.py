# -*- coding: utf-8 -*-

from tensorflow_serving.apis import classification_pb2
from tensorflow_serving.apis import regression_pb2
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2

from grpc.beta import implementations

'''
pip install tensorflow-serving-api
pip install grpcio
'''

channel = implementations.insecure_channel("0.0.0.0", int(8500))
stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

request = classification_pb2.ClassificationRequest()
example = request.input.example_list.examples.add()
#example.features.feature['SepalLength'].float_list.value.extend([float(100)])

result = stub.Classify(request, 10.0)  # 10 secs timeout

print(result)
