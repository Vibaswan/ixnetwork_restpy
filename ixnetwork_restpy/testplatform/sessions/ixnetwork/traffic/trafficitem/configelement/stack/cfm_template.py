from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Connectivity_Fault_Management_CFM(Base):
    __slots__ = ()
    _SDM_NAME = 'cfm'
    _SDM_ATT_MAP = {
        'Common Header': 'cfm.cfmHeader.commonHeader',
        'Select Packet Header': 'cfm.cfmHeader.selectPacketHeader',
        'TLVs': 'cfm.cfmHeader.tlvs',
    }

    def __init__(self, parent):
        super(Connectivity_Fault_Management_CFM, self).__init__(parent)

    @property
    def Common_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Common Header']))

    @property
    def Select_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Select Packet Header']))

    @property
    def TLVs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TLVs']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
