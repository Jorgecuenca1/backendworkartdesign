from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .models import CostRestauration
from .serializers import CostRestaurationSerializer


# Create your views here.

@api_view(['GET', 'POST', 'DELETE', ])
def costrestauration_list(request):
    # Recuperar todos los categorys / busque por cost
    if request.method == 'GET':
        cost = request.GET.get('cost', None)

        if cost is not None:
            costrestaurations = CostRestauration.objects.filter(cost__icontains=cost)
        else:
            costrestaurations = CostRestauration.objects.all()

        costrestaurations_serializer = CostRestaurationSerializer(costrestaurations, many=True)

        return JsonResponse(costrestaurations_serializer.data, safe=False)

    # Crear y guardar un costrestaurations nuevo
    elif request.method == 'POST':
        costrestauration_datos = JSONParser().parse(request)
        costrestauration_serializer = CostRestaurationSerializer(data=costrestauration_datos)

        if costrestauration_serializer.is_valid():
            costrestauration_serializer.save()

            return JsonResponse(costrestauration_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(costrestauration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los costrestaurations
    elif request.method == 'DELETE':
        conteo = CostRestauration.objects.all().delete()

        return JsonResponse(
            {'message': '{} costrestaurations fueron eliminados exitosamente'.format(conteo[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE', ])
def costrestauration_detail(request, pk):
    try:
        costrestauration = CostRestauration.objects.get(pk=pk)
    except CostRestauration.DoesNotExist:
        return JsonResponse(
            {'message': 'El costrestauration no existe'},
            status=status.HTTP_404_NOT_FOUND)

    # Recuperar un costrestauration por un id
    if request.method == 'GET':
        costrestauration_serializer = CostRestaurationSerializer(costrestauration)
        return JsonResponse(costrestauration_serializer.data)

    # Actualizar un costrestauration por el id
    elif request.method == 'PUT':
        costrestauration_datos = JSONParser().parse(request)
        costrestauration_serializer = CostRestaurationSerializer(costrestauration, data=costrestauration_datos)

        if costrestauration_serializer.is_valid():
            costrestauration_serializer.save()

            return JsonResponse(costrestauration_serializer.data)

        return JsonResponse(costrestauration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina un costrestauration por el id
    elif request.method == 'DELETE':
        costrestauration.delete()

        return JsonResponse(
            {'message': 'El leveldamage fue eliminado exitosamente'},
            status=status.HTTP_204_NO_CONTENT
        )