from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .models import TypePainting
from .serializers import TypePaintingSerializer


# Create your views here.

@api_view(['GET', 'POST', 'DELETE', ])
def typepainting_list(request):
    # Recuperar todos los categorys / busque por name
    if request.method == 'GET':
        name = request.GET.get('name', None)

        if name is not None:
            typepaintings = TypePainting.objects.filter(name__icontains=name)
        else:
            typepaintings = TypePainting.objects.all()

        typepaintings_serializer = TypePaintingSerializer(typepaintings, many=True)

        return JsonResponse(typepaintings_serializer.data, safe=False)

    # Crear y guardar un typepaintings nuevo
    elif request.method == 'POST':
        typepainting_datos = JSONParser().parse(request)
        typepainting_serializer = TypePaintingSerializer(data=typepainting_datos)

        if typepainting_serializer.is_valid():
            typepainting_serializer.save()

            return JsonResponse(typepainting_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(typepainting_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los typepaintings
    elif request.method == 'DELETE':
        conteo = TypePainting.objects.all().delete()

        return JsonResponse(
            {'message': '{} typepaintings fueron eliminados exitosamente'.format(conteo[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE', ])
def typepainting_detail(request, pk):
    try:
        typepainting = TypePainting.objects.get(pk=pk)
    except TypePainting.DoesNotExist:
        return JsonResponse(
            {'message': 'El typepainting no existe'},
            status=status.HTTP_404_NOT_FOUND)

    # Recuperar un typepainting por un id
    if request.method == 'GET':
        typepainting_serializer = TypePaintingSerializer(typepainting)
        return JsonResponse(typepainting_serializer.data)

    # Actualizar un typepainting por el id
    elif request.method == 'PUT':
        typepainting_datos = JSONParser().parse(request)
        typepainting_serializer = TypePaintingSerializer(typepainting, data=typepainting_datos)

        if typepainting_serializer.is_valid():
            typepainting_serializer.save()

            return JsonResponse(typepainting_serializer.data)

        return JsonResponse(typepainting_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina un typepainting por el id
    elif request.method == 'DELETE':
        typepainting.delete()

        return JsonResponse(
            {'message': 'El typepainting fue eliminado exitosamente'},
            status=status.HTTP_204_NO_CONTENT
        )