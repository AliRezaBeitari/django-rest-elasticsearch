from rest_framework import serializers

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Product
from .documents import ProductDocument


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'summary',
            'description',
            'created_at',
        )


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        # Specify the correspondent document class
        document = ProductDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'title',
            'summary',
            'description',
            'created_at',
        )
