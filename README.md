# Unit Under Test

This is a test harness for testing a unit that might need reboots and might need to connect/disconnect
from one or more Ethernet interfaces.

The USB-Serial cable allows the test harness to talk to a shell on the target unit.

The Ethernet cross-bar allows the test harness to plug/unplug two network jacks and swap them around.

The powered-outlet allows the test harness to perform a hard power-cycle while testing.

![](https://github.com/topherCantrell/UnitUnderTest/blob/master/art/schematic.jpg)