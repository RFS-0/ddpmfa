from django.core.management.base import BaseCommand

from dpmfa import models as dbm
#from dpmfa.model2json.ExternalListInflow import ExternalListInflow
#from dpmfa.model2json.FieldList import FieldList
from dpmfa.model2json.Model import Model

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        model_db_entity = dbm.model.objects.get(pk=1)

        model_dict = (Model()).configure_for(model_db_entity).as_dictionary()
        model_json = json.dumps(model_dict, indent=2)

        #print(model_json)

        #e = ExternalListInflow(2)
        #e.apply_default_configuration()
        #print(json.dumps(e.as_dictionary(), indent=2))


        #print(model)


