from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_ESC_SW_ACC(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEESCSWACC'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEESCSWACC.header.fcoeHeader',
        'FC Header': 'fCoEESCSWACC.header.fcHeader',
        'FC Command': 'fCoEESCSWACC.header.fcCmd',
        'Reserved1': 'fCoEESCSWACC.header.reserved1',
        'Reserved2': 'fCoEESCSWACC.header.reserved2',
        'Payload Length': 'fCoEESCSWACC.header.length',
        'Vendor Id String': 'fCoEESCSWACC.header.vendorId',
        'Accepted Protocol Descriptor': 'fCoEESCSWACC.header.protocolDescriptor',
    }

    def __init__(self, parent):
        super(FCoE_ESC_SW_ACC, self).__init__(parent)

    @property
    def FCoE_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCoE Header']))

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
