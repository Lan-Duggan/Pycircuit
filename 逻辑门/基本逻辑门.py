from abc import ABC, abstractmethod


class LogicGate(ABC):
    def __init__(self, lbl):
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

    # 每个逻辑门的运行逻辑
    @abstractmethod
    def perform_gate_logic(self):
        # 抽象方法，要求子类必须实现
        pass


class BinaryGate(LogicGate):

    def __init__(self, lbl, pin_a=0, pin_b=0):
        super().__init__(lbl)
        self.pin_a = pin_a
        self.pin_b = pin_b

    def import_pin_a(self, pin_a):
        self.pin_a = pin_a

    def import_pin_b(self, pin_b):
        self.pin_b = pin_b

    def get_pin_a(self):
        return self.pin_a

    def get_pin_b(self):
        return self.pin_b

    def perform_gate_logic(self):
        # 抽象方法，要求子类必须实现
        pass


class UnaryGate(LogicGate):
    def __init__(self, lbl, pin=0):
        super().__init__(lbl)
        self.pin = pin

    def import_pin(self, pin):
        self.pin =pin

    def get_pin(self):
        return self.pin

    def perform_gate_logic(self):
        # 抽象方法，要求子类必须实现
        pass


class AndGate(BinaryGate):
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return 1 if a == 1 and b == 1 else 0


class OrGate(BinaryGate):
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return 1 if a == 1 or b == 1 else 0


class NotGate(UnaryGate):
    def perform_gate_logic(self):
        pin = self.get_pin()
        return 0 if pin == 1 else 1


class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_next_pin(self.from_gate.get_output())  # 将信号传递给目标门

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


if __name__ == "__main__":
    # 创建门
    g1 = AndGate("G1", 1, )
    g1.import_pin_b(1)
    g2 = OrGate("G2", 0, 1)
    g3 = NotGate("G3", 1)

    print(g1.get_output())

