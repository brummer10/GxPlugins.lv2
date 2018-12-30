# GxPlugins.lv2
GxPlugins.lv2 is a set of extra standalone lv2 plugins designed to compliment the Guitarix project. Each plugin exists as its own submodule under this repository.

## Plugin Summary

*Disclaimer* The product names modeled in this software are trademarks of their respective companies that do not endorse and are not associated or affiliated with this simulation. All trademarks are the property of their respective holders.

#### Overdrive
* GxBottleRocket.lv2 - Based on the [Mesa V1 Bottle Rocket](http://mesaboogie.com/support/out-of-production/v-1-bottle-rocket.html) tube overdrive
* GxDOP250.lv2 - Based on the [Analog Man DOD OD-250 Yellow Overdrive](https://www.buyanalogman.com/DOD_OD_250_p/am-dod-250.htm)
* GxGuvnor.lv2 - Based on the [Marshall "The Guv'nor" Overdrive](https://marshall.com/marshall-amps/products/pedals/gv-2-guvnor-plus)
* GxHotBox.lv2 - Based on the [Matchless Hot Box](http://matchlessamplifiers.com/pedals/hotbox-iii) tube overdrive
* GxSD1.lv2 - Based on the [Boss SD-1 Super Overdrive](https://www.boss.info/us/products/sd-1/)
* GxSD2Lead.lv2 - Based on the [Boss SD-2 Dual Overdrive](http://www.bossarea.com/boss-sd-2-dual-overdrive/)

#### Fuzz/Distortion
* GxAxisFace.lv2 - Based on the [Axis Face Silicon](http://fuzzcentral.ssguitar.com/axisface.php) fuzz
* GxFz1b.lv2 - Based on the Robert Moog-designed [Maestro FZ-1B](https://en.wikipedia.org/wiki/Maestro_FZ-1_Fuzz-Tone) fuzz
* GxFz1s.lv2 - Based on the [Maestro FZ-1S Super-Fuzz](https://en.wikipedia.org/wiki/Maestro_FZ-1_Fuzz-Tone)
* GxHyperion.lv2 - Based on the Devi Ever FX Hyperion fuzz
* GxHeathkit.lv2 - Based on the [Heathkit TA-28](http://harmony.demont.net/heathkit.php) distortion/booster/fuzz
* GxKnightFuzz.lv2 - Based on the [Basic Audio Knight Fuzz](http://www.basicaudio.net/pedal-details.php?pedal=30) fuzz
* GxLiquidDrive.lv2 - Based on the [Liquid Drive](http://fuzzcentral.ssguitar.com/liquid.php) fuzz, a modified [Ross Distortion](http://www.home-wrecker.com/ross.html)
* GxSuppaToneBender.lv2 - Based on the [Colorsound Supa Tonebender](https://en.wikipedia.org/wiki/Tone_Bender) which, in turn, is based on the [Electro-Harmonix Big Muff π](https://en.wikipedia.org/wiki/Big_Muff)
* GxSaturator.lv2 - Based on the Joe Satriani-specified [Vox Satchurator](https://www.joesatrianiuniverse.com/gear/vox-js-pedals/satchurator/) distortion
* GxSunFace.lv2 - Based on the [Analog Man Sun Face](http://www.analogman.com/fuzzface.htm) fuzz
* GxSuperFuzz.lv2 - Based on the [Univox Super-Fuzz](https://en.wikipedia.org/wiki/Univox_Super-Fuzz)
* GxToneMachine.lv2 - Based on the [Foxx Tone Machine](www.cbcpedals.com/product-p/tone-machine.htm) fuzz
* GxTubeDistortion.lv2 - Generic tube distortion based on http://www.montagar.com/~patj/tubedist.gif
* GxVintageFuzzMaster.lv2 - Based on the Devi Ever Vintage Fuzz Master
* GxVoodoFuzz.lv2 - Based on the [Voodoo Lab SuperFuzz](http://www.voodoolab.com/superfuzz.htm). It's basically a Bosstone circuit, followed by the tone control of the [Foxx Tone Machine](www.cbcpedals.com/product-p/tone-machine.htm) in parralel with a [Devi Ever Dark Boost](https://reverb.com/p/devi-ever-fx-dark-boost).

#### Amplifiers
* GxMicroAmp.lv2 - A simple booster 
* GxVBassPreAmp.lv2 - Simulation of the 1984 [Vox Venue Bass 100 Pre Amp](https://www.korguk.com/voxcircuits/) section
* GxSVT.lv2 - Based on the [Ampeg SVT-CL Bass Head](https://ampeg.com/products/classic/svtcl/) 
* GxVmk2.lv2 - Based on Vox MKII solid state preamp of the late 60s
* GxUvox720k - Based on [Vox-style amps](https://www.voxamps.com), probably the [JMI Vox UL730](http://www.voxshowroom.com/uk/amp/730.html)... need input from brummer

#### Other
* GxQuack.lv2 - Autowah
* GxSlowGear.lv2 - Based on the [Boss Gx SlowGear](http://www.bossarea.com/boss-sg-1-slow-gear/), attack-smoothing, auto-swelling pedal of the early 80s

###### Build and installation

Dependencies:
- libc6-dev
- libcairo2-dev
- libx11-dev
- x11proto-dev
- lv2-dev

On Ubuntu/Debian: 
```
sudo apt install libc6-dev libcairo2-dev libx11-dev x11proto-dev lv2-dev
```
NOTE: These packages may have different names on different distributions. GxPlugins.lv2 has no configure script, so make will simply fail when one of these packages isn't found.

## Build 

```
git submodule init
git submodule update
make
make install # will install into ~/.lv2 ... AND/OR....
sudo make install # will install into /usr/lib/lv2
```
## Debian package

You can build a Debian package directly with:
```
dpkg-buildpackage -rfakeroot -uc -us -b
```

## Images

###### GxBottleRocket.lv2
![GxBottleRocket](https://github.com/brummer10/GxBottleRocket.lv2/raw/master/GxBottleRocket.png)
###### GxHotBox.lv2
![GxHotBox](https://github.com/brummer10/GxHotBox.lv2/raw/master/GxHotBox.png)
###### GxVBassPreAmp.lv2
![GxVBassPreAmp](https://github.com/brummer10/GxVBassPreAmp.lv2/raw/master/GxVBassPreAmp.png)
###### GxSuppaToneBender.lv2
![GxSuppaToneBender](https://raw.githubusercontent.com/brummer10/GxSuppaToneBender.lv2/master/GxSuppaToneBender.png)
###### GxHyperion.lv2
![GxHyperion](https://raw.githubusercontent.com/brummer10/GxHyperion.lv2/master/GxHyperion.png)
###### GxVoodoFuzz.lv2
![GxVoodooFuzz](https://raw.githubusercontent.com/brummer10/GxVoodoFuzz.lv2/master/GxVoodooFuzz.png)
###### GxSaturator.lv2
![GxSaturator](https://github.com/brummer10/GxSaturator.lv2/raw/master/saturator.png)
###### GxVintageFuzzMaster.lv2
![GxVintageFuzzMaster](https://github.com/brummer10/GxVintageFuzzMaster.lv2/raw/master/GxVintageFuzzMaster.png)
###### GxSuperFuzz.lv2
![GxSuperFuzz](https://raw.githubusercontent.com/brummer10/GxSuperFuzz.lv2/master/GxSuperFuzz.png)
###### GxVmk2.lv2
![GxVmk2](https://raw.githubusercontent.com/brummer10/GxVmk2.lv2/master/GxVmk2.png)
###### GxUVox720k.lv2
![GxUVox720k](https://raw.githubusercontent.com/brummer10/GxUVox720k.lv2/master/GxUVox720k.png)
###### GxSlowGear.lv2
![GxSlowGear](https://raw.githubusercontent.com/brummer10/GxSlowGear.lv2/master/GxSlowGear.png)
###### GxGuvnor.lv2
![GxGuvnor](https://raw.githubusercontent.com/brummer10/GxGuvnor.lv2/master/GxGuvnor.png)
###### GxToneMachine.lv2
![GxToneMachine](https://raw.githubusercontent.com/brummer10/GxToneMachine.lv2/master/GxToneMachine.png)
###### GxSD1.lv2
![GxSD1](https://github.com/brummer10/GxSD1.lv2/raw/master/GxSD1.png)
###### GxSD2Lead.lv2
![GxSD2Lead](https://github.com/brummer10/GxSD2Lead.lv2/raw/master/GxSD2Lead.png)
###### GxQuack.lv2
![GxQuack](https://raw.githubusercontent.com/brummer10/GxQuack.lv2/master/GxQuack.png)
###### GxSVT.lv2
![GxSVT](https://raw.githubusercontent.com/brummer10/GxSVT.lv2/master/GxSVT.png)
###### GxHeathkit.lv2
![GxHeathkit](https://raw.githubusercontent.com/brummer10/GxHeathkit.lv2/master/GxHeathkit.png)
###### GxKnightFuzz.lv2
![GxKnightFuzz](https://raw.githubusercontent.com/brummer10/GxKnightFuzz.lv2/master/GxKnightFuzz.png)
###### GxFz1b.lv2
![GxFz1b](https://raw.githubusercontent.com/brummer10/GxFz1b.lv2/master/GxFz1b.png)
###### GxFz1s.lv2
![GxFz1s](https://raw.githubusercontent.com/brummer10/GxFz1s.lv2/master/GxFz1s.png)
###### GxAxisFace.lv2
![GxAxisFace](https://raw.githubusercontent.com/brummer10/GxAxisFace.lv2/master/GxAxisFace.png)
###### GxSunFace.lv2
![GxSunFace](https://raw.githubusercontent.com/brummer10/GxSunFace.lv2/master/GxSunFace.png)
###### GxLiquidDrive.lv2
![GxLiqidDrive](https://raw.githubusercontent.com/brummer10/GxLiquidDrive.lv2/master/GxLiquidDrive.png)
###### GxDOP250.lv2
![GxDOP250](https://raw.githubusercontent.com/brummer10/GxDOP250.lv2/master/GxDOP250.png)
###### GxTubeDistortion.lv2
![GxTubeDistortion](https://raw.githubusercontent.com/brummer10/GxTubeDistortion.lv2/master/GxTubeDistortion.png)
###### GxMicroAmp.lv2
![GxMicroAmp](https://raw.githubusercontent.com/brummer10/GxMicroAmp.lv2/master/GxMicroAmp.png)
