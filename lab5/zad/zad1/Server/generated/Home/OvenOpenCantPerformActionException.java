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

public class OvenOpenCantPerformActionException extends InvalidParameterException
{
    public OvenOpenCantPerformActionException()
    {
        super();
    }

    public OvenOpenCantPerformActionException(Throwable cause)
    {
        super(cause);
    }

    public OvenOpenCantPerformActionException(String message)
    {
        super(message);
    }

    public OvenOpenCantPerformActionException(String message, Throwable cause)
    {
        super(message, cause);
    }

    public String ice_id()
    {
        return "::Home::OvenOpenCantPerformActionException";
    }

    /** @hidden */
    @Override
    protected void _writeImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice("::Home::OvenOpenCantPerformActionException", -1, false);
        ostr_.endSlice();
        super._writeImpl(ostr_);
    }

    /** @hidden */
    @Override
    protected void _readImpl(com.zeroc.Ice.InputStream istr_)
    {
        istr_.startSlice();
        istr_.endSlice();
        super._readImpl(istr_);
    }

    /** @hidden */
    public static final long serialVersionUID = 4648791718983551246L;
}
