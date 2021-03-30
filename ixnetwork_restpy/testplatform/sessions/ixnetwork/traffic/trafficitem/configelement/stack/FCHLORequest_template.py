from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_HLO_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'FCHLORequest'
    _SDM_ATT_MAP = {
        'FC Header': 'fcHLORequest.header.fcHeader',
        'FC Command': 'fcHLORequest.header.fcCmd',
        'FSPF Header': 'fcHLORequest.header.fspfHeader',
        'Reserved1': 'fcHLORequest.header.reserved1',
        'Hello_Interval': 'fcHLORequest.header.helloInterval',
        'Dead_Interval': 'fcHLORequest.header.deadInterval',
        'Recipient Domain_ID': 'fcHLORequest.header.recipientDID',
        'Reserved2': 'fcHLORequest.header.reserved2',
        'Originating Port Index': 'fcHLORequest.header.origPortIndex',
    }

    def __init__(self, parent):
        super(FC_HLO_Request, self).__init__(parent)

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_Command(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Command']))

    @property
    def FSPF_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FSPF Header']))

    @property
    def Reserved1(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved1']))

    @property
    def Hello_Interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hello_Interval']))

    @property
    def Dead_Interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dead_Interval']))

    @property
    def Recipient_Domain_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Recipient Domain_ID']))

    @property
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    @property
    def Originating_Port_Index(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Originating Port Index']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
