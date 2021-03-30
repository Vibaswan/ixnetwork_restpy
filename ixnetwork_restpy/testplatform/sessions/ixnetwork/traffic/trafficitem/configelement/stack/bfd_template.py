from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BFD_Bidirectional_Forwarding_Detection(Base):
    __slots__ = ()
    _SDM_NAME = 'bfd'
    _SDM_ATT_MAP = {
        'Version': 'bfd.header.version',
        'Diagnostic': 'bfd.header.diagnostic',
        'State': 'bfd.header.state',
        'Poll (P)': 'bfd.header.pollP',
        'Final (F)': 'bfd.header.finalF',
        'Control plane independent (C)': 'bfd.header.controlPlaneIndependentC',
        'Authentication (A)': 'bfd.header.authenticationA',
        'Demand (D)': 'bfd.header.demandD',
        'Reserved': 'bfd.header.reserved',
        'Detect time multiplier': 'bfd.header.detectTimeMultiplier',
        'Length': 'bfd.header.length',
        'My discriminator': 'bfd.header.myDiscriminator',
        'Your discriminator': 'bfd.header.yourDiscriminator',
        'Desired min TX interval': 'bfd.header.desiredMinTXInterval',
        'Required min RX interval': 'bfd.header.requiredMinRXInterval',
        'Required min echo RX interval': 'bfd.header.requiredMinEchoRXInterval',
        'Authentication Option': 'bfd.header.authenticationOption',
    }

    def __init__(self, parent):
        super(BFD_Bidirectional_Forwarding_Detection, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Diagnostic(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Diagnostic']))

    @property
    def State(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['State']))

    @property
    def Poll_P(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Poll (P)']))

    @property
    def Final_F(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Final (F)']))

    @property
    def Control_plane_independent_C(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Control plane independent (C)']))

    @property
    def Authentication_A(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authentication (A)']))

    @property
    def Demand_D(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Demand (D)']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Detect_time_multiplier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Detect time multiplier']))

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def My_discriminator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['My discriminator']))

    @property
    def Your_discriminator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Your discriminator']))

    @property
    def Desired_min_TX_interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Desired min TX interval']))

    @property
    def Required_min_RX_interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Required min RX interval']))

    @property
    def Required_min_echo_RX_interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Required min echo RX interval']))

    @property
    def Authentication_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authentication Option']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
