from rest_framework import viewsets
from .models import Showtime
from .serializers import ShowtimeSerializer

class ShowtimeViewSet(viewsets.ModelViewSet):  # NUEVO
    queryset = Showtime.objects.all().order_by('id')
    serializer_class = ShowtimeSerializer