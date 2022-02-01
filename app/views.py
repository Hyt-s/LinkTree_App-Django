from .serializers import LinkTreeSerializer, LinksSerializer
from .models import LinkTree, Links
from rest_framework.viewsets import ModelViewSet


class LinkTreeMVS(ModelViewSet):
    queryset = LinkTree.objects.all()
    serializer_class = LinkTreeSerializer

class LinksMVS(ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
