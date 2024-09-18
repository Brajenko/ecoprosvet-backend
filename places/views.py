from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView

from .models import Place, PlacesImage

from .serializers import PlaceSerializer, PlacesImageSerializer

from users.permissions import IsCreator, IsOrganizer

class PlaceListView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlacesImageCreateView(CreateAPIView):
    queryset = PlacesImage.objects.all()
    serializer_class = PlacesImageSerializer
    permission_classes = [IsOrganizer]
