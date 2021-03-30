from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RSVP(Base):
    __slots__ = ()
    _SDM_NAME = 'rsvp'
    _SDM_ATT_MAP = {
        'Version': 'rsvp.rsvpMessege.version',
        'Flag': 'rsvp.rsvpMessege.flag',
        'Messege Type': 'rsvp.rsvpMessege.messegeType',
        'RSVP checksum': 'rsvp.rsvpMessege.rsvpChecksum',
        'TTL': 'rsvp.rsvpMessege.ttl',
        'Reserved': 'rsvp.rsvpMessege.reserved',
        'RSVP Length': 'rsvp.rsvpMessege.rsvpLength',
        'Objects': 'rsvp.rsvpMessege.objects',
    }

    def __init__(self, parent):
        super(RSVP, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Flag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flag']))

    @property
    def Messege_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Messege Type']))

    @property
    def RSVP_checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RSVP checksum']))

    @property
    def TTL(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TTL']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def RSVP_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RSVP Length']))

    @property
    def Objects(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Objects']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
