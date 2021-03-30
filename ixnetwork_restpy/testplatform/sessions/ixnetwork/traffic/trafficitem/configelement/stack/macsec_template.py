from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MACsec(Base):
    __slots__ = ()
    _SDM_NAME = 'macsec'
    _SDM_ATT_MAP = {
        'Metadata': 'macsec.secTag.metadata',
        'TCI (TAG Control Information)': 'macsec.secTag.tci',
        'Association Number (AN)': 'macsec.secTag.an',
        'Short Length (SL)': 'macsec.secTag.sl',
        'Packet Number (PN)': 'macsec.secTag.pn',
        'Secure Channel Identifier (SCI)': 'macsec.secTag.sci',
    }

    def __init__(self, parent):
        super(MACsec, self).__init__(parent)

    @property
    def Metadata(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metadata']))

    @property
    def TCI_TAG_Control_Information(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TCI (TAG Control Information)']))

    @property
    def Association_Number_AN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Association Number (AN)']))

    @property
    def Short_Length_SL(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Short Length (SL)']))

    @property
    def Packet_Number_PN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Packet Number (PN)']))

    @property
    def Secure_Channel_Identifier_SCI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Secure Channel Identifier (SCI)']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
