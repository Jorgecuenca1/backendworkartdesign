from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.decorators import api_view

from .models import CategoryDamage
from .serializers import CategoryDamageSerializer

from rest_framework.decorators import api_view, schema


from rest_framework.schemas import AutoSchema

# Create your views here.


# Create your views here.


@api_view(['GET', 'POST', 'DELETE', ])

def categorydamage_list(request):

    # Recuperar todos los categorys / busque por name
    if request.method == 'GET':
        name = request.GET.get('name', None)

        if name is not None:
            categorydamages = CategoryDamage.objects.filter(name__icontains=name)
        else:
            categorydamages = CategoryDamage.objects.all()

        categorydamages_serializer = CategoryDamageSerializer(categorydamages, many=True)

        return JsonResponse(categorydamages_serializer.data, safe=False)

    # Crear y guardar un categorydamage nuevo
    elif request.method == 'POST':
        categorydamage_datos = JSONParser().parse(request)
        categorydamage_serializer = CategoryDamageSerializer(data=categorydamage_datos)

        if categorydamage_serializer.is_valid():
            categorydamage_serializer.save()

            return JsonResponse(categorydamage_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(categorydamage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los categorydamages
    elif request.method == 'DELETE':
        conteo = CategoryDamage.objects.all().delete()

        return JsonResponse(
            {'message': '{} categorydamages fueron eliminados exitosamente'.format(conteo[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE', ])
def categorydamage_detail(request, pk):
    try:
        categorydamage = CategoryDamage.objects.get(pk=pk)
    except CategoryDamage.DoesNotExist:
        return JsonResponse(
            {'message': 'El categorydamage no existe'},
            status=status.HTTP_404_NOT_FOUND)

    # Recuperar un categorydamage por un id
    if request.method == 'GET':
        categorydamage_serializer = CategoryDamageSerializer(categorydamage)
        return JsonResponse(categorydamage_serializer.data)

    # Actualizar un categorydamage por el id
    elif request.method == 'PUT':
        categorydamage_datos = JSONParser().parse(request)
        categorydamage_serializer = CategoryDamageSerializer(categorydamage, data=categorydamage_datos)

        if categorydamage_serializer.is_valid():
            categorydamage_serializer.save()

            return JsonResponse(categorydamage_serializer.data)

        return JsonResponse(categorydamage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina un categorydamage por el id
    elif request.method == 'DELETE':
        categorydamage.delete()

        return JsonResponse(
            {'message': 'El categorydamage fue eliminado exitosamente'},
            status=status.HTTP_204_NO_CONTENT
        )