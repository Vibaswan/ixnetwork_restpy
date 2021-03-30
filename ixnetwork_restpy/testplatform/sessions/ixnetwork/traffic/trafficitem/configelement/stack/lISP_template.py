from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISP(Base):
    __slots__ = ()
    _SDM_NAME = 'lISP'
    _SDM_ATT_MAP = {
        'nonce-present-bit': 'lISP.header.nonce-present-bit',
        'locator-status-bit': 'lISP.header.locator-status-bit',
        'echo-nonce-request-bit': 'lISP.header.echo-nonce-request-bit',
        'map-version-present-bit': 'lISP.header.map-version-present-bit',
        'instance-id-bit': 'lISP.header.instance-id-bit',
        'Flags': 'lISP.header.flags',
        'Nonce/Map-Version': 'lISP.header.nonce-map-version',
        'Instance ID/Locator Status Bits': 'lISP.header.instance-id-locator-sstatus-bits',
    }

    def __init__(self, parent):
        super(LISP, self).__init__(parent)

    @property
    def nonce_present_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['nonce-present-bit']))

    @property
    def locator_status_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['locator-status-bit']))

    @property
    def echo_nonce_request_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['echo-nonce-request-bit']))

    @property
    def map_version_present_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['map-version-present-bit']))

    @property
    def instance_id_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['instance-id-bit']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Nonce_Map_Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Nonce/Map-Version']))

    @property
    def Instance_ID_Locator_Status_Bits(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Instance ID/Locator Status Bits']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
