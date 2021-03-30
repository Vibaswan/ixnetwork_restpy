from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TDS_Remote_Procedure_Call(Base):
    __slots__ = ()
    _SDM_NAME = 'TDS_Remote_Procedure_Call'
    _SDM_ATT_MAP = {
        'Type': 'TDS_Remote_Procedure_Call.header.Type',
        'Status': 'TDS_Remote_Procedure_Call.header.Status',
        'Length': 'TDS_Remote_Procedure_Call.header.Length',
        'Channel': 'TDS_Remote_Procedure_Call.header.Channel',
        'Packet number': 'TDS_Remote_Procedure_Call.header.Packet number',
        'Window': 'TDS_Remote_Procedure_Call.header.Window',
        'Remote Procedure Call': 'TDS_Remote_Procedure_Call.header.Remote Procedure Call',
    }

    def __init__(self, parent):
        super(TDS_Remote_Procedure_Call, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Status(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Status']))

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def Channel(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Channel']))

    @property
    def Packet_number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Packet number']))

    @property
    def Window(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Window']))

    @property
    def Remote_Procedure_Call(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Remote Procedure Call']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
