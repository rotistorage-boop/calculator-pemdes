import math


class Calculator:
    """Logika operasi matematika untuk kalkulator."""

    def __init__(self):
        self.reset()

    def reset(self):
        """Reset semua state kalkulator."""
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.should_reset = False

    def input_number(self, num: str) -> str:
        """Masukkan angka ke kalkulator."""
        if self.should_reset:
            self.current = num
            self.should_reset = False
        elif self.current == "0":
            self.current = num
        else:
            self.current += num
        return self.current

    def input_operator(self, op: str) -> str:
        """Masukkan operator (+, -, *, /)."""
        if self.operator and not self.should_reset:
            self.calculate()
        self.previous = self.current
        self.operator = op
        self.should_reset = True
        return self.current

    def calculate(self) -> str:
        """Hitung hasil operasi."""
        if not self.operator or not self.previous:
            return self.current

        try:
            a = float(self.previous)
            b = float(self.current)

            if self.operator == "+":
                result = a + b
            elif self.operator == "-":
                result = a - b
            elif self.operator == "*":
                result = a * b
            elif self.operator == "/":
                if b == 0:
                    self.reset()
                    return "Error"
                result = a / b
            else:
                return self.current

            self.current = self._format(result)
            self.previous = ""
            self.operator = ""
            self.should_reset = True
            return self.current
        except Exception:
            self.reset()
            return "Error"

    def square_root(self) -> str:
        """Hitung akar kuadrat (√x)."""
        try:
            val = float(self.current)
            if val < 0:
                self.reset()
                return "Error"
            result = math.sqrt(val)
            self.current = self._format(result)
            self.should_reset = True
            return self.current
        except Exception:
            self.reset()
            return "Error"

    def square(self) -> str:
        """Hitung kuadrat (x²)."""
        try:
            val = float(self.current)
            result = val ** 2
            self.current = self._format(result)
            self.should_reset = True
            return self.current
        except Exception:
            self.reset()
            return "Error"

    def reciprocal(self) -> str:
        """Hitung kebalikan (1/x)."""
        try:
            val = float(self.current)
            if val == 0:
                self.reset()
                return "Error"
            result = 1 / val
            self.current = self._format(result)
            self.should_reset = True
            return self.current
        except Exception:
            self.reset()
            return "Error"

    def clear(self) -> str:
        """Clear kalkulator."""
        self.reset()
        return "0"

    @staticmethod
    def _format(result: float) -> str:
        """Format angka: hilangkan .0 jika bilangan bulat."""
        if result == int(result):
            return str(int(result))
        return str(round(result, 10))
