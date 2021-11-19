import graphene

import apps.marktplaats.schema


class Query(apps.marktplaats.schema.Query):
    pass

schema = graphene.Schema(query=Query)