from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class INT_Probe_Marker(Base):
    __slots__ = ()
    _SDM_NAME = 'intprobemarker'
    _SDM_ATT_MAP = {
        'INT Probe Marker': 'probemarker.header.pm',
    }

    def __init__(self, parent):
        super(INT_Probe_Marker, self).__init__(parent)

    @property
    def INT_Probe_Marker(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['INT Probe Marker']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
