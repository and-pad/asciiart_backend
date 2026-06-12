import os

from django.conf import settings
from django.utils.text import get_valid_filename
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .jpgtotext import asciijpg


def parse_bool(value):
    return str(value).lower() in {"true", "1", "yes", "on"}


def parse_positive_int(value, field_name):
    if value in (None, ""):
        return None

    try:
        parsed_value = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} debe ser un número entero")

    if parsed_value < 0:
        raise ValueError(f"{field_name} debe ser un número entero positivo")

    return parsed_value


class asciiJpg(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        image = request.FILES.get("image")

        if not image:
            return Response(
                {"error": "No se recibió imagen"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            width = parse_positive_int(request.data.get("width"), "width")
            height = parse_positive_int(request.data.get("height"), "height")
        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        colors = parse_bool(request.data.get("colors"))

        temp_dir = os.path.join(settings.BASE_DIR, "temp")
        os.makedirs(temp_dir, exist_ok=True)

        filename = get_valid_filename(image.name)
        image_path = os.path.join(temp_dir, filename)

        with open(image_path, "wb+") as file:
            for chunk in image.chunks():
                file.write(chunk)

        try:
            html = asciijpg().convert(
                image_path=image_path,
                width=width,
                height=height,
                colors=colors,
            )
        except Exception:
            os.remove(image_path)
            return Response(
                {"error": "No fue posible convertir la imagen a ASCII"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        os.remove(image_path)

        return Response({"html": html}, status=status.HTTP_200_OK)
