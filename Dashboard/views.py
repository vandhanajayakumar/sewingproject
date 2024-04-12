
#1st
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import MachineData
# from .serializers import MachineDataSerializer
# import logging

# logger = logging.getLogger(__name__)

# @api_view(['GET', 'POST'])
# def machine_data_list_create(request):
#     if request.method == 'GET':
#         queryset = MachineData.objects.all()
#         serializer = MachineDataSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MachineDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         logger.error(serializer.errors) 
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def machine_data_detail(request, pk):
#     try:
#         machine_data = MachineData.objects.get(pk=pk)
#     except MachineData.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = MachineDataSerializer(machine_data)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MachineDataSerializer(machine_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         logger.error(serializer.errors)  
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         machine_data.delete()
#         return Response(status=204)


#2
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import MachineData
# from .serializers import MachineDataSerializer
# import logging

# logger = logging.getLogger(__name__)

# @api_view(['GET', 'POST'])
# def machine_data_list_create(request):
#     if request.method == 'GET':
#         return Response({"message": "Data retrieved successfully"})
#     elif request.method == 'POST':
#         serializer = MachineDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Data created successfully"}, status=201) 
#         logger.error(serializer.errors) 
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def machine_data_detail(request, pk):
#     try:
#         machine_data = MachineData.objects.get(pk=pk)
#     except MachineData.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         return Response({"message": "Data retrieved successfully"})
#     elif request.method == 'PUT':
#         serializer = MachineDataSerializer(machine_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         logger.error(serializer.errors)  
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         machine_data.delete()
#         return Response(status=204)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MachineData
from .serializers import MachineDataSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def machine_data_list_create(request):
    if request.method == 'GET':
        if 'Postman' in request.META.get('HTTP_USER_AGENT', ''):
            return Response({"message": "Data retrieved successfully"})
        else:
            queryset = MachineData.objects.all()
            serializer = MachineDataSerializer(queryset, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MachineDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data created successfully"}, status=201) 
        logger.error(serializer.errors) 
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def machine_data_detail(request, pk):
    try:
        machine_data = MachineData.objects.get(pk=pk)
    except MachineData.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        if 'Postman' in request.META.get('HTTP_USER_AGENT', ''):
            return Response({"message": "Data retrieved successfully"})
        else:
            serializer = MachineDataSerializer(machine_data)
            return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MachineDataSerializer(machine_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(serializer.errors)  
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        machine_data.delete()
        return Response(status=204)
