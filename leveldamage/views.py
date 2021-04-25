from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .models import LevelDamage
from .serializers import LevelDamageSerializer


# Create your views here.

@api_view(['GET', 'POST', 'DELETE', ])
def leveldamage_list(request):
    # Recuperar todos los categorys / busque por name
    if request.method == 'GET':
        name = request.GET.get('name', None)

        if name is not None:
            leveldamages = LevelDamage.objects.filter(name__icontains=name)
        else:
            leveldamages = LevelDamage.objects.all()

        leveldamages_serializer = LevelDamageSerializer(leveldamages, many=True)

        return JsonResponse(leveldamages_serializer.data, safe=False)

    # Crear y guardar un leveldamages nuevo
    elif request.method == 'POST':
        leveldamage_datos = JSONParser().parse(request)
        leveldamage_serializer = LevelDamageSerializer(data=leveldamage_datos)

        if leveldamage_serializer.is_valid():
            leveldamage_serializer.save()

            return JsonResponse(leveldamage_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(leveldamage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los leveldamages
    elif request.method == 'DELETE':
        conteo = LevelDamage.objects.all().delete()

        return JsonResponse(
            {'message': '{} leveldamages fueron eliminados exitosamente'.format(conteo[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE', ])
def leveldamage_detail(request, pk):
    try:
        leveldamage = LevelDamage.objects.get(pk=pk)
    except LevelDamage.DoesNotExist:
        return JsonResponse(
            {'message': 'El leveldamage no existe'},
            status=status.HTTP_404_NOT_FOUND)

    # Recuperar un leveldamage por un id
    if request.method == 'GET':
        leveldamage_serializer = LevelDamageSerializer(leveldamage)
        return JsonResponse(leveldamage_serializer.data)

    # Actualizar un leveldamage por el id
    elif request.method == 'PUT':
        leveldamage_datos = JSONParser().parse(request)
        leveldamage_serializer = LevelDamageSerializer(leveldamage, data=leveldamage_datos)

        if leveldamage_serializer.is_valid():
            leveldamage_serializer.save()

            return JsonResponse(leveldamage_serializer.data)

        return JsonResponse(leveldamage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina un leveldamage por el id
    elif request.method == 'DELETE':
        leveldamage.delete()

        return JsonResponse(
            {'message': 'El leveldamage fue eliminado exitosamente'},
            status=status.HTTP_204_NO_CONTENT
        )