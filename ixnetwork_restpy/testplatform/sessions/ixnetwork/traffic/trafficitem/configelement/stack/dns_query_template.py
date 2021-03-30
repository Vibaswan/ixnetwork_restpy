from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DNS_Query(Base):
    __slots__ = ()
    _SDM_NAME = 'dns_query'
    _SDM_ATT_MAP = {
        'Transaction ID': 'dns_query.header.tid',
        'Flags': 'dns_query.header.dnsflags',
        'Query Count': 'dns_query.header.QCount',
        'Answer Count': 'dns_query.header.ACount',
        'Authority Count': 'dns_query.header.AuthCount',
        'Additional Info Count': 'dns_query.header.InfoCount',
        'Queries': 'dns_query.header.queries',
    }

    def __init__(self, parent):
        super(DNS_Query, self).__init__(parent)

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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
