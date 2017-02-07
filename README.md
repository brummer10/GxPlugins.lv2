# GxPlugins.lv2
A set of extra lv2 plugins from the guitarix project.

This repository contain the following extra GxPlugins as submodules.

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
###### GxSD1.lv2.lv2
![GxSD1](https://github.com/brummer10/GxSD1.lv2/raw/master/GxSD1.png)


###### BUILD DEPENDENCY’S 

the following packages are needed to build the GxPlugs:

- libc6-dev
- libgtk2.0-dev
- libstdc++6-dev
- lv2-dev

note that those packages could have different, but similar names 
on different distributions. There is no configure script, 
make will simply fail when one of those packages isn't found.

## BUILD 

$ git submodule init

$ git submodule update

$ make

$ make install

will install into ~/.lv2

$ sudo make install

will install into /usr/lib/lv2

(*) Other product names modeled in this software are trademarks 
of their respective companies that do not endorse and are not associated 
or affiliated with this simulation. 
All other trademarks are the property of their respective holders.
