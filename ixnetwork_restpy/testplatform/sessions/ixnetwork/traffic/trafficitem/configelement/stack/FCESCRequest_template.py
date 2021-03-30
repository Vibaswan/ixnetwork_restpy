from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_ESC_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'FCESCRequest'
    _SDM_ATT_MAP = {
        'FC Header': 'fcESCRequest.header.fcHeader',
        'FC Command': 'fcESCRequest.header.fcCmd',
        'Reserved1': 'fcESCRequest.header.reserved1',
        'Flags': 'fcESCRequest.header.flags',
        'Payload Length': 'fcESCRequest.header.length',
        'Vendor Id String': 'fcESCRequest.header.vendorId',
        'Protocol Descriptor': 'fcESCRequest.header.protocolDescriptor',
    }

    def __init__(self, parent):
        super(FC_ESC_Request, self).__init__(parent)

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
