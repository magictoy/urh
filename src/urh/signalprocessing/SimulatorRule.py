from enum import Enum

from urh.signalprocessing.SimulatorItem import SimulatorItem
from urh.signalprocessing.SimulatorRuleset import SimulatorRuleset

class SimulatorRule(SimulatorItem):
    def __init__(self):
        super().__init__()

    def set_parent(self, value):
        if value is not None:
            assert value.parent() is None

        super().set_parent(value)

    def has_else_condition(self):
        return len([child for child in self.children if child.type is ConditionType.ELSE]) == 1

class ConditionType(Enum):
    IF = "if ..."
    ELSE_IF = "else if ..."
    ELSE = "else"

class SimulatorRuleCondition(SimulatorItem):
    def __init__(self, type: ConditionType):
        super().__init__()
        self.type = type
        self.ruleset = SimulatorRuleset()

    def set_parent(self, value):
        if value is not None:
            assert isinstance(value, SimulatorRule)

        super().set_parent(value)