from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class JPEG_Video_Format(Base):
    __slots__ = ()
    _SDM_NAME = 'jpegVideoFormat'
    _SDM_ATT_MAP = {
        'JPEG Main Header': 'jpegVideoFormat.header.jpegMainHeader',
        'JPEG Payload Data': 'jpegVideoFormat.header.jpegPayloadData',
    }

    def __init__(self, parent):
        super(JPEG_Video_Format, self).__init__(parent)

    @property
    def JPEG_Main_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JPEG Main Header']))

    @property
    def JPEG_Payload_Data(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JPEG Payload Data']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
