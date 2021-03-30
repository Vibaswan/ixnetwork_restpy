from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MSTP_BPDU(Base):
    __slots__ = ()
    _SDM_NAME = 'mstpBPDU'
    _SDM_ATT_MAP = {
        'Protocol identifier': 'mstpBPDU.header.protocolIdentifier',
        'Protocol version identifier': 'mstpBPDU.header.protocolVersionIdentifier',
        'BPDU type': 'mstpBPDU.header.bpduType',
        'CIST Flags': 'mstpBPDU.header.cistFlags',
        'CIST root identifier': 'mstpBPDU.header.cistRootIdentifier',
        'CIST external path cost': 'mstpBPDU.header.cistExternalPathCost',
        'CIST regional root identifier': 'mstpBPDU.header.cistRegionalRootIdentifier',
        'CIST port identifier': 'mstpBPDU.header.cistPortIdentifier',
        'Message age': 'mstpBPDU.header.messageAge',
        'Max age(in msecs)': 'mstpBPDU.header.maxAgeinMsecs',
        'Hello time(in msecs)': 'mstpBPDU.header.helloTimeinMsecs',
        'Forward delay(in msecs)': 'mstpBPDU.header.forwardDelayinMsecs',
        'Version 1 Length': 'mstpBPDU.header.version1Length',
        'Version 3 length(in octets)': 'mstpBPDU.header.version3LengthinOctets',
        'MSTI configuration identifier': 'mstpBPDU.header.mstiConfigurationIdentifier',
        'CIST internal root path cost': 'mstpBPDU.header.cistInternalRootPathCost',
        'CIST bridge identifier': 'mstpBPDU.header.cistBridgeIdentifier',
        'CIST remaining hops': 'mstpBPDU.header.cistRemainingHops',
        'MSTI configuration message': 'mstpBPDU.header.mstiConfigurationMessage',
    }

    def __init__(self, parent):
        super(MSTP_BPDU, self).__init__(parent)

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
    def CIST_Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST Flags']))

    @property
    def CIST_root_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST root identifier']))

    @property
    def CIST_external_path_cost(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST external path cost']))

    @property
    def CIST_regional_root_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST regional root identifier']))

    @property
    def CIST_port_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST port identifier']))

    @property
    def Message_age(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message age']))

    @property
    def Max_agein_msecs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Max age(in msecs)']))

    @property
    def Hello_timein_msecs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hello time(in msecs)']))

    @property
    def Forward_delayin_msecs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Forward delay(in msecs)']))

    @property
    def Version_1_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version 1 Length']))

    @property
    def Version_3_lengthin_octets(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version 3 length(in octets)']))

    @property
    def MSTI_configuration_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MSTI configuration identifier']))

    @property
    def CIST_internal_root_path_cost(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST internal root path cost']))

    @property
    def CIST_bridge_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST bridge identifier']))

    @property
    def CIST_remaining_hops(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIST remaining hops']))

    @property
    def MSTI_configuration_message(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MSTI configuration message']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
