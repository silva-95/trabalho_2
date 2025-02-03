from rest_framework import serializers
from produto.models import Topico

class TopicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topico
        fields = '__all__'
