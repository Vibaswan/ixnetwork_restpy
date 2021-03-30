from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MACsec_HW(Base):
    __slots__ = ()
    _SDM_NAME = 'macsecHw'
    _SDM_ATT_MAP = {
        'Metadata': 'MacsecHw.secTag.metadata',
        'TCI (TAG Control Information)': 'MacsecHw.secTag.tci',
        'Association Number (AN)': 'MacsecHw.secTag.an',
        'Short Length (SL)': 'MacsecHw.secTag.sl',
        'Packet Number (PN)': 'MacsecHw.secTag.pn',
        'Secure Channel Identifier (SCI)': 'MacsecHw.secTag.sci',
    }

    def __init__(self, parent):
        super(MACsec_HW, self).__init__(parent)

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
