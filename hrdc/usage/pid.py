from .usage import *

PhysicalInterfaceDevice = Usage("pid.PhysicalInterfaceDevice", 0xf0001, CA)
Normal = Usage("pid.Normal", 0xf0020, DV)
SetEffectReport = Usage("pid.SetEffectReport", 0xf0021, CL)
EffectBlockIndex = Usage("pid.EffectBlockIndex", 0xf0022, DV)
ParameterBlockOffset = Usage("pid.ParameterBlockOffset", 0xf0023, DV)
ROMFlag = Usage("pid.ROMFlag", 0xf0024, DF)
EffectType = Usage("pid.EffectType", 0xf0025, NAry)
ETConstantForce = Usage("pid.ETConstantForce", 0xf0026, Sel) 
ETRamp = Usage("pid.ETRamp", 0xf0027, Sel) 
ETCustomForceData = Usage("pid.ETCustomForceData", 0xf0028, Sel) 
ETSquare = Usage("pid.ETSquare", 0xf0030, Sel) 
ETSine = Usage("pid.ETSine", 0xf0031, Sel) 
ETTriangle = Usage("pid.ETTriangle", 0xf0032, Sel) 
ETSawtoothUp = Usage("pid.ETSawtoothUp", 0xf0033, Sel) 
ETSawtoothDown = Usage("pid.ETSawtoothDown", 0xf0034, Sel) 
ETSpring = Usage("pid.ETSpring", 0xf0040, Sel) 
ETDamper = Usage("pid.ETDamper", 0xf0041, Sel) 
ETInertia = Usage("pid.ETInertia", 0xf0042, Sel) 
ETFriction = Usage("pid.ETFriction", 0xf0043, Sel) 
Duration = Usage("pid.Duration", 0xf0050, DV)
SamplePeriod = Usage("pid.SamplePeriod", 0xf0051, DV)
Gain = Usage("pid.Gain", 0xf0052, DV)
TriggerButton = Usage("pid.TriggerButton", 0xf0053, DV)
TriggerRepeatInterval = Usage("pid.TriggerRepeatInterval", 0xf0054, DV)
AxesEnable = Usage("pid.AxesEnable", 0xf0055, US)
DirectionEnable = Usage("pid.DirectionEnable", 0xf0056, DF)
Direction = Usage("pid.Direction", 0xf0057, CL)
TypeSpecificBlockOffset = Usage("pid.TypeSpecificBlockOffset", 0xf0058, CL)
BlockType = Usage("pid.BlockType", 0xf0059, NAry)
SetEnvelopeReport = Usage("pid.SetEnvelopeReport", 0xf005A, CL)
AttackLevel = Usage("pid.AttackLevel", 0xf005B, DV)
AttackTime = Usage("pid.AttackTime", 0xf005C, DV)
FadeLevel = Usage("pid.FadeLevel", 0xf005D, DV)
FadeTime = Usage("pid.FadeTime", 0xf005E, DV)
SetConditionReport = Usage("pid.SetConditionReport", 0xf005F, CL)
CPOffset = Usage("pid.CPOffset", 0xf0060, DV)
PositiveCoefficient = Usage("pid.PositiveCoefficient", 0xf0061, DV)
NegativeCoefficient = Usage("pid.NegativeCoefficient", 0xf0062, DV)
PositiveSaturation = Usage("pid.PositiveSaturation", 0xf0063, DV)
NegativeSaturation = Usage("pid.NegativeSaturation", 0xf0064, DV)
DeadBand = Usage("pid.DeadBand", 0xf0065, DV)
DownloadForceSample = Usage("pid.DownloadForceSample", 0xf0066, CL)
IsochCustomForceEnable = Usage("pid.IsochCustomForceEnable", 0xf0067, CL)
CustomForceDataReport = Usage("pid.CustomForceDataReport", 0xf0068, CL)
CustomForceData = Usage("pid.CustomForceData", 0xf0069, DV)
CustomForceVendorDefinedData = Usage("pid.CustomForceVendorDefinedData", 0xf006A, DV)
SetCustomForceReport = Usage("pid.SetCustomForceReport", 0xf006B, CL)
CustomForceDataOffset = Usage("pid.CustomForceDataOffset", 0xf006C, DV)
SampleCount = Usage("pid.SampleCount", 0xf006D, DV)
SetPeriodicReport = Usage("pid.SetPeriodicReport", 0xf006E, CL)
Offset = Usage("pid.Offset", 0xf006F, DV)
Magnitude = Usage("pid.Magnitude", 0xf0070, DV)
Phase = Usage("pid.Phase", 0xf0071, DV)
Period = Usage("pid.Period", 0xf0072, DV)
SetConstantForceReport = Usage("pid.SetConstantForceReport", 0xf0073, CL)
SetRampForceReport = Usage("pid.SetRampForceReport", 0xf0074, CL)
RampStart = Usage("pid.RampStart", 0xf0075, DV)
RampEnd = Usage("pid.RampEnd", 0xf0076, DV)
EffectOperationReport = Usage("pid.EffectOperationReport", 0xf0077, CL)
EffectOperation = Usage("pid.EffectOperation", 0xf0078, NAry)
OpEffectStart = Usage("pid.OpEffectStart", 0xf0079, Sel) 
OpEffectStartSolo = Usage("pid.OpEffectStartSolo", 0xf007A, Sel) 
OpEffectStop = Usage("pid.OpEffectStop", 0xf007B, Sel) 
LoopCount = Usage("pid.LoopCount", 0xf007C, DV)
DeviceGainReport = Usage("pid.DeviceGainReport", 0xf007D, CL)
DeviceGain = Usage("pid.DeviceGain", 0xf007E, DV)
PoolReport = Usage("pid.PoolReport", 0xf007F, CL)
RAMPoolSize = Usage("pid.RAMPoolSize", 0xf0080, DV)
ROMPoolSize = Usage("pid.ROMPoolSize", 0xf0081, SV)
ROMEffectBlockCount = Usage("pid.ROMEffectBlockCount", 0xf0082, SV)
SimultaneousEffectsMax = Usage("pid.SimultaneousEffectsMax", 0xf0083, SV)
PoolAlignment = Usage("pid.PoolAlignment", 0xf0084, SV)
PoolMoveReport = Usage("pid.PoolMoveReport", 0xf0085, CL)
MoveSource = Usage("pid.MoveSource", 0xf0086, DV)
MoveDestination = Usage("pid.MoveDestination", 0xf0087, DV)
MoveLength = Usage("pid.MoveLength", 0xf0088, DV)
BlockLoadReport = Usage("pid.BlockLoadReport", 0xf0089, CL)
BlockLoadStatus = Usage("pid.BlockLoadStatus", 0xf008B, NAry)
BlockLoadSuccess = Usage("pid.BlockLoadSuccess", 0xf008C, Sel) 
BlockLoadFull = Usage("pid.BlockLoadFull", 0xf008D, Sel) 
BlockLoadError = Usage("pid.BlockLoadError", 0xf008E, Sel) 
BlockHandle = Usage("pid.BlockHandle", 0xf008F, DV)
BlockFreeReport = Usage("pid.BlockFreeReport", 0xf0090, CL)
TypeSpecificBlockHandle = Usage("pid.TypeSpecificBlockHandle", 0xf0091, DV)
StateReport = Usage("pid.StateReport", 0xf0092, CL)
EffectPlaying = Usage("pid.EffectPlaying", 0xf0094, DF)
DeviceControlReport = Usage("pid.DeviceControlReport", 0xf0095, CL)
DeviceControl = Usage("pid.DeviceControl", 0xf0096, NAry)
DCEnableActuators = Usage("pid.DCEnableActuators", 0xf0097, Sel) 
DCDisableActuators = Usage("pid.DCDisableActuators", 0xf0098, Sel) 
DCStopAllEffects = Usage("pid.DCStopAllEffects", 0xf0099, Sel) 
DCDeviceReset = Usage("pid.DCDeviceReset", 0xf009A, Sel) 
DCDevicePause = Usage("pid.DCDevicePause", 0xf009B, Sel) 
DCDeviceContinue = Usage("pid.DCDeviceContinue", 0xf009C, Sel) 
DevicePaused = Usage("pid.DevicePaused", 0xf009F, DF)
ActuatorsEnabled = Usage("pid.ActuatorsEnabled", 0xf00A0, DF)
SafetySwitch = Usage("pid.SafetySwitch", 0xf00A4, DF)
ActuatorOverrideSwitch = Usage("pid.ActuatorOverrideSwitch", 0xf00A5, DF)
ActuatorPower = Usage("pid.ActuatorPower", 0xf00A6, OOC) 
StartDelay = Usage("pid.StartDelay", 0xf00A7, DV)
ParameterBlockSize = Usage("pid.ParameterBlockSize", 0xf00A8, CL)
DeviceManagedPool = Usage("pid.DeviceManagedPool", 0xf00A9, SF)
SharedParameterBlocks = Usage("pid.SharedParameterBlocks", 0xf00AA, SF)
CreateNewEffectReport = Usage("pid.CreateNewEffectReport", 0xf00AB, CL)
RAMPoolAvailable = Usage("pid.RAMPoolAvailable", 0xf00AC, DV)
