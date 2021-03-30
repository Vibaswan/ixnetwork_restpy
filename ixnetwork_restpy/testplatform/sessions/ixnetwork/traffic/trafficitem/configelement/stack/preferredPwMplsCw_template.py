from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Preferred_PW_MPLS_Control_Word(Base):
    __slots__ = ()
    _SDM_NAME = 'preferredPwMplsCw'
    _SDM_ATT_MAP = {
        'CW Rsvd': 'preferedPwMPlsCw.controlWord.reserved',
        'CW Flags': 'preferedPwMPlsCw.controlWord.flags',
        'CW FRG': 'preferedPwMPlsCw.controlWord.frg',
        'CW Length': 'preferedPwMPlsCw.controlWord.length',
        'CW Sequence Number': 'preferedPwMPlsCw.controlWord.sequenceNumber',
    }

    def __init__(self, parent):
        super(Preferred_PW_MPLS_Control_Word, self).__init__(parent)

    @property
    def CW_Rsvd(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Rsvd']))

    @property
    def CW_Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Flags']))

    @property
    def CW_FRG(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW FRG']))

    @property
    def CW_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Length']))

    @property
    def CW_Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Sequence Number']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
