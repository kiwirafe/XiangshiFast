from XiangshiFast.main import CalculatorFast

calculator = CalculatorFast()
for x in dir(calculator):
    if x[:2] != "__":
        exec(x + "=" + "calculator." + x)
