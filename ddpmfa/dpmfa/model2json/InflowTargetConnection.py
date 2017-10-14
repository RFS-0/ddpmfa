from dpmfa.model2json.Connection import Connection


class InflowTargetConnection(Connection):

    def __init__(self, owner):
        super(InflowTargetConnection, self).__init__(owner, 'inflowTarget', 'Inflow Target')
