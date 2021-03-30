from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class STP_Configuration_BPDU(Base):
    __slots__ = ()
    _SDM_NAME = 'stpCfgBPDU'
    _SDM_ATT_MAP = {
        'Protocol identifier': 'stpCfgBPDU.header.protocolIdentifier',
        'Protocol version identifier': 'stpCfgBPDU.header.protocolVersionIdentifier',
        'BPDU type': 'stpCfgBPDU.header.bpduType',
        'Flags': 'stpCfgBPDU.header.flags',
        'Root identifier': 'stpCfgBPDU.header.rootIdentifier',
        'Root path cost': 'stpCfgBPDU.header.rootPathCost',
        'Bridge identifier': 'stpCfgBPDU.header.bridgeIdentifier',
        'Port identifier': 'stpCfgBPDU.header.portIdentifier',
        'Message age': 'stpCfgBPDU.header.messageAge',
        'Max age': 'stpCfgBPDU.header.maxAge',
        'Hello time': 'stpCfgBPDU.header.helloTime',
        'Forward delay': 'stpCfgBPDU.header.forwardDelay',
    }

    def __init__(self, parent):
        super(STP_Configuration_BPDU, self).__init__(parent)

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
    def Root_path_cost(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Root path cost']))

    @property
    def Bridge_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bridge identifier']))

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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
