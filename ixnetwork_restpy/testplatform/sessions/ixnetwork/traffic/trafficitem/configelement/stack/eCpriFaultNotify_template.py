from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Fault_Notify(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriFaultNotify'
    _SDM_ATT_MAP = {
        'elementId': 'eCpriFaultNotify.header.elementId',
        'raiseCease': 'eCpriFaultNotify.header.raiseCease',
        'faultNotifNum': 'eCpriFaultNotify.header.faultNotifNum',
        'addInfo': 'eCpriFaultNotify.header.addInfo',
    }

    def __init__(self, parent):
        super(eCPRI_Fault_Notify, self).__init__(parent)

    @property
    def elementId(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['elementId']))

    @property
    def raiseCease(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['raiseCease']))

    @property
    def faultNotifNum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['faultNotifNum']))

    @property
    def addInfo(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['addInfo']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
