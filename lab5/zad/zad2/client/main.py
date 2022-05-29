import grpc
from yagrc import reflector as yagrc_reflector
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from AdvancedCalculator import AdvancedCalculator
from Calculator import Calculator
from Stream import Stream

if __name__ == '__main__':
    reflector = yagrc_reflector.GrpcReflectionClient()
    with grpc.insecure_channel("127.0.0.2:50051") as channel:
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        services = reflection_db.get_services()
        print(f"Services: {services}")
        calculator = Calculator(channel, reflector)
        advanced_calculator = AdvancedCalculator(channel, reflector)
        stream = Stream(channel, reflector)
        calculator.add(10, 2)
        calculator.add(1000, 2000)
        calculator.subtract(1000, 2000)
        advanced_calculator.complex_operation(1, [1, 2, 3, 1])
        advanced_calculator.complex_operation(0, [1, 2, 3, 1])
        stream.generate_prime_numbers(8)
        stream.count_prime_numbers([i for i in range(1, 15, 2)])
