package main.server.control;

import Home.Connection;
import Home.ConnectionI;
import Home.DeviceName;
import com.zeroc.Ice.Current;
import com.zeroc.Ice.InputStream;
import com.zeroc.Ice.OutputStream;
import com.zeroc.Ice.UserException;
import com.zeroc.IceInternal.Incoming;

import java.util.*;
import java.util.concurrent.CompletionStage;


public class ConnectionAdapter extends Connection implements ConnectionI {

    public ConnectionAdapter() {
    }

    @Override
    public void ping(String[] devices, Current current) {
        System.out.println(Arrays.toString(devices));
    }


    @Override
    public String[] ice_ids(Current current) {
        return ConnectionI.super.ice_ids(current);
    }

    @Override
    public String ice_id(Current current) {
        return ConnectionI.super.ice_id(current);
    }

    @Override
    public CompletionStage<OutputStream> _iceDispatch(Incoming in, Current current) throws UserException {
        return ConnectionI.super._iceDispatch(in, current);
    }

    @Override
    public void _iceWriteImpl(OutputStream ostr) {
        ConnectionI.super._iceWriteImpl(ostr);
    }

    @Override
    public void _iceReadImpl(InputStream istr) {
        ConnectionI.super._iceReadImpl(istr);
    }
}
