//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.3
//
// <auto-generated>
//
// Generated from file `home.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Home;

public interface BulbulatorDisp extends DeviceDisp,
                                        BulbulatorI
{
    /** @hidden */
    static final String[] _iceIds =
    {
        "::Home::Bulbulator",
        "::Home::BulbulatorI",
        "::Home::Device",
        "::Home::DeviceI",
        "::Ice::Object"
    };

    @Override
    default String[] ice_ids(com.zeroc.Ice.Current current)
    {
        return _iceIds;
    }

    @Override
    default String ice_id(com.zeroc.Ice.Current current)
    {
        return ice_staticId();
    }

    static String ice_staticId()
    {
        return Bulbulator.ice_staticId();
    }

    /** @hidden */
    final static String[] _iceOps =
    {
        "getDeviceParameters",
        "ice_id",
        "ice_ids",
        "ice_isA",
        "ice_ping",
        "isBulbulatorSaturator",
        "makeNoise",
        "setParameters",
        "turnDeviceOff",
        "turnDeviceOn"
    };

    /** @hidden */
    @Override
    default java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceDispatch(com.zeroc.IceInternal.Incoming in, com.zeroc.Ice.Current current)
        throws com.zeroc.Ice.UserException
    {
        int pos = java.util.Arrays.binarySearch(_iceOps, current.operation);
        if(pos < 0)
        {
            throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
        }

        switch(pos)
        {
            case 0:
            {
                return DeviceI._iceD_getDeviceParameters(this, in, current);
            }
            case 1:
            {
                return com.zeroc.Ice.Object._iceD_ice_id(this, in, current);
            }
            case 2:
            {
                return com.zeroc.Ice.Object._iceD_ice_ids(this, in, current);
            }
            case 3:
            {
                return com.zeroc.Ice.Object._iceD_ice_isA(this, in, current);
            }
            case 4:
            {
                return com.zeroc.Ice.Object._iceD_ice_ping(this, in, current);
            }
            case 5:
            {
                return BulbulatorI._iceD_isBulbulatorSaturator(this, in, current);
            }
            case 6:
            {
                return BulbulatorI._iceD_makeNoise(this, in, current);
            }
            case 7:
            {
                return DeviceI._iceD_setParameters(this, in, current);
            }
            case 8:
            {
                return DeviceI._iceD_turnDeviceOff(this, in, current);
            }
            case 9:
            {
                return DeviceI._iceD_turnDeviceOn(this, in, current);
            }
        }

        assert(false);
        throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
    }
}
