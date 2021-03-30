from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Geneve(Base):
    __slots__ = ()
    _SDM_NAME = 'geneve'
    _SDM_ATT_MAP = {
        'Version': 'geneve.header.version',
        'Options Length': 'geneve.header.optionslen',
        'Flags': 'geneve.header.flags',
        'Protocol Type': 'geneve.header.protocol',
        'VNI': 'geneve.header.vni',
        'Reserved8': 'geneve.header.reserved8',
        'Length of data field': 'geneve.header.length',
        'Tunnel Options': 'geneve.header.options',
    }

    def __init__(self, parent):
        super(Geneve, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Options_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Options Length']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Type']))

    @property
    def VNI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VNI']))

    @property
    def Reserved8(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved8']))

    @property
    def Length_of_data_field(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length of data field']))

    @property
    def Tunnel_Options(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Tunnel Options']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
