class AdvancedCalculator:
    def __init__(self, channel, reflector):
        reflector.load_protocols(channel, symbols=["calculator.AdvancedCalculator"])
        stub_class = reflector.service_stub_class("calculator.AdvancedCalculator")
        self.complex_arithmetic_op_arguments = reflector.message_class("calculator.ComplexArithmeticOpArguments")
        self.stub = stub_class(channel)

    def complex_operation(self, op_type, args):
        try:
            print(self.stub.ComplexOperation(self.complex_arithmetic_op_arguments(optype=op_type, args=args)))
        except Exception as e:
            print(e)