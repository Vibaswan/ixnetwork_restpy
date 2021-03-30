from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Msg_Type_Remote_Memory_Access4(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType4'
    _SDM_ATT_MAP = {
        'rmaid': 'eCpriMsgType4.header.rmaid',
        'rdwr': 'eCpriMsgType4.header.rdwr',
        'reqresp': 'eCpriMsgType4.header.reqresp',
        'elemid': 'eCpriMsgType4.header.elemid',
        'address': 'eCpriMsgType4.header.address',
        'memorylength': 'eCpriMsgType4.header.',
    }

    def __init__(self, parent):
        super(eCPRI_Msg_Type_Remote_Memory_Access4, self).__init__(parent)

    @property
    def rmaid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['rmaid']))

    @property
    def rdwr(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['rdwr']))

    @property
    def reqresp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['reqresp']))

    @property
    def elemid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['elemid']))

    @property
    def address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['address']))

    @property
    def memorylength(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['memorylength']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
