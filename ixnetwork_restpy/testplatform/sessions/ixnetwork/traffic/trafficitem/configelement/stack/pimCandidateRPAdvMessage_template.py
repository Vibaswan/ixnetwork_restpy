from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PIM_Candidate_RP_Adv_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'pimCandidateRPAdvMessage'
    _SDM_ATT_MAP = {
        'Version': 'pimCandidateRPAdvMessage.header.version',
        'Type': 'pimCandidateRPAdvMessage.header.type',
        'Reserved': 'pimCandidateRPAdvMessage.header.reserved',
        'Checksum': 'pimCandidateRPAdvMessage.header.checksum',
        'Prefix-Cnt': 'pimCandidateRPAdvMessage.header.prefixCnt',
        'Priority': 'pimCandidateRPAdvMessage.header.priority',
        'HoldTime': 'pimCandidateRPAdvMessage.header.holdTime',
        'Encoded-Unicast-RP-Address': 'pimCandidateRPAdvMessage.header.encodedUnicastRPAddress',
        'Encoded-Group Address': 'pimCandidateRPAdvMessage.header.encodedGroupAddress',
    }

    def __init__(self, parent):
        super(PIM_Candidate_RP_Adv_Message, self).__init__(parent)

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
    def Prefix_Cnt(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Prefix-Cnt']))

    @property
    def Priority(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    @property
    def HoldTime(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HoldTime']))

    @property
    def Encoded_Unicast_RP_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encoded-Unicast-RP-Address']))

    @property
    def Encoded_Group_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encoded-Group Address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
