from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DNS_Response(Base):
    __slots__ = ()
    _SDM_NAME = 'dns_response'
    _SDM_ATT_MAP = {
        'Transaction ID': 'dns_response.header.tid',
        'Flags': 'dns_response.header.dnsflags',
        'Query Count': 'dns_response.header.QCount',
        'Answer Count': 'dns_response.header.ACount',
        'Authority Count': 'dns_response.header.AuthCount',
        'Additional Info Count': 'dns_response.header.InfoCount',
        'Queries': 'dns_response.header.queries',
        'RR Type': 'dns_response.header.rrtype',
    }

    def __init__(self, parent):
        super(DNS_Response, self).__init__(parent)

    @property
    def Transaction_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Transaction ID']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Query_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Query Count']))

    @property
    def Answer_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Answer Count']))

    @property
    def Authority_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authority Count']))

    @property
    def Additional_Info_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Additional Info Count']))

    @property
    def Queries(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Queries']))

    @property
    def RR_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RR Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
