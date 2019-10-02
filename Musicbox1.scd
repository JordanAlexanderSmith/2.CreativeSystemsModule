
b = Buffer.read(s, "snare.wav".resolveRelative);
b.play;
// buses from which to read and write incoming data: available *everywhere* holding last value written
~xBus = Bus.control(s,1);
~yBus = Bus.control(s,1);
~buttBus = Bus.control(s,1);
~switchBus = Bus.control(s, 1)

(
SynthDef("default", {| out = 0 |
    Out.ar(out, SinOsc.ar(~xBus.kr(1).lag(0.1), mul: ~yBus.kr(1).lag(0.1)));
}).add;
)

x = Synth.newPaused("default");
x.run
x.run(false)

SerialPort.devices;

//Serial Path to my Macbook
p = ArduinoSMS("/dev/tty.SLAB_USBtoUART", 9600);

(
~xLo = 1000;
~xHi = 0;
~yLo = 1000;
~yHi = 0;

p.action = {|... msg|

	msg.postln;

	if (msg[0] < ~xLo) { ~xLo = msg[0]; ("~xLo = " + ~xLo).postln };
	if (msg[0] > ~xHi) { ~xHi = msg[0]; ("~xHi = " + ~xHi).postln };

	if (msg[1] < ~yLo) { ~yLo = msg[1]; ("~yLo = " + ~yLo).postln };
	if (msg[1] > ~yHi) { ~yHi = msg[1]; ("~yHi = " + ~yHi).postln };

	if (msg[2] == 1 ) { b.play };
	if (msg[3] == 1 ) { x.run };
	if (msg[3] == 0 ) { x.run(false) };

	//if (msg[3] == 1) { play { SinOsc.ar(~xBus.kr(1).lag(0.1), mul: ~yBus.kr(1).lag(0.1)) } };
	// write the outputs to the control buses and scale appropriately

	~xBus.set(msg[0].linlin(~xLo, ~xHi, 100, 1500));
	~yBus.set(msg[1].linlin(~yLo, ~yHi, 0.01, 1.0));


};
)


p.close; 