from django.core.management.base import BaseCommand, CommandError
from dpmfa import models as dbm
from dpmfa import converter as conv
from django.contrib.auth.models import User

class Command(BaseCommand):

    def play_release(self, func_name, func_args):
        r = dbm.function_release.objects.get(pk=2)
        r.release_function = func_name
        r.function_parameters = func_args
        r.save()

        c = conv.FunctionReleaseConverter(r)
        f = c.releaseFunction

        print(func_name)
        print('---------------')
        print(f)
        print(f(0))
        print(f(10))
        print(f(20))
        print(f(30))

    def handle(self, *args, **options):
        self.play_release('LI', '-10,0.1')
        self.play_release('PO', '10,20,-10,2')
        self.play_release('EX', '20,10,.2,.3')
        self.play_release('LG', '20,10,30,40')
        self.play_release('SI', '10,0.03,5')
        self.play_release('CO', '10,0.03,5')


