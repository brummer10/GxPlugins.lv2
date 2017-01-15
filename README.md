# GxPlugins.lv2
A set of extra lv2 plugins from the guitarix project.

This repository contain the following extra GxPlugins as submodules.

###### GxBottleRocket.lv2
###### GxHotBox.lv2
###### GxVBassPreAmp.lv2
###### GxSuppaToneBender.lv2
###### GxHyperion.lv2
###### GxVoodoFuzz.lv2
###### GxSaturator.lv2
###### GxVintageFuzzMaster.lv2
###### GxSuperFuzz.lv2
###### GxVmk2.lv2
###### GxUVox720k.lv2
###### GxSlowGear.lv2
###### GxGuvnor.lv2
###### GxToneMachine.lv2


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
$ make install

will install into ~/.lv2

$ sudo make install

will install into /usr/lib/lv2

(*) Other product names modeled in this software are trademarks 
of their respective companies that do not endorse and are not associated 
or affiliated with this simulation. 
All other trademarks are the property of their respective holders.
