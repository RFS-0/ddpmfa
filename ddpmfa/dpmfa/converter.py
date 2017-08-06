import dpmfa.models as django_models
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import components as package_components
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import model as package_model
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import simulator as package_simulator

class CompartmentConverter(object):
    
    def __init__(self, db_compartment=django_models.compartment):
        try: 
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
                
        except:
            print("Could not convert the entity received from the db to dpmfa compartment")
            
    def getCompartment(self):
        return self.compartment_dpmfa
    
class FlowCompartmentConverter(CompartmentConverter):
    
    def __init__(self, db_flow_compartment=django_models.flow_compartment):
        super(FlowCompartmentConverter, self).__init__(db_flow_compartment)
        
        try:      
            self.transfers = []        
            self.adjustOutTCs = db_flow_compartment.adjust_outgoing_tcs
            self.logOutflows = db_flow_compartment.log_outflows
            self.immediateReleaseRate = 1
            
            self.flow_compartment_dpmfa = package_components.FlowCompartment(
                self.name, 
                self.transfers, 
                self.logInflows, 
                self.logOutflows, 
                self.adjustOutTCs, 
                self.categories
                )
        
        except:
            print("Could not convert the entity received from the db to dpmfa flow compartment")
     
        
    def getFlowCompartment(self):
        return self.flow_compartment_dpmfa
    
    
    
    
    
    
    
    