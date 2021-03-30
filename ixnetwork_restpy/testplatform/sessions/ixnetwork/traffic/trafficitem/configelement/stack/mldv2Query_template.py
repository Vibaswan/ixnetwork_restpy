from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MLDv2_Query(Base):
    __slots__ = ()
    _SDM_NAME = 'mldv2Query'
    _SDM_ATT_MAP = {
        'Type': 'mldv2Query.mldv2ListenerQuery.type',
        'Code': 'mldv2Query.mldv2ListenerQuery.code',
        'MLDv2 checksum': 'mldv2Query.mldv2ListenerQuery.mldv2Checksum',
        'Maximum response code': 'mldv2Query.mldv2ListenerQuery.maximumResponseCode',
        'Reserved': 'mldv2Query.mldv2ListenerQuery.reserved',
        'Multicast address': 'mldv2Query.mldv2ListenerQuery.multicastAddress',
        'Resv': 'mldv2Query.mldv2ListenerQuery.resv',
        'S Flag': 'mldv2Query.mldv2ListenerQuery.sFlag',
        'QRV': 'mldv2Query.mldv2ListenerQuery.qrv',
        'QQIC': 'mldv2Query.mldv2ListenerQuery.qqic',
        'Number of Sources': 'mldv2Query.mldv2ListenerQuery.numberOfSources',
        'SourceAddress Entries': 'mldv2Query.mldv2ListenerQuery.sourceAddressEntries',
    }

    def __init__(self, parent):
        super(MLDv2_Query, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Code']))

    @property
    def MLDv2_checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MLDv2 checksum']))

    @property
    def Maximum_response_code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Maximum response code']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Multicast_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Multicast address']))

    @property
    def Resv(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Resv']))

    @property
    def S_Flag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['S Flag']))

    @property
    def QRV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['QRV']))

    @property
    def QQIC(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['QQIC']))

    @property
    def Number_of_Sources(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Number of Sources']))

    @property
    def SourceAddress_Entries(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddress Entries']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
