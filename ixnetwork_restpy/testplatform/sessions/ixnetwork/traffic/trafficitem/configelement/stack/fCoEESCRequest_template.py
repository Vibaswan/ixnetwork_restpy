from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_ESC_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEESCRequest'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEESCRequest.header.fcoeHeader',
        'FC Header': 'fCoEESCRequest.header.fcHeader',
        'FC Command': 'fCoEESCRequest.header.fcCmd',
        'Reserved1': 'fCoEESCRequest.header.reserved1',
        'Flags': 'fCoEESCRequest.header.flags',
        'Payload Length': 'fCoEESCRequest.header.length',
        'Vendor Id String': 'fCoEESCRequest.header.vendorId',
        'Protocol Descriptor': 'fCoEESCRequest.header.protocolDescriptor',
    }

    def __init__(self, parent):
        super(FCoE_ESC_Request, self).__init__(parent)

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
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Payload_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Length']))

    @property
    def Vendor_Id_String(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vendor Id String']))

    @property
    def Protocol_Descriptor(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Descriptor']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
