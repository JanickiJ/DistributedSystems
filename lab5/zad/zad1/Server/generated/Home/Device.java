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

public class Device extends com.zeroc.Ice.Value
{
    public Device()
    {
        this.name = "";
        this.type = DeviceType.OVEN;
    }

    public Device(String name, DeviceType type, boolean isOn)
    {
        this.name = name;
        this.type = type;
        this.isOn = isOn;
    }

    public String name;

    public DeviceType type;

    public boolean isOn;

    public Device clone()
    {
        return (Device)super.clone();
    }

    public static String ice_staticId()
    {
        return "::Home::Device";
    }

    @Override
    public String ice_id()
    {
        return ice_staticId();
    }

    /** @hidden */
    public static final long serialVersionUID = 7635086845827812165L;

    /** @hidden */
    @Override
    protected void _iceWriteImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice(ice_staticId(), -1, true);
        ostr_.writeString(name);
        DeviceType.ice_write(ostr_, type);
        ostr_.writeBool(isOn);
        ostr_.endSlice();
    }

    /** @hidden */
    @Override
    protected void _iceReadImpl(com.zeroc.Ice.InputStream istr_)
    {
        istr_.startSlice();
        name = istr_.readString();
        type = DeviceType.ice_read(istr_);
        isOn = istr_.readBool();
        istr_.endSlice();
    }
}
