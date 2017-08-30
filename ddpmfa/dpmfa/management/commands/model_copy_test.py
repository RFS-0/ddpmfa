from django.core.management.base import BaseCommand, CommandError
from dpmfa import models as dbm
from dpmfa.modelcopier import ModelCopier
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        model1 = dbm.model.objects.get(pk=1)
        model2 = ModelCopier.copy_model(model1)
        print(model1)
        print('------------')
        print(model1.compartments.all())

        print(model2)
        print('------------')
        print(model2.compartments.all())
        print(model2.prototype_model)


