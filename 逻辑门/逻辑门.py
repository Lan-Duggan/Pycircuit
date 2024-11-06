class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            return self.get_input(f"Enter pin A input for gate {self.get_label()}:")
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b is None:
            return self.get_input(f"Enter pin B input for gate {self.get_label()}:")
        else:
            return self.pin_b.get_from().get_output()

    def get_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value in (0, 1):
                    return value
                else:
                    print("Please enter 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter an integer (0 or 1).")

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            raise RuntimeError("Error: No EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return self.get_input(f"Enter pin input for gate {self.get_label()}:")
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        self.pin = source


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
        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(f"Output of gate {g4.get_label()}: {g4.get_output()}")
