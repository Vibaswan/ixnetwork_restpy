from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Geneve_With_INT(Base):
    __slots__ = ()
    _SDM_NAME = 'genevewithtelemetry'
    _SDM_ATT_MAP = {
        'Version': 'genevewithtelemetry.header.version',
        'Options Length (x4 octets)': 'genevewithtelemetry.header.optionslength',
        'Flags': 'genevewithtelemetry.header.flags',
        'Protocol Type': 'genevewithtelemetry.header.protocol',
        'VNI': 'genevewithtelemetry.header.vni',
        'Reserved8': 'genevewithtelemetry.header.reserved8',
        'Length of data field': 'genevewithtelemetry.header.length',
        'Tunnel Options': 'genevewithtelemetry.header.tlv',
    }

    def __init__(self, parent):
        super(Geneve_With_INT, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Options_Length_x4_octets(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Options Length (x4 octets)']))

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
