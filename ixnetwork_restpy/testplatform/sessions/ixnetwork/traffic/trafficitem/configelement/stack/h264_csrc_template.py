from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class H264_CSRC(Base):
    __slots__ = ()
    _SDM_NAME = 'h264_csrc'
    _SDM_ATT_MAP = {
        'CSRC': 'h264_csrc.header.csrcList',
    }

    def __init__(self, parent):
        super(H264_CSRC, self).__init__(parent)

    @property
    def CSRC(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CSRC']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
