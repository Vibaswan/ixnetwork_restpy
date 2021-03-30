from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class H264_Specific_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'h264_sh'
    _SDM_ATT_MAP = {
        'F': 'h264SH.h264SpecificHeader.F',
        'NRI': 'h264SH.h264SpecificHeader.NRI',
        'NAL Unit Type': 'h264SH.h264SpecificHeader.nalUnitType',
        'Length': 'h264SH.h264SpecificHeader.length',
        'RAW Byte Sequence Payload': 'h264SH.h264SpecificHeader.rawPayload',
        'Padding': 'h264SH.h264SpecificHeader.Padding',
    }

    def __init__(self, parent):
        super(H264_Specific_Header, self).__init__(parent)

    @property
    def F(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['F']))

    @property
    def NRI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NRI']))

    @property
    def NAL_Unit_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NAL Unit Type']))

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def RAW_Byte_Sequence_Payload(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RAW Byte Sequence Payload']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
