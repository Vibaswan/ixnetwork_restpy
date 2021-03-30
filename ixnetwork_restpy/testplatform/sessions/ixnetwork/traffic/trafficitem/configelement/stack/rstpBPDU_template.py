from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RSTP_BPDU(Base):
    __slots__ = ()
    _SDM_NAME = 'rstpBPDU'
    _SDM_ATT_MAP = {
        'Protocol identifier': 'rstpBPDU.header.protocolIdentifier',
        'Protocol version identifier': 'rstpBPDU.header.protocolVersionIdentifier',
        'BPDU type': 'rstpBPDU.header.bpduType',
        'Flags': 'rstpBPDU.header.flags',
        'Root identifier': 'rstpBPDU.header.rootIdentifier',
        'External root path cost': 'rstpBPDU.header.externalRootPathCost',
        'Regional root identifier': 'rstpBPDU.header.regionalRootIdentifier',
        'Port identifier': 'rstpBPDU.header.portIdentifier',
        'Message age': 'rstpBPDU.header.messageAge',
        'Max age': 'rstpBPDU.header.maxAge',
        'Hello time': 'rstpBPDU.header.helloTime',
        'Forward delay': 'rstpBPDU.header.forwardDelay',
        'Version 1 Length': 'rstpBPDU.header.version1Length',
    }

    def __init__(self, parent):
        super(RSTP_BPDU, self).__init__(parent)

    @property
    def Protocol_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol identifier']))

    @property
    def Protocol_version_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol version identifier']))

    @property
    def BPDU_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BPDU type']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Root_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Root identifier']))

    @property
    def External_root_path_cost(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['External root path cost']))

    @property
    def Regional_root_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Regional root identifier']))

    @property
    def Port_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Port identifier']))

    @property
    def Message_age(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message age']))

    @property
    def Max_age(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Max age']))

    @property
    def Hello_time(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hello time']))

    @property
    def Forward_delay(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Forward delay']))

    @property
    def Version_1_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version 1 Length']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
