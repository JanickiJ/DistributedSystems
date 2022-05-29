class Stream:
    def __init__(self, channel, reflector):
        reflector.load_protocols(channel, symbols=["streaming.StreamTester"])
        stub_class = reflector.service_stub_class("streaming.StreamTester")
        self.number = reflector.message_class("streaming.Number")
        self.task = reflector.message_class("streaming.Task")
        self.stub = stub_class(channel)

    def generate_prime_numbers(self, arg):
        try:
            for i in self.stub.GeneratePrimeNumbers(self.task(max=arg)):
                print(i)
        except Exception as e:
            print(e)

    def count_prime_numbers(self, args):
        def prime_numbers_generator(args):
            for i in args:
                yield self.number(value=i)

        try:
            print(self.stub.CountPrimeNumbers(prime_numbers_generator(args)))
        except Exception as e:
            print(e)