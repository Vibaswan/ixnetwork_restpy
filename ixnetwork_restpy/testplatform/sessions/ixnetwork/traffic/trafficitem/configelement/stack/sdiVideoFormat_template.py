from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SDI_Video_Format(Base):
    __slots__ = ()
    _SDM_NAME = 'sdiVideoFormat'
    _SDM_ATT_MAP = {
        'Map': 'sdiVideoFormat.sdiHeader.Map',
        'Sample': 'sdiVideoFormat.sdiHeader.sample',
        'Frame': 'sdiVideoFormat.sdiHeader.frame',
        'Frame rate': 'sdiVideoFormat.sdiHeader.frameRate',
        'Frame Count': 'sdiVideoFormat.sdiHeader.frameCount',
    }

    def __init__(self, parent):
        super(SDI_Video_Format, self).__init__(parent)

    @property
    def Map(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Map']))

    @property
    def Sample(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sample']))

    @property
    def Frame(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frame']))

    @property
    def Frame_rate(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frame rate']))

    @property
    def Frame_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frame Count']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
