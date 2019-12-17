from elasticsearch_dsl import Index

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Product

# The name of your index
product = Index('products')

# See ElasticSearch Indices API reference for available settings
product.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@registry.register_document
@product.document
class ProductDocument(Document):
    class Django:
        model = Product  # The model associated with this Document

        # The fields of the model you want to be indexed in ElasticSearch
        fields = (
            'title',
            'summary',
        )
