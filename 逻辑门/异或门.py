from 基本逻辑门修改 import BinaryGate, AndGate, OrGate, NotGate


class XorGate(BinaryGate):
    def __init__(self, lbl, pin_a, pin_b):
        super().__init__(lbl, pin_a, pin_b)
        self.ag_1 = AndGate("AndGate1")  # A & NOT B
        self.ag_2 = AndGate("AndGate2")  # NOT A & B
        self.og = OrGate("OrGate")       # 连接两个与门的结果
        self.ng_a = NotGate("NotGateA")  # NOT A
        self.ng_b = NotGate("NotGateB")  # NOT B

    def perform_gate_logic(self):
        self.ng_a.import_pin(self.pin_a)
        a_ = self.ng_a.get_output()
        self.ng_b.import_pin(self.pin_b)
        b_ = self.ng_b.get_output()

        self.ag_1.import_pin_a(self.pin_a)
        self.ag_1.import_pin_b(b_)
        result_1 = self.ag_1.get_output()

        self.ag_2.import_pin_a(a_)
        self.ag_2.import_pin_b(self.pin_b)
        result_2 = self.ag_2.get_output()

        self.og.import_pin_a(result_1)
        self.og.import_pin_b(result_2)

        return self.og.perform_gate_logic()



if __name__ == "__main__":
    xorgate =XorGate("XorGate",0,1)
    print(xorgate.get_output())
    xorgate.import_pin_b(0)
    print(xorgate.get_output())

