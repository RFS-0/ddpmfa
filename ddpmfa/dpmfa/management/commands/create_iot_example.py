from django.core.management.base import BaseCommand, CommandError
from dpmfa.models import *

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        iot_project = project.objects.filter(name='IoT project')
        
        if len(iot_project) >= 1:
            self.stdout.write("The IoT project already exists\n", ending='')
            self.stdout.write("Exiting without any changes to db\n", ending='')
            self.stdout.write("Bye", ending='')
            return
        
        # creation of the project
        iot_project = project()
        iot_project.name = 'IoT project'
        iot_project.description = 'This is the description of the IoT project. It is great. Very great.'
        iot_project.save()
        
        # creation of the model
        iot_model = model()
        iot_model.name = 'IoT Model'    
        iot_model.description = 'This is a very detailed description of the IoT example model. It describes everything. It is awesome.'
        iot_model.seed = 1
        iot_model.project = iot_project
        iot_model.save()
        