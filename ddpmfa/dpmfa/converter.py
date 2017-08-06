import dpmfa.models as django_models
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import components as package_components
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import model as package_model
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import simulator as package_simulator

class CompartmentConverter(object):
    
    def __init__(self, db_compartment):
        self.compartment_db = db_compartment
        self.compNumber = db_compartment.pk
        self.name = db_compartment.name
        self.logInflows = db_compartment.log_inflows
        self.categories = db_compartment.categories
        self.compartment_dpmfa = package_components.Compartment(
            self.name, 
            self.logInflows, 
            self.categories
            )
                
        #except:
        #    print("Could not convert the entity received from the db")
            
    def getDpmfaCompartment(self):
        return self.compartment_dpmfa
        
        