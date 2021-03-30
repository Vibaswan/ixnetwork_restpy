from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NTP(Base):
    __slots__ = ()
    _SDM_NAME = 'ntp'
    _SDM_ATT_MAP = {
        'NTP-Leap-Indicator': 'ntp.header.leapindicator',
        'NTP-Version': 'ntp.header.version',
        'NTP-Mode': 'ntp.header.mode',
        'NTP-Stratum': 'ntp.header.stratum',
        'NTP-Poll-interval': 'ntp.header.pollinterval',
        'NTP-Precision': 'ntp.header.precision',
        'NTP-Root-delay': 'ntp.header.rootdelay',
        'NTP-Root-dispersion': 'ntp.header.rootdispersion',
        'NTP-Reference-clock-identifier': 'ntp.header.referenceclockidentifier',
        'NTP-Reference-timestamp': 'ntp.header.referencetimestamp',
        'NTP-Originate-timestamp': 'ntp.header.originatetimestamp',
        'NTP-Receive-timestamp': 'ntp.header.receivetimestamp',
        'NTP-Transmit-timestamp': 'ntp.header.transmittimestamp',
        'NTPv4 Extension field': 'ntp.header.extension',
        'Authentication': 'ntp.header.authentication',
    }

    def __init__(self, parent):
        super(NTP, self).__init__(parent)

    @property
    def NTP_Leap_Indicator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Leap-Indicator']))

    @property
    def NTP_Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Version']))

    @property
    def NTP_Mode(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Mode']))

    @property
    def NTP_Stratum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Stratum']))

    @property
    def NTP_Poll_interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Poll-interval']))

    @property
    def NTP_Precision(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Precision']))

    @property
    def NTP_Root_delay(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Root-delay']))

    @property
    def NTP_Root_dispersion(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Root-dispersion']))

    @property
    def NTP_Reference_clock_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Reference-clock-identifier']))

    @property
    def NTP_Reference_timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Reference-timestamp']))

    @property
    def NTP_Originate_timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Originate-timestamp']))

    @property
    def NTP_Receive_timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Receive-timestamp']))

    @property
    def NTP_Transmit_timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTP-Transmit-timestamp']))

    @property
    def NTPv4_Extension_field(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NTPv4 Extension field']))

    @property
    def Authentication(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authentication']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
