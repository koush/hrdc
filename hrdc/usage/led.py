from .usage import *

NumLock = Usage("led.NumLock", 0x80001, OOC)
CapsLock = Usage("led.CapsLock", 0x80002, OOC)
ScrollLock = Usage("led.ScrollLock", 0x80003, OOC)
Compose = Usage("led.Compose", 0x80004, OOC)
Kana = Usage("led.Kana", 0x80005, OOC)
Power = Usage("led.Power", 0x80006, OOC)
Shift = Usage("led.Shift", 0x80007, OOC)
DoNotDisturb = Usage("led.DoNotDisturb", 0x80008, OOC)
Mute = Usage("led.Mute", 0x80009, OOC)
ToneEnable = Usage("led.ToneEnable", 0x8000A, OOC)
HighCutFilter = Usage("led.HighCutFilter", 0x8000B, OOC)
LowCutFilter = Usage("led.LowCutFilter", 0x8000C, OOC)
EqualizerEnable = Usage("led.EqualizerEnable", 0x8000D, OOC)
SoundFieldOn = Usage("led.SoundFieldOn", 0x8000E, OOC)
SurroundOn = Usage("led.SurroundOn", 0x8000F, OOC)
Repeat = Usage("led.Repeat", 0x80010, OOC)
Stereo = Usage("led.Stereo", 0x80011, OOC)
SamplingRateDetect = Usage("led.SamplingRateDetect", 0x80012, OOC)
Spinning = Usage("led.Spinning", 0x80013, OOC)
CAV = Usage("led.CAV", 0x80014, OOC)
CLV = Usage("led.CLV", 0x80015, OOC)
RecordingFormatDetect = Usage("led.RecordingFormatDetect", 0x80016, OOC)
OffHook = Usage("led.OffHook", 0x80017, OOC)
Ring = Usage("led.Ring", 0x80018, OOC)
MessageWaiting = Usage("led.MessageWaiting", 0x80019, OOC)
DataMode = Usage("led.DataMode", 0x8001A, OOC)
BatteryOperation = Usage("led.BatteryOperation", 0x8001B, OOC)
BatteryOK = Usage("led.BatteryOK", 0x8001C, OOC)
BatteryLow = Usage("led.BatteryLow", 0x8001D, OOC)
Speaker = Usage("led.Speaker", 0x8001E, OOC)
HeadSet = Usage("led.HeadSet", 0x8001F, OOC)
Hold = Usage("led.Hold", 0x80020, OOC)
Microphone = Usage("led.Microphone", 0x80021, OOC)
Coverage = Usage("led.Coverage", 0x80022, OOC)
NightMode = Usage("led.NightMode", 0x80023, OOC)
SendCalls = Usage("led.SendCalls", 0x80024, OOC)
CallPickup = Usage("led.CallPickup", 0x80025, OOC)
Conference = Usage("led.Conference", 0x80026, OOC)
StandBy = Usage("led.StandBy", 0x80027, OOC)
CameraOn = Usage("led.CameraOn", 0x80028, OOC)
CameraOff = Usage("led.CameraOff", 0x80029, OOC)
OnLine = Usage("led.OnLine", 0x8002A, OOC)
OffLine = Usage("led.OffLine", 0x8002B, OOC)
Busy = Usage("led.Busy", 0x8002C, OOC)
Ready = Usage("led.Ready", 0x8002D, OOC)
PaperOut = Usage("led.PaperOut", 0x8002E, OOC)
PaperJam = Usage("led.PaperJam", 0x8002F, OOC)
Remote = Usage("led.Remote", 0x80030, OOC)
Forward = Usage("led.Forward", 0x80031, OOC)
Reverse = Usage("led.Reverse", 0x80032, OOC)
Stop = Usage("led.Stop", 0x80033, OOC)
Rewind = Usage("led.Rewind", 0x80034, OOC)
FastForward = Usage("led.FastForward", 0x80035, OOC)
Play = Usage("led.Play", 0x80036, OOC)
Pause = Usage("led.Pause", 0x80037, OOC)
Record = Usage("led.Record", 0x80038, OOC)
Error = Usage("led.Error", 0x80039, OOC)
UsageSelectedIndicator = Usage("led.UsageSelectedIndicator", 0x8003A, US)
UsageInUseIndicator = Usage("led.UsageInUseIndicator", 0x8003B, US)
UsageMultiModeIndicator = Usage("led.UsageMultiModeIndicator", 0x8003C, UM)
IndicatorOn = Usage("led.IndicatorOn", 0x8003D, Sel)
IndicatorFlash = Usage("led.IndicatorFlash", 0x8003E, Sel)
IndicatorSlowBlink = Usage("led.IndicatorSlowBlink", 0x8003F, Sel)
IndicatorFastBlink = Usage("led.IndicatorFastBlink", 0x80040, Sel)
IndicatorOff = Usage("led.IndicatorOff", 0x80041, Sel)
FlashOnTime = Usage("led.FlashOnTime", 0x80042, DV)
SlowBlinkOnTime = Usage("led.SlowBlinkOnTime", 0x80043, DV)
SlowBlinkOffTime = Usage("led.SlowBlinkOffTime", 0x80044, DV)
FastBlinkOnTime = Usage("led.FastBlinkOnTime", 0x80045, DV)
FastBlinkOffTime = Usage("led.FastBlinkOffTime", 0x80046, DV)
UsageIndicatorColor = Usage("led.UsageIndicatorColor", 0x80047, UM)
IndicatorRed = Usage("led.IndicatorRed", 0x80048, Sel)
IndicatorAmber = Usage("led.IndicatorAmber", 0x8004A, Sel)
SystemSuspend = Usage("led.SystemSuspend", 0x8004C, OOC)
ExternalPowerConnected = Usage("led.ExternalPowerConnected", 0x8004D, OOC)

# HUTRR47
PlayerIndicator = Usage("led.PlayerIndicator", 0x8004e, NAry)
Player1 = Usage("led.Player1", 0x8004f, Sel)
Player2 = Usage("led.Player2", 0x80050, Sel)
Player3 = Usage("led.Player3", 0x80051, Sel)
Player4 = Usage("led.Player4", 0x80052, Sel)
Player5 = Usage("led.Player5", 0x80053, Sel)
Player6 = Usage("led.Player6", 0x80054, Sel)
Player7 = Usage("led.Player7", 0x80055, Sel)
Player8 = Usage("led.Player8", 0x80056, Sel)
