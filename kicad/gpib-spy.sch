EESchema Schematic File Version 2
LIBS:PL_analog_ICs
LIBS:PL_capacitors
LIBS:PL_comms
LIBS:PL_connectors
LIBS:PL_diodes
LIBS:PL_displays
LIBS:PL_GPIB
LIBS:PL_inductors
LIBS:PL_LEDs
LIBS:PL_microcontrollers
LIBS:PL_mounting_holes
LIBS:PL_opamps
LIBS:PL_opto
LIBS:PL_power
LIBS:PL_references
LIBS:PL_regulators
LIBS:PL_relays
LIBS:PL_resistors
LIBS:PL_sensors
LIBS:PL_switchers
LIBS:PL_switches
LIBS:PL_transistors
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:gpib-spy-cache
EELAYER 27 0
EELAYER END
$Descr USLetter 11000 8500
encoding utf-8
Sheet 1 1
Title ""
Date "7 jul 2017"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L GPIB P4
U 1 1 595D2861
P 7450 3550
F 0 "P4" H 7000 4475 40  0000 L BNN
F 1 "GPIB FEMALE" H 7900 4475 40  0000 R BNN
F 2 "~" H 7050 3650 60  0000 C CNN
F 3 "~" H 7050 3650 60  0000 C CNN
	1    7450 3550
	1    0    0    -1  
$EndComp
$Comp
L GPIB P1
U 1 1 595D2870
P 3900 3550
F 0 "P1" H 3450 4475 40  0000 L BNN
F 1 "GPIB MALE" H 4350 4475 40  0000 R BNN
F 2 "~" H 3500 3650 60  0000 C CNN
F 3 "~" H 3500 3650 60  0000 C CNN
	1    3900 3550
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR01
U 1 1 595D2943
P 3200 4550
F 0 "#PWR01" H 3200 4350 50  0001 C CNN
F 1 "GND" H 3200 4450 40  0000 C CNN
F 2 "" H 3200 4550 50  0000 C CNN
F 3 "" H 3200 4550 50  0000 C CNN
	1    3200 4550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 595D2A12
P 8150 4550
F 0 "#PWR02" H 8150 4350 50  0001 C CNN
F 1 "GND" H 8150 4450 40  0000 C CNN
F 2 "" H 8150 4550 50  0000 C CNN
F 3 "" H 8150 4550 50  0000 C CNN
	1    8150 4550
	1    0    0    -1  
$EndComp
$Comp
L CONN_5X2 P2
U 1 1 595D2EB3
P 5100 4900
F 0 "P2" V 5050 4900 40  0000 C CNN
F 1 "CONN_5X2" V 5150 4900 40  0000 C CNN
F 2 "~" H 5100 5050 60  0000 C CNN
F 3 "~" H 5100 5050 60  0000 C CNN
	1    5100 4900
	1    0    0    -1  
$EndComp
$Comp
L CONN_5X2 P3
U 1 1 595D2EC2
P 6250 4900
F 0 "P3" V 6200 4900 40  0000 C CNN
F 1 "CONN_5X2" V 6300 4900 40  0000 C CNN
F 2 "~" H 6250 5050 60  0000 C CNN
F 3 "~" H 6250 5050 60  0000 C CNN
	1    6250 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 2750 6850 2750
Wire Wire Line
	4500 2850 6850 2850
Wire Wire Line
	4500 2950 6850 2950
Wire Wire Line
	4500 3050 6850 3050
Wire Wire Line
	4500 3150 6850 3150
Wire Wire Line
	4500 3250 6850 3250
Wire Wire Line
	4500 3350 6850 3350
Wire Wire Line
	4500 3450 6850 3450
Wire Wire Line
	4500 3650 6850 3650
Wire Wire Line
	4500 3750 6850 3750
Wire Wire Line
	4500 3850 6850 3850
Wire Wire Line
	4500 4050 6850 4050
Wire Wire Line
	4500 4150 6850 4150
Wire Wire Line
	4500 4250 6850 4250
Wire Wire Line
	4500 4350 6850 4350
Wire Wire Line
	4500 4450 6850 4450
Wire Wire Line
	3300 3750 3200 3750
Wire Wire Line
	3200 3750 3200 4550
Wire Wire Line
	3300 4450 3200 4450
Connection ~ 3200 4450
Wire Wire Line
	3200 4350 3300 4350
Connection ~ 3200 4350
Wire Wire Line
	3200 4250 3300 4250
Connection ~ 3200 4250
Wire Wire Line
	3200 4150 3300 4150
Connection ~ 3200 4150
Wire Wire Line
	3200 4050 3300 4050
Connection ~ 3200 4050
Wire Wire Line
	3200 3950 3300 3950
Connection ~ 3200 3950
Wire Wire Line
	3200 3850 3300 3850
Connection ~ 3200 3850
Wire Wire Line
	8050 3750 8150 3750
Wire Wire Line
	8150 3750 8150 4550
Wire Wire Line
	8050 4450 8150 4450
Connection ~ 8150 4450
Wire Wire Line
	8050 4350 8150 4350
Connection ~ 8150 4350
Wire Wire Line
	8050 4250 8150 4250
Connection ~ 8150 4250
Wire Wire Line
	8050 4150 8150 4150
Connection ~ 8150 4150
Wire Wire Line
	8050 4050 8150 4050
Connection ~ 8150 4050
Wire Wire Line
	8050 3950 8150 3950
Connection ~ 8150 3950
Wire Wire Line
	8050 3850 8150 3850
Connection ~ 8150 3850
Wire Wire Line
	4850 4700 4850 2750
Connection ~ 4850 2750
Wire Wire Line
	5350 4700 5350 2850
Connection ~ 5350 2850
Wire Wire Line
	4850 4800 4800 4800
Wire Wire Line
	4800 4800 4800 2950
Connection ~ 4800 2950
Wire Wire Line
	5350 4800 5400 4800
Wire Wire Line
	5400 4800 5400 3050
Connection ~ 5400 3050
Wire Wire Line
	4850 4900 4750 4900
Wire Wire Line
	4750 4900 4750 3150
Connection ~ 4750 3150
Wire Wire Line
	5350 4900 5450 4900
Wire Wire Line
	5450 4900 5450 3250
Connection ~ 5450 3250
Wire Wire Line
	4850 5000 4700 5000
Wire Wire Line
	4700 5000 4700 3350
Connection ~ 4700 3350
Wire Wire Line
	5350 5000 5500 5000
Wire Wire Line
	5500 5000 5500 3450
Connection ~ 5500 3450
$Comp
L GND #PWR03
U 1 1 595EF4F1
P 5450 5200
F 0 "#PWR03" H 5450 5000 50  0001 C CNN
F 1 "GND" H 5450 5100 40  0000 C CNN
F 2 "" H 5450 5200 50  0000 C CNN
F 3 "" H 5450 5200 50  0000 C CNN
	1    5450 5200
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 595EF4F7
P 5900 5200
F 0 "#PWR04" H 5900 5000 50  0001 C CNN
F 1 "GND" H 5900 5100 40  0000 C CNN
F 2 "" H 5900 5200 50  0000 C CNN
F 3 "" H 5900 5200 50  0000 C CNN
	1    5900 5200
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR05
U 1 1 595EF4FD
P 4750 5200
F 0 "#PWR05" H 4750 5000 50  0001 C CNN
F 1 "GND" H 4750 5100 40  0000 C CNN
F 2 "" H 4750 5200 50  0000 C CNN
F 3 "" H 4750 5200 50  0000 C CNN
	1    4750 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4850 5100 4750 5100
Wire Wire Line
	4750 5100 4750 5200
Wire Wire Line
	5350 5100 5450 5100
Wire Wire Line
	5450 5100 5450 5200
$Comp
L GND #PWR06
U 1 1 595EF5DB
P 6600 5200
F 0 "#PWR06" H 6600 5000 50  0001 C CNN
F 1 "GND" H 6600 5100 40  0000 C CNN
F 2 "" H 6600 5200 50  0000 C CNN
F 3 "" H 6600 5200 50  0000 C CNN
	1    6600 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	6500 5100 6600 5100
Wire Wire Line
	6600 5100 6600 5200
Wire Wire Line
	6000 5100 5900 5100
Wire Wire Line
	5900 5100 5900 5200
Wire Wire Line
	6000 4700 6000 3650
Connection ~ 6000 3650
Wire Wire Line
	6500 4700 6500 3750
Connection ~ 6500 3750
Wire Wire Line
	6000 4800 5950 4800
Wire Wire Line
	5950 4800 5950 3850
Connection ~ 5950 3850
Wire Wire Line
	6500 4800 6550 4800
Wire Wire Line
	6550 4800 6550 4050
Connection ~ 6550 4050
Wire Wire Line
	6000 4900 5900 4900
Wire Wire Line
	5900 4900 5900 4150
Connection ~ 5900 4150
Wire Wire Line
	6500 4900 6600 4900
Wire Wire Line
	6600 4900 6600 4250
Connection ~ 6600 4250
Wire Wire Line
	6000 5000 5850 5000
Wire Wire Line
	5850 5000 5850 4350
Connection ~ 5850 4350
Wire Wire Line
	6500 5000 6650 5000
Wire Wire Line
	6650 5000 6650 4450
Connection ~ 6650 4450
$EndSCHEMATC
