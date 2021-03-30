from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class E_LMI(Base):
    __slots__ = ()
    _SDM_NAME = 'elmi'
    _SDM_ATT_MAP = {
        'Protocol Version': 'elmi.elmiHeader.protoVersion',
        'Message Type': 'elmi.elmiHeader.msgType',
        'Select Information Element': 'elmi.elmiHeader.selectInformationElement',
    }

    def __init__(self, parent):
        super(E_LMI, self).__init__(parent)

    @property
    def Protocol_Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Version']))

    @property
    def Message_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Type']))

    @property
    def Select_Information_Element(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Select Information Element']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
