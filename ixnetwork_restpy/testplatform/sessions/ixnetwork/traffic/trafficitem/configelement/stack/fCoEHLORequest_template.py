from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_HLO_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEHLORequest'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEHLORequest.header.fcoeHeader',
        'FC Header': 'fCoEHLORequest.header.fcHeader',
        'FC Command': 'fCoEHLORequest.header.fcCmd',
        'FSPF Header': 'fCoEHLORequest.header.fspfHeader',
        'Reserved1': 'fCoEHLORequest.header.reserved1',
        'Hello_Interval': 'fCoEHLORequest.header.helloInterval',
        'Dead_Interval': 'fCoEHLORequest.header.deadInterval',
        'Recipient Domain_ID': 'fCoEHLORequest.header.recipientDID',
        'Reserved2': 'fCoEHLORequest.header.reserved2',
        'Originating Port Index': 'fCoEHLORequest.header.origPortIndex',
    }

    def __init__(self, parent):
        super(FCoE_HLO_Request, self).__init__(parent)

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
