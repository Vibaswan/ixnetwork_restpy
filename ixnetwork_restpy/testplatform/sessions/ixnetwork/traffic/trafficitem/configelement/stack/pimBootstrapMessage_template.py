from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PIM_Bootstrap_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'pimBootstrapMessage'
    _SDM_ATT_MAP = {
        'Version': 'pimBootstrapMessage.header.version',
        'Type': 'pimBootstrapMessage.header.type',
        'Reserved': 'pimBootstrapMessage.header.reserved',
        'Checksum': 'pimBootstrapMessage.header.checksum',
        'Fragment Tag': 'pimBootstrapMessage.header.fragmentTag',
        'Hash Mask Len': 'pimBootstrapMessage.header.hashMaskLen',
        'BSR-priority': 'pimBootstrapMessage.header.bsrpriority',
        'Encoded-Unicast-BSR-Address': 'pimBootstrapMessage.header.encodedUnicastBSRAddress',
        'Encoded-Group Address Fields': 'pimBootstrapMessage.header.encodedGroupAddressFields',
    }

    def __init__(self, parent):
        super(PIM_Bootstrap_Message, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Fragment_Tag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Fragment Tag']))

    @property
    def Hash_Mask_Len(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hash Mask Len']))

    @property
    def BSR_priority(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BSR-priority']))

    @property
    def Encoded_Unicast_BSR_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encoded-Unicast-BSR-Address']))

    @property
    def Encoded_Group_Address_Fields(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encoded-Group Address Fields']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
