from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class JPEG_2000_Video_Format(Base):
    __slots__ = ()
    _SDM_NAME = 'jpeg2000VideoFormat'
    _SDM_ATT_MAP = {
        'JPEG 2000 Payload Header': 'jpeg2000VideoFormat.header.jpeg2000PayloadHeader',
        'JPEG 2000 payload': 'jpeg2000VideoFormat.header.jpeg2000Payload',
    }

    def __init__(self, parent):
        super(JPEG_2000_Video_Format, self).__init__(parent)

    @property
    def JPEG_2000_Payload_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JPEG 2000 Payload Header']))

    @property
    def JPEG_2000_payload(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JPEG 2000 payload']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
