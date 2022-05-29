package grpc.server;

import io.grpc.stub.StreamObserver;
import sr.grpc.gen.ArithmeticOpArguments;
import sr.grpc.gen.ArithmeticOpResult;
import sr.grpc.gen.CalculatorGrpc;

public class CalculatorImpl extends CalculatorGrpc.CalculatorImplBase
{
	@Override
	public void add(ArithmeticOpArguments request,
					StreamObserver<ArithmeticOpResult> responseObserver)
	{
		System.out.println("addRequest (" + request.getArg1() + ", " + request.getArg2() +")");
		int val = request.getArg1() + request.getArg2();
		ArithmeticOpResult result = ArithmeticOpResult.newBuilder().setRes(val).build();
		if(request.getArg1() > 100 && request.getArg2() > 100) try { Thread.sleep(5000); } catch(java.lang.InterruptedException ex) { }
		responseObserver.onNext(result);
		responseObserver.onCompleted();
	}

	@Override
	public void subtract(ArithmeticOpArguments request,
			StreamObserver<ArithmeticOpResult> responseObserver)
	{
		System.out.println("subtractRequest (" + request.getArg1() + ", " + request.getArg2() +")");

		responseObserver.onError(io.grpc.Status.INVALID_ARGUMENT.withDescription("Bad arguments").asRuntimeException());

		int val = request.getArg1() - request.getArg2();
		ArithmeticOpResult result = ArithmeticOpResult.newBuilder().setRes(val).build();
		responseObserver.onNext(result);
		responseObserver.onCompleted();
	}


}
