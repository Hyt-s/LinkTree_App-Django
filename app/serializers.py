from rest_framework import serializers
from .models import Links, LinkTree


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"

class LinkTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkTree
        fields = "__all__"
