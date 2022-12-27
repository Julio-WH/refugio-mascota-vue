from django.http import Http404

from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from app.API.serializers import MascotasSerializer, PersonaSerializer, VacunaSerializer, PersonaSerializer
from app.mascota.models import Mascota, Vacuna
from app.adopcion.models import Persona


class ListMascotas(APIView):

    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        mascotas = Mascota.objects.all().select_related('persona').prefetch_related('vacuna').order_by("-fecha_rescate")
        mascotas_json = MascotasSerializer(mascotas, many=True)
        return Response(mascotas_json.data)

    def post(self, request):
        print(request.data)
        mascotas_json = MascotasSerializer(data=request.data)  # UnMarshall
        if mascotas_json.is_valid():
            mascotas_json.save()
            return Response(mascotas_json.data, status=status.HTTP_201_CREATED)
        return Response(mascotas_json.errors, status=status.HTTP_400_BAD_REQUEST)

class ListVacunas(APIView):
    def get(self, request):
        vacunas = Vacuna.objects.all()
        vacunas_json = VacunaSerializer(vacunas, many=True)
        return Response(vacunas_json.data)

class ListPersonas(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        persona_json = PersonaSerializer(personas, many=True)
        return Response(persona_json.data)
class DetalleMascota(APIView):

    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mascotas = self.get_object(pk)
        mascotas_json = MascotasSerializer(mascotas)
        return Response(mascotas_json.data)

    def put(self, request, pk):
        mascotas = self.get_object(pk)
        mascotas_json = MascotasSerializer(mascotas, data=request.data)
        if mascotas_json.is_valid():
            mascotas_json.save()
            return Response(mascotas_json.data)
        return Response(mascotas_json.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MascotaPersonaList(APIView):
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mascotas = self.get_object(pk)
        mascotas_json = PersonaSerializer(mascotas.persona)
        return Response(mascotas_json.data)
