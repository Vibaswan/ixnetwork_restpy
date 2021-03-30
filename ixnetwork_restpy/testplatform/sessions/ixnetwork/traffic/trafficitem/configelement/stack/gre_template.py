from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class GRE(Base):
    __slots__ = ()
    _SDM_NAME = 'gre'
    _SDM_ATT_MAP = {
        'Checksum Present': 'gre.header.checksumPresent',
        'Reserved': 'gre.header.reserved1',
        'Key Present': 'gre.header.keyPresent',
        'Sequence Number Present': 'gre.header.sequencePresent',
        'Reserved': 'gre.header.reserved2',
        'Version': 'gre.header.version',
        'Protocol': 'gre.header.protocol',
        'Checksum Option': 'gre.header.checksumHolder',
        'Key Option': 'gre.header.keyHolder',
        'Sequence Option': 'gre.header.sequenceHolder',
    }

    def __init__(self, parent):
        super(GRE, self).__init__(parent)

    @property
    def Checksum_Present(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum Present']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Key_Present(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Key Present']))

    @property
    def Sequence_Number_Present(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number Present']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Protocol(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol']))

    @property
    def Checksum_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum Option']))

    @property
    def Key_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Key Option']))

    @property
    def Sequence_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Option']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
