from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Marker_PDU(Base):
    __slots__ = ()
    _SDM_NAME = 'markerPDU'
    _SDM_ATT_MAP = {
        'Marker Header': 'markerPDU.header.header',
        'Actor Information': 'markerPDU.header.actor',
        'Terminator': 'markerPDU.header.terminator',
        'Reserved': 'markerPDU.header.reserved',
        'Frame Check Sequence CRC-32': 'markerPDU.header.fcs',
    }

    def __init__(self, parent):
        super(Marker_PDU, self).__init__(parent)

    @property
    def Marker_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Marker Header']))

    @property
    def Actor_Information(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Actor Information']))

    @property
    def Terminator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Terminator']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Frame_Check_Sequence_CRC_32(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frame Check Sequence CRC-32']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
