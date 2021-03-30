from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IxP4_P4CALC(Base):
    __slots__ = ()
    _SDM_NAME = 'ixP4_P4CALC'
    _SDM_ATT_MAP = {
        'protocol_type': 'ixP4_P4CALC.p4CALC.protocol_type',
        'protocol_subtype': 'ixP4_P4CALC.p4CALC.protocol_subtype',
        'version': 'ixP4_P4CALC.p4CALC.version',
        'operator': 'ixP4_P4CALC.p4CALC.operator',
        'left_operand': 'ixP4_P4CALC.p4CALC.left_operand',
        'right_operand': 'ixP4_P4CALC.p4CALC.right_operand',
        'result': 'ixP4_P4CALC.p4CALC.result',
    }

    def __init__(self, parent):
        super(IxP4_P4CALC, self).__init__(parent)

    @property
    def protocol_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['protocol_type']))

    @property
    def protocol_subtype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['protocol_subtype']))

    @property
    def version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['version']))

    @property
    def operator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['operator']))

    @property
    def left_operand(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['left_operand']))

    @property
    def right_operand(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['right_operand']))

    @property
    def result(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['result']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
