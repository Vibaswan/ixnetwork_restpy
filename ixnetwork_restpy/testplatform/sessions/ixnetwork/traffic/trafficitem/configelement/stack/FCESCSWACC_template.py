from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_ESC_SW_ACC(Base):
    __slots__ = ()
    _SDM_NAME = 'FCESCSWACC'
    _SDM_ATT_MAP = {
        'FC Header': 'fcESCSWACC.header.fcHeader',
        'FC Command': 'fcESCSWACC.header.fcCmd',
        'Reserved1': 'fcESCSWACC.header.reserved1',
        'Reserved2': 'fcESCSWACC.header.reserved2',
        'Payload Length': 'fcESCSWACC.header.length',
        'Vendor Id String': 'fcESCSWACC.header.vendorId',
        'Accepted Protocol Descriptor': 'fcESCSWACC.header.protocolDescriptor',
    }

    def __init__(self, parent):
        super(FC_ESC_SW_ACC, self).__init__(parent)

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_Command(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Command']))

    @property
    def Reserved1(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved1']))

    @property
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    @property
    def Payload_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Length']))

    @property
    def Vendor_Id_String(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vendor Id String']))

    @property
    def Accepted_Protocol_Descriptor(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accepted Protocol Descriptor']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
