class Calculator:
    def __init__(self, channel, reflector):
        reflector.load_protocols(channel, symbols=["calculator.Calculator"])
        stub_class = reflector.service_stub_class("calculator.Calculator")
        self.arithmetic_op_result_message = reflector.message_class("calculator.ArithmeticOpArguments")
        self.stub = stub_class(channel)

    def add(self, arg1, arg2):
        try:
            print(self.stub.Add(self.arithmetic_op_result_message(arg1=arg1, arg2=arg2)))
        except Exception as e:
            print(e)

    def subtract(self, arg1, arg2):
        try:
            print(self.stub.Subtract(self.arithmetic_op_result_message(arg1=arg1, arg2=arg2)))
        except Exception as e:
            print(e)
