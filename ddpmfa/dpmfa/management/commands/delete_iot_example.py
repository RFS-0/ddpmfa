from django.core.management.base import BaseCommand, CommandError
from dpmfa.models import *

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        iot_project = project.objects.filter(name='IoT project')
        
        if len(iot_project) < 1:
            self.stdout.write("There is no iot example to delete\n", ending='')
            self.stdout.write("Exiting without any changes to db\n", ending='')
            self.stdout.write("Bye", ending='')
            return
        
        # delete the project
        iot_project.delete()
        self.stdout.write("Delete IoT project from the db", ending='')