# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.3
#
# <auto-generated>
#
# Generated from file `home.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Home
_M_Home = Ice.openModule('Home')
__name__ = 'Home'

if 'DeviceType' not in _M_Home.__dict__:
    _M_Home.DeviceType = Ice.createTempClass()
    class DeviceType(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    DeviceType.OVEN = DeviceType("OVEN", 0)
    DeviceType.BULBULATOR = DeviceType("BULBULATOR", 1)
    DeviceType.LIGHTBULB = DeviceType("LIGHTBULB", 2)
    DeviceType._enumerators = { 0:DeviceType.OVEN, 1:DeviceType.BULBULATOR, 2:DeviceType.LIGHTBULB }

    _M_Home._t_DeviceType = IcePy.defineEnum('::Home::DeviceType', DeviceType, (), DeviceType._enumerators)

    _M_Home.DeviceType = DeviceType
    del DeviceType

if 'Colors' not in _M_Home.__dict__:
    _M_Home.Colors = Ice.createTempClass()
    class Colors(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Colors.RED = Colors("RED", 0)
    Colors.GREEN = Colors("GREEN", 1)
    Colors.BLUE = Colors("BLUE", 2)
    Colors.WHITE = Colors("WHITE", 3)
    Colors.RAINBOW = Colors("RAINBOW", 4)
    Colors._enumerators = { 0:Colors.RED, 1:Colors.GREEN, 2:Colors.BLUE, 3:Colors.WHITE, 4:Colors.RAINBOW }

    _M_Home._t_Colors = IcePy.defineEnum('::Home::Colors', Colors, (), Colors._enumerators)

    _M_Home.Colors = Colors
    del Colors

if 'OvenMode' not in _M_Home.__dict__:
    _M_Home.OvenMode = Ice.createTempClass()
    class OvenMode(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    OvenMode.FAN = OvenMode("FAN", 0)
    OvenMode.CONVENTIONALHEATING = OvenMode("CONVENTIONALHEATING", 1)
    OvenMode.BOTTOMHEAT = OvenMode("BOTTOMHEAT", 2)
    OvenMode.FANWITHGRILL = OvenMode("FANWITHGRILL", 3)
    OvenMode.GRILL = OvenMode("GRILL", 4)
    OvenMode.DEFROSTING = OvenMode("DEFROSTING", 5)
    OvenMode.LIGHT = OvenMode("LIGHT", 6)
    OvenMode._enumerators = { 0:OvenMode.FAN, 1:OvenMode.CONVENTIONALHEATING, 2:OvenMode.BOTTOMHEAT, 3:OvenMode.FANWITHGRILL, 4:OvenMode.GRILL, 5:OvenMode.DEFROSTING, 6:OvenMode.LIGHT }

    _M_Home._t_OvenMode = IcePy.defineEnum('::Home::OvenMode', OvenMode, (), OvenMode._enumerators)

    _M_Home.OvenMode = OvenMode
    del OvenMode

if '_t_possibleLightBulbColors' not in _M_Home.__dict__:
    _M_Home._t_possibleLightBulbColors = IcePy.defineSequence('::Home::possibleLightBulbColors', (), _M_Home._t_Colors)

if '_t_possibleOvenMods' not in _M_Home.__dict__:
    _M_Home._t_possibleOvenMods = IcePy.defineSequence('::Home::possibleOvenMods', (), _M_Home._t_OvenMode)

if '_t_DeviceParameters' not in _M_Home.__dict__:
    _M_Home._t_DeviceParameters = IcePy.defineDictionary('::Home::DeviceParameters', (), IcePy._t_string, IcePy._t_string)

if 'Exception' not in _M_Home.__dict__:
    _M_Home.Exception = Ice.createTempClass()
    class Exception(Ice.UserException):
        def __init__(self, message=''):
            self.message = message

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::Exception'

    _M_Home._t_Exception = IcePy.defineException('::Home::Exception', Exception, (), False, None, (('message', (), IcePy._t_string, False, 0),))
    Exception._ice_type = _M_Home._t_Exception

    _M_Home.Exception = Exception
    del Exception

if 'InvalidParameterException' not in _M_Home.__dict__:
    _M_Home.InvalidParameterException = Ice.createTempClass()
    class InvalidParameterException(_M_Home.Exception):
        def __init__(self, message=''):
            _M_Home.Exception.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::InvalidParameterException'

    _M_Home._t_InvalidParameterException = IcePy.defineException('::Home::InvalidParameterException', InvalidParameterException, (), False, _M_Home._t_Exception, ())
    InvalidParameterException._ice_type = _M_Home._t_InvalidParameterException

    _M_Home.InvalidParameterException = InvalidParameterException
    del InvalidParameterException

if 'isAlreadyONException' not in _M_Home.__dict__:
    _M_Home.isAlreadyONException = Ice.createTempClass()
    class isAlreadyONException(_M_Home.InvalidParameterException):
        def __init__(self, message=''):
            _M_Home.InvalidParameterException.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::isAlreadyONException'

    _M_Home._t_isAlreadyONException = IcePy.defineException('::Home::isAlreadyONException', isAlreadyONException, (), False, _M_Home._t_InvalidParameterException, ())
    isAlreadyONException._ice_type = _M_Home._t_isAlreadyONException

    _M_Home.isAlreadyONException = isAlreadyONException
    del isAlreadyONException

if 'isAlreadyOFFException' not in _M_Home.__dict__:
    _M_Home.isAlreadyOFFException = Ice.createTempClass()
    class isAlreadyOFFException(_M_Home.InvalidParameterException):
        def __init__(self, message=''):
            _M_Home.InvalidParameterException.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::isAlreadyOFFException'

    _M_Home._t_isAlreadyOFFException = IcePy.defineException('::Home::isAlreadyOFFException', isAlreadyOFFException, (), False, _M_Home._t_InvalidParameterException, ())
    isAlreadyOFFException._ice_type = _M_Home._t_isAlreadyOFFException

    _M_Home.isAlreadyOFFException = isAlreadyOFFException
    del isAlreadyOFFException

if 'UnsupportedColorException' not in _M_Home.__dict__:
    _M_Home.UnsupportedColorException = Ice.createTempClass()
    class UnsupportedColorException(_M_Home.InvalidParameterException):
        def __init__(self, message=''):
            _M_Home.InvalidParameterException.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::UnsupportedColorException'

    _M_Home._t_UnsupportedColorException = IcePy.defineException('::Home::UnsupportedColorException', UnsupportedColorException, (), False, _M_Home._t_InvalidParameterException, ())
    UnsupportedColorException._ice_type = _M_Home._t_UnsupportedColorException

    _M_Home.UnsupportedColorException = UnsupportedColorException
    del UnsupportedColorException

if 'UnsupportedOvenModeException' not in _M_Home.__dict__:
    _M_Home.UnsupportedOvenModeException = Ice.createTempClass()
    class UnsupportedOvenModeException(_M_Home.InvalidParameterException):
        def __init__(self, message=''):
            _M_Home.InvalidParameterException.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::UnsupportedOvenModeException'

    _M_Home._t_UnsupportedOvenModeException = IcePy.defineException('::Home::UnsupportedOvenModeException', UnsupportedOvenModeException, (), False, _M_Home._t_InvalidParameterException, ())
    UnsupportedOvenModeException._ice_type = _M_Home._t_UnsupportedOvenModeException

    _M_Home.UnsupportedOvenModeException = UnsupportedOvenModeException
    del UnsupportedOvenModeException

if 'TemperatureOutOfScope' not in _M_Home.__dict__:
    _M_Home.TemperatureOutOfScope = Ice.createTempClass()
    class TemperatureOutOfScope(_M_Home.InvalidParameterException):
        def __init__(self, message=''):
            _M_Home.InvalidParameterException.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::TemperatureOutOfScope'

    _M_Home._t_TemperatureOutOfScope = IcePy.defineException('::Home::TemperatureOutOfScope', TemperatureOutOfScope, (), False, _M_Home._t_InvalidParameterException, ())
    TemperatureOutOfScope._ice_type = _M_Home._t_TemperatureOutOfScope

    _M_Home.TemperatureOutOfScope = TemperatureOutOfScope
    del TemperatureOutOfScope

if 'OvenOpenCantPerformActionException' not in _M_Home.__dict__:
    _M_Home.OvenOpenCantPerformActionException = Ice.createTempClass()
    class OvenOpenCantPerformActionException(_M_Home.InvalidParameterException):
        def __init__(self, message=''):
            _M_Home.InvalidParameterException.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::OvenOpenCantPerformActionException'

    _M_Home._t_OvenOpenCantPerformActionException = IcePy.defineException('::Home::OvenOpenCantPerformActionException', OvenOpenCantPerformActionException, (), False, _M_Home._t_InvalidParameterException, ())
    OvenOpenCantPerformActionException._ice_type = _M_Home._t_OvenOpenCantPerformActionException

    _M_Home.OvenOpenCantPerformActionException = OvenOpenCantPerformActionException
    del OvenOpenCantPerformActionException

if 'TurnOnToMakeNoiseException' not in _M_Home.__dict__:
    _M_Home.TurnOnToMakeNoiseException = Ice.createTempClass()
    class TurnOnToMakeNoiseException(_M_Home.Exception):
        def __init__(self, message=''):
            _M_Home.Exception.__init__(self, message)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::TurnOnToMakeNoiseException'

    _M_Home._t_TurnOnToMakeNoiseException = IcePy.defineException('::Home::TurnOnToMakeNoiseException', TurnOnToMakeNoiseException, (), False, _M_Home._t_Exception, ())
    TurnOnToMakeNoiseException._ice_type = _M_Home._t_TurnOnToMakeNoiseException

    _M_Home.TurnOnToMakeNoiseException = TurnOnToMakeNoiseException
    del TurnOnToMakeNoiseException

if 'Device' not in _M_Home.__dict__:
    _M_Home.Device = Ice.createTempClass()
    class Device(Ice.Value):
        def __init__(self, name='', type=_M_Home.DeviceType.OVEN, isOn=False):
            self.name = name
            self.type = type
            self.isOn = isOn

        def ice_id(self):
            return '::Home::Device'

        @staticmethod
        def ice_staticId():
            return '::Home::Device'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_Device)

        __repr__ = __str__

    _M_Home._t_Device = IcePy.defineValue('::Home::Device', Device, -1, (), False, False, None, (
        ('name', (), IcePy._t_string, False, 0),
        ('type', (), _M_Home._t_DeviceType, False, 0),
        ('isOn', (), IcePy._t_bool, False, 0)
    ))
    Device._ice_type = _M_Home._t_Device

    _M_Home.Device = Device
    del Device

_M_Home._t_DeviceI = IcePy.defineValue('::Home::DeviceI', Ice.Value, -1, (), False, True, None, ())

if 'DeviceIPrx' not in _M_Home.__dict__:
    _M_Home.DeviceIPrx = Ice.createTempClass()
    class DeviceIPrx(Ice.ObjectPrx):

        def turnDeviceOn(self, context=None):
            return _M_Home.DeviceI._op_turnDeviceOn.invoke(self, ((), context))

        def turnDeviceOnAsync(self, context=None):
            return _M_Home.DeviceI._op_turnDeviceOn.invokeAsync(self, ((), context))

        def begin_turnDeviceOn(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.DeviceI._op_turnDeviceOn.begin(self, ((), _response, _ex, _sent, context))

        def end_turnDeviceOn(self, _r):
            return _M_Home.DeviceI._op_turnDeviceOn.end(self, _r)

        def turnDeviceOff(self, context=None):
            return _M_Home.DeviceI._op_turnDeviceOff.invoke(self, ((), context))

        def turnDeviceOffAsync(self, context=None):
            return _M_Home.DeviceI._op_turnDeviceOff.invokeAsync(self, ((), context))

        def begin_turnDeviceOff(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.DeviceI._op_turnDeviceOff.begin(self, ((), _response, _ex, _sent, context))

        def end_turnDeviceOff(self, _r):
            return _M_Home.DeviceI._op_turnDeviceOff.end(self, _r)

        def getDeviceParameters(self, context=None):
            return _M_Home.DeviceI._op_getDeviceParameters.invoke(self, ((), context))

        def getDeviceParametersAsync(self, context=None):
            return _M_Home.DeviceI._op_getDeviceParameters.invokeAsync(self, ((), context))

        def begin_getDeviceParameters(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.DeviceI._op_getDeviceParameters.begin(self, ((), _response, _ex, _sent, context))

        def end_getDeviceParameters(self, _r):
            return _M_Home.DeviceI._op_getDeviceParameters.end(self, _r)

        def setParameters(self, deviceParameters, context=None):
            return _M_Home.DeviceI._op_setParameters.invoke(self, ((deviceParameters, ), context))

        def setParametersAsync(self, deviceParameters, context=None):
            return _M_Home.DeviceI._op_setParameters.invokeAsync(self, ((deviceParameters, ), context))

        def begin_setParameters(self, deviceParameters, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.DeviceI._op_setParameters.begin(self, ((deviceParameters, ), _response, _ex, _sent, context))

        def end_setParameters(self, _r):
            return _M_Home.DeviceI._op_setParameters.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.DeviceIPrx.ice_checkedCast(proxy, '::Home::DeviceI', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.DeviceIPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::DeviceI'
    _M_Home._t_DeviceIPrx = IcePy.defineProxy('::Home::DeviceI', DeviceIPrx)

    _M_Home.DeviceIPrx = DeviceIPrx
    del DeviceIPrx

    _M_Home.DeviceI = Ice.createTempClass()
    class DeviceI(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Home::DeviceI', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::DeviceI'

        @staticmethod
        def ice_staticId():
            return '::Home::DeviceI'

        def turnDeviceOn(self, current=None):
            raise NotImplementedError("servant method 'turnDeviceOn' not implemented")

        def turnDeviceOff(self, current=None):
            raise NotImplementedError("servant method 'turnDeviceOff' not implemented")

        def getDeviceParameters(self, current=None):
            raise NotImplementedError("servant method 'getDeviceParameters' not implemented")

        def setParameters(self, deviceParameters, current=None):
            raise NotImplementedError("servant method 'setParameters' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_DeviceIDisp)

        __repr__ = __str__

    _M_Home._t_DeviceIDisp = IcePy.defineClass('::Home::DeviceI', DeviceI, (), None, ())
    DeviceI._ice_type = _M_Home._t_DeviceIDisp

    DeviceI._op_turnDeviceOn = IcePy.Operation('turnDeviceOn', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, (_M_Home._t_isAlreadyONException,))
    DeviceI._op_turnDeviceOff = IcePy.Operation('turnDeviceOff', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, (_M_Home._t_isAlreadyOFFException,))
    DeviceI._op_getDeviceParameters = IcePy.Operation('getDeviceParameters', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_Home._t_DeviceParameters, False, 0), ())
    DeviceI._op_setParameters = IcePy.Operation('setParameters', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Home._t_DeviceParameters, False, 0),), (), None, (_M_Home._t_InvalidParameterException,))

    _M_Home.DeviceI = DeviceI
    del DeviceI

if 'LightBulb' not in _M_Home.__dict__:
    _M_Home.LightBulb = Ice.createTempClass()
    class LightBulb(_M_Home.Device):
        def __init__(self, name='', type=_M_Home.DeviceType.OVEN, isOn=False, possibleLightBulbColors=None, color=_M_Home.Colors.RED):
            _M_Home.Device.__init__(self, name, type, isOn)
            self.possibleLightBulbColors = possibleLightBulbColors
            self.color = color

        def ice_id(self):
            return '::Home::LightBulb'

        @staticmethod
        def ice_staticId():
            return '::Home::LightBulb'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_LightBulb)

        __repr__ = __str__

    _M_Home._t_LightBulb = IcePy.defineValue('::Home::LightBulb', LightBulb, -1, (), False, False, _M_Home._t_Device, (
        ('possibleLightBulbColors', (), _M_Home._t_possibleLightBulbColors, False, 0),
        ('color', (), _M_Home._t_Colors, False, 0)
    ))
    LightBulb._ice_type = _M_Home._t_LightBulb

    _M_Home.LightBulb = LightBulb
    del LightBulb

_M_Home._t_LightBulbI = IcePy.defineValue('::Home::LightBulbI', Ice.Value, -1, (), False, True, None, ())

if 'LightBulbIPrx' not in _M_Home.__dict__:
    _M_Home.LightBulbIPrx = Ice.createTempClass()
    class LightBulbIPrx(_M_Home.DeviceIPrx):

        def setColor(self, color, context=None):
            return _M_Home.LightBulbI._op_setColor.invoke(self, ((color, ), context))

        def setColorAsync(self, color, context=None):
            return _M_Home.LightBulbI._op_setColor.invokeAsync(self, ((color, ), context))

        def begin_setColor(self, color, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.LightBulbI._op_setColor.begin(self, ((color, ), _response, _ex, _sent, context))

        def end_setColor(self, _r):
            return _M_Home.LightBulbI._op_setColor.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.LightBulbIPrx.ice_checkedCast(proxy, '::Home::LightBulbI', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.LightBulbIPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::LightBulbI'
    _M_Home._t_LightBulbIPrx = IcePy.defineProxy('::Home::LightBulbI', LightBulbIPrx)

    _M_Home.LightBulbIPrx = LightBulbIPrx
    del LightBulbIPrx

    _M_Home.LightBulbI = Ice.createTempClass()
    class LightBulbI(_M_Home.DeviceI):

        def ice_ids(self, current=None):
            return ('::Home::DeviceI', '::Home::LightBulbI', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::LightBulbI'

        @staticmethod
        def ice_staticId():
            return '::Home::LightBulbI'

        def setColor(self, color, current=None):
            raise NotImplementedError("servant method 'setColor' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_LightBulbIDisp)

        __repr__ = __str__

    _M_Home._t_LightBulbIDisp = IcePy.defineClass('::Home::LightBulbI', LightBulbI, (), None, (_M_Home._t_DeviceIDisp,))
    LightBulbI._ice_type = _M_Home._t_LightBulbIDisp

    LightBulbI._op_setColor = IcePy.Operation('setColor', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Home._t_Colors, False, 0),), (), None, (_M_Home._t_UnsupportedColorException,))

    _M_Home.LightBulbI = LightBulbI
    del LightBulbI

if 'Oven' not in _M_Home.__dict__:
    _M_Home.Oven = Ice.createTempClass()
    class Oven(_M_Home.Device):
        def __init__(self, name='', type=_M_Home.DeviceType.OVEN, isOn=False, possibleOvenMods=None, ovenMode=_M_Home.OvenMode.FAN, temperature=0, isOpen=False):
            _M_Home.Device.__init__(self, name, type, isOn)
            self.possibleOvenMods = possibleOvenMods
            self.ovenMode = ovenMode
            self.temperature = temperature
            self.isOpen = isOpen

        def ice_id(self):
            return '::Home::Oven'

        @staticmethod
        def ice_staticId():
            return '::Home::Oven'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_Oven)

        __repr__ = __str__

    _M_Home._t_Oven = IcePy.defineValue('::Home::Oven', Oven, -1, (), False, False, _M_Home._t_Device, (
        ('possibleOvenMods', (), _M_Home._t_possibleOvenMods, False, 0),
        ('ovenMode', (), _M_Home._t_OvenMode, False, 0),
        ('temperature', (), IcePy._t_short, False, 0),
        ('isOpen', (), IcePy._t_bool, False, 0)
    ))
    Oven._ice_type = _M_Home._t_Oven

    _M_Home.Oven = Oven
    del Oven

_M_Home._t_OvenI = IcePy.defineValue('::Home::OvenI', Ice.Value, -1, (), False, True, None, ())

if 'OvenIPrx' not in _M_Home.__dict__:
    _M_Home.OvenIPrx = Ice.createTempClass()
    class OvenIPrx(_M_Home.DeviceIPrx):

        def setOvenMode(self, ovenMode, context=None):
            return _M_Home.OvenI._op_setOvenMode.invoke(self, ((ovenMode, ), context))

        def setOvenModeAsync(self, ovenMode, context=None):
            return _M_Home.OvenI._op_setOvenMode.invokeAsync(self, ((ovenMode, ), context))

        def begin_setOvenMode(self, ovenMode, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.OvenI._op_setOvenMode.begin(self, ((ovenMode, ), _response, _ex, _sent, context))

        def end_setOvenMode(self, _r):
            return _M_Home.OvenI._op_setOvenMode.end(self, _r)

        def setTemperature(self, temperature, context=None):
            return _M_Home.OvenI._op_setTemperature.invoke(self, ((temperature, ), context))

        def setTemperatureAsync(self, temperature, context=None):
            return _M_Home.OvenI._op_setTemperature.invokeAsync(self, ((temperature, ), context))

        def begin_setTemperature(self, temperature, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.OvenI._op_setTemperature.begin(self, ((temperature, ), _response, _ex, _sent, context))

        def end_setTemperature(self, _r):
            return _M_Home.OvenI._op_setTemperature.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.OvenIPrx.ice_checkedCast(proxy, '::Home::OvenI', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.OvenIPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::OvenI'
    _M_Home._t_OvenIPrx = IcePy.defineProxy('::Home::OvenI', OvenIPrx)

    _M_Home.OvenIPrx = OvenIPrx
    del OvenIPrx

    _M_Home.OvenI = Ice.createTempClass()
    class OvenI(_M_Home.DeviceI):

        def ice_ids(self, current=None):
            return ('::Home::DeviceI', '::Home::OvenI', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::OvenI'

        @staticmethod
        def ice_staticId():
            return '::Home::OvenI'

        def setOvenMode(self, ovenMode, current=None):
            raise NotImplementedError("servant method 'setOvenMode' not implemented")

        def setTemperature(self, temperature, current=None):
            raise NotImplementedError("servant method 'setTemperature' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_OvenIDisp)

        __repr__ = __str__

    _M_Home._t_OvenIDisp = IcePy.defineClass('::Home::OvenI', OvenI, (), None, (_M_Home._t_DeviceIDisp,))
    OvenI._ice_type = _M_Home._t_OvenIDisp

    OvenI._op_setOvenMode = IcePy.Operation('setOvenMode', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Home._t_OvenMode, False, 0),), (), None, (_M_Home._t_UnsupportedOvenModeException, _M_Home._t_OvenOpenCantPerformActionException))
    OvenI._op_setTemperature = IcePy.Operation('setTemperature', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_short, False, 0),), (), None, (_M_Home._t_TemperatureOutOfScope,))

    _M_Home.OvenI = OvenI
    del OvenI

if 'Bulbulator' not in _M_Home.__dict__:
    _M_Home.Bulbulator = Ice.createTempClass()
    class Bulbulator(_M_Home.Device):
        def __init__(self, name='', type=_M_Home.DeviceType.OVEN, isOn=False, phrase='', repeatNumber=0):
            _M_Home.Device.__init__(self, name, type, isOn)
            self.phrase = phrase
            self.repeatNumber = repeatNumber

        def ice_id(self):
            return '::Home::Bulbulator'

        @staticmethod
        def ice_staticId():
            return '::Home::Bulbulator'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_Bulbulator)

        __repr__ = __str__

    _M_Home._t_Bulbulator = IcePy.defineValue('::Home::Bulbulator', Bulbulator, -1, (), False, False, _M_Home._t_Device, (
        ('phrase', (), IcePy._t_string, False, 0),
        ('repeatNumber', (), IcePy._t_short, False, 0)
    ))
    Bulbulator._ice_type = _M_Home._t_Bulbulator

    _M_Home.Bulbulator = Bulbulator
    del Bulbulator

_M_Home._t_BulbulatorI = IcePy.defineValue('::Home::BulbulatorI', Ice.Value, -1, (), False, True, None, ())

if 'BulbulatorIPrx' not in _M_Home.__dict__:
    _M_Home.BulbulatorIPrx = Ice.createTempClass()
    class BulbulatorIPrx(_M_Home.DeviceIPrx):

        def isBulbulatorSaturator(self, context=None):
            return _M_Home.BulbulatorI._op_isBulbulatorSaturator.invoke(self, ((), context))

        def isBulbulatorSaturatorAsync(self, context=None):
            return _M_Home.BulbulatorI._op_isBulbulatorSaturator.invokeAsync(self, ((), context))

        def begin_isBulbulatorSaturator(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.BulbulatorI._op_isBulbulatorSaturator.begin(self, ((), _response, _ex, _sent, context))

        def end_isBulbulatorSaturator(self, _r):
            return _M_Home.BulbulatorI._op_isBulbulatorSaturator.end(self, _r)

        def makeNoise(self, repeatNumber, context=None):
            return _M_Home.BulbulatorI._op_makeNoise.invoke(self, ((repeatNumber, ), context))

        def makeNoiseAsync(self, repeatNumber, context=None):
            return _M_Home.BulbulatorI._op_makeNoise.invokeAsync(self, ((repeatNumber, ), context))

        def begin_makeNoise(self, repeatNumber, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.BulbulatorI._op_makeNoise.begin(self, ((repeatNumber, ), _response, _ex, _sent, context))

        def end_makeNoise(self, _r):
            return _M_Home.BulbulatorI._op_makeNoise.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.BulbulatorIPrx.ice_checkedCast(proxy, '::Home::BulbulatorI', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.BulbulatorIPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::BulbulatorI'
    _M_Home._t_BulbulatorIPrx = IcePy.defineProxy('::Home::BulbulatorI', BulbulatorIPrx)

    _M_Home.BulbulatorIPrx = BulbulatorIPrx
    del BulbulatorIPrx

    _M_Home.BulbulatorI = Ice.createTempClass()
    class BulbulatorI(_M_Home.DeviceI):

        def ice_ids(self, current=None):
            return ('::Home::BulbulatorI', '::Home::DeviceI', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::BulbulatorI'

        @staticmethod
        def ice_staticId():
            return '::Home::BulbulatorI'

        def isBulbulatorSaturator(self, current=None):
            raise NotImplementedError("servant method 'isBulbulatorSaturator' not implemented")

        def makeNoise(self, repeatNumber, current=None):
            raise NotImplementedError("servant method 'makeNoise' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_BulbulatorIDisp)

        __repr__ = __str__

    _M_Home._t_BulbulatorIDisp = IcePy.defineClass('::Home::BulbulatorI', BulbulatorI, (), None, (_M_Home._t_DeviceIDisp,))
    BulbulatorI._ice_type = _M_Home._t_BulbulatorIDisp

    BulbulatorI._op_isBulbulatorSaturator = IcePy.Operation('isBulbulatorSaturator', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())
    BulbulatorI._op_makeNoise = IcePy.Operation('makeNoise', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_short, False, 0),), (), ((), IcePy._t_string, False, 0), (_M_Home._t_TurnOnToMakeNoiseException,))

    _M_Home.BulbulatorI = BulbulatorI
    del BulbulatorI

if 'DeviceName' not in _M_Home.__dict__:
    _M_Home.DeviceName = Ice.createTempClass()
    class DeviceName(Ice.Value):
        def __init__(self, name=''):
            self.name = name

        def ice_id(self):
            return '::Home::DeviceName'

        @staticmethod
        def ice_staticId():
            return '::Home::DeviceName'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_DeviceName)

        __repr__ = __str__

    _M_Home._t_DeviceName = IcePy.defineValue('::Home::DeviceName', DeviceName, -1, (), False, False, None, (('name', (), IcePy._t_string, False, 0),))
    DeviceName._ice_type = _M_Home._t_DeviceName

    _M_Home.DeviceName = DeviceName
    del DeviceName

if '_t_Devices' not in _M_Home.__dict__:
    _M_Home._t_Devices = IcePy.defineSequence('::Home::Devices', (), IcePy._t_string)

if 'Connection' not in _M_Home.__dict__:
    _M_Home.Connection = Ice.createTempClass()
    class Connection(Ice.Value):
        def __init__(self, devices=None):
            self.devices = devices

        def ice_id(self):
            return '::Home::Connection'

        @staticmethod
        def ice_staticId():
            return '::Home::Connection'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_Connection)

        __repr__ = __str__

    _M_Home._t_Connection = IcePy.defineValue('::Home::Connection', Connection, -1, (), False, False, None, (('devices', (), _M_Home._t_Devices, False, 0),))
    Connection._ice_type = _M_Home._t_Connection

    _M_Home.Connection = Connection
    del Connection

_M_Home._t_ConnectionI = IcePy.defineValue('::Home::ConnectionI', Ice.Value, -1, (), False, True, None, ())

if 'ConnectionIPrx' not in _M_Home.__dict__:
    _M_Home.ConnectionIPrx = Ice.createTempClass()
    class ConnectionIPrx(Ice.ObjectPrx):

        def ping(self, devices, context=None):
            return _M_Home.ConnectionI._op_ping.invoke(self, ((devices, ), context))

        def pingAsync(self, devices, context=None):
            return _M_Home.ConnectionI._op_ping.invokeAsync(self, ((devices, ), context))

        def begin_ping(self, devices, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.ConnectionI._op_ping.begin(self, ((devices, ), _response, _ex, _sent, context))

        def end_ping(self, _r):
            return _M_Home.ConnectionI._op_ping.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.ConnectionIPrx.ice_checkedCast(proxy, '::Home::ConnectionI', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.ConnectionIPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::ConnectionI'
    _M_Home._t_ConnectionIPrx = IcePy.defineProxy('::Home::ConnectionI', ConnectionIPrx)

    _M_Home.ConnectionIPrx = ConnectionIPrx
    del ConnectionIPrx

    _M_Home.ConnectionI = Ice.createTempClass()
    class ConnectionI(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Home::ConnectionI', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::ConnectionI'

        @staticmethod
        def ice_staticId():
            return '::Home::ConnectionI'

        def ping(self, devices, current=None):
            raise NotImplementedError("servant method 'ping' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_ConnectionIDisp)

        __repr__ = __str__

    _M_Home._t_ConnectionIDisp = IcePy.defineClass('::Home::ConnectionI', ConnectionI, (), None, ())
    ConnectionI._ice_type = _M_Home._t_ConnectionIDisp

    ConnectionI._op_ping = IcePy.Operation('ping', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Home._t_Devices, False, 0),), (), None, ())

    _M_Home.ConnectionI = ConnectionI
    del ConnectionI

# End of module Home