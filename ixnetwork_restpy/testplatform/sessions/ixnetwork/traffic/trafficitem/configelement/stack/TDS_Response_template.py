from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TDS_Response(Base):
    __slots__ = ()
    _SDM_NAME = 'TDS_Response'
    _SDM_ATT_MAP = {
        'Type': 'TDS_Response.header.Type',
        'Status': 'TDS_Response.header.Status',
        'Length': 'TDS_Response.header.Length',
        'Channel': 'TDS_Response.header.Channel',
        'Packet number': 'TDS_Response.header.Packet number',
        'Window': 'TDS_Response.header.Window',
        'Token 0xff Done in Proc': 'TDS_Response.header.Token 0xff Done in Proc',
        'Token 0x00 Unknown Token Type': 'TDS_Response.header.Token 0x00 Unknown Token Type',
        'Token 0x00 Unknown Token Type 2': 'TDS_Response.header.Token 0x00 Unknown Token Type 2',
    }

    def __init__(self, parent):
        super(TDS_Response, self).__init__(parent)

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
    def Token_0xff_Done_in_Proc(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Token 0xff Done in Proc']))

    @property
    def Token_0x00_Unknown_Token_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Token 0x00 Unknown Token Type']))

    @property
    def Token_0x00_Unknown_Token_Type_2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Token 0x00 Unknown Token Type 2']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
