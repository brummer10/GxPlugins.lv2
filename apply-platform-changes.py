#!/usr/bin/env python
# vim:fdm=indent:

# This script mimics the changes to GxCreamMachine to support building for MSWin,
# applies them to all subprojects and prepares them for commit.
# It will be not required, once all projects have been converted.
# Included changes:
#   first: https://github.com/brummer10/GxCreamMachine.lv2/commit/9a8b85a145c6a46d1fe9eea3e66765f34aa66709
#   last:  https://github.com/brummer10/GxCreamMachine.lv2/commit/6750b115f76d37fd0bafa740ff682a62da9ff09d

import re
import os

project = ''

def patch_makefile(MakefileIn, MakefileOut):
    global project
    oschecks = """\t# check OS specific stuff
	OS := $(shell echo $$OS)
	UNAME_S := $(shell uname -s)
	GUI_PLATFORM_DIR = ./gui
	# cross compilation (e.g.: PKG_CONFIG_PATH=/usr/local/pkgconfig make CROSS=x86_64-w64-mingw32- mod)
	ifneq (,$(findstring mingw,$(CROSS)))
		# Found
		TARGET = Windows
		STRIP = $(CROSS)strip
		PKGCONFIG = $(CROSS)pkg-config
		CC = $(CROSS)cc
		CXX = $(CROSS)g++
		LD = $(CROSS)ld
	else
		# Not found
		ifeq ($(UNAME_S), Linux) #LINUX
			TARGET = Linux
		endif
		ifeq ($(OS), Windows_NT) #WINDOWS
			TARGET = Windows
		endif
		ifeq ($(UNAME_S), Darwin) #APPLE
			TARGET = Apple
		endif
	endif
	ifeq ($(TARGET), Linux)
		ABI_CFLAGS = -Wl,-z,nodelete
		ABI_CXXFLAGS = -Wl,-z,relro,-z,now
		ABI_LDFLAGS = -Wl,-z,noexecstack
		GUI_LIBS = -L/usr/X11/lib -lX11
		LIB_EXT = so
		GUI_PLATFORM_FILES = $(GUI_PLATFORM_DIR)/gx_platform_linux.c
	endif
	ifeq ($(TARGET), Windows)
		ECHO += -e
		ABI_LDFLAGS = -static -lpthread
		GUI_LIBS = -liconv -lstdc++
		PKGCONFIG_FLAGS = --static
		LIB_EXT = dll
		TTLUPDATE = sed -i '/lv2:binary/ s/\.so/\.dll/ ' $(BUNDLE)/manifest.ttl
		TTLUPDATEGUI = sed -i '/a guiext:X11UI/ s/X11UI/WindowsUI/ ; /guiext:binary/ s/\.so/\.dll/ ' $(BUNDLE)/$(NAME).ttl
		GUI_PLATFORM_FILES = $(GUI_PLATFORM_DIR)/gx_platform_mswin.c
	endif
	ifeq ($(TARGET), Apple)
		# insert magic here
		GUI_PLATFORM_FILES = $(GUI_PLATFORM_DIR)/gx_platform_apple.c
	endif"""
    make_fp = open(MakefileIn)
    make_data = make_fp.read()
    make_fp.close()
    # -- global replacements --
    # replace fixed C/CXX/LDFLAGS by variables
    make_data = make_data.replace('-Wl,-z,relro,-z,now', '$(ABI_CXXFLAGS)')
    make_data = make_data.replace('-Wl,-z,noexecstack', '$(ABI_LDFLAGS)')
    make_data = make_data.replace('-Wl,-z,nodelete', '$(ABI_CFLAGS)')
    # replace fixed library extension ".so" by variable LIB_EXT
    make_data = re.sub(r'\.so\b', r'.$(LIB_EXT)', make_data)
    # replace fixed "echo" by variable ECHO
    make_data = re.sub(r'\becho\b', r'$(ECHO)', make_data)
    # replace fixed "pkg-config" by variable PKGCONFIG
    make_data = re.sub(r'\bpkg-config\b', r'$(PKGCONFIG)', make_data)
    # -- changes to specific sections --
    make_lines = make_data.split('\n')
    out = []
    in_all = False
    in_mod = False
    for i, line in enumerate(make_lines):
        # insert ECHO before STRIP
        if (line.find('\tSTRIP') > -1):
            out.append('\tECHO ?= echo')
            out.append(line)
            # append definition of PKGCONFIG after STRIP
            out.append('\tPKGCONFIG ?= pkg-config')
        # replace flags by variables (pkgconfig, X11) in GUI_LDFLAGS
        elif (line.find('GUI_LDFLAGS') > -1):
            line = line.replace('pkg-config', 'pkg-config $(PKGCONFIG_FLAGS)')
            line = line.replace('-L/usr/X11/lib -lX11', '$(GUI_LIBS)')
            # also add PKGCONFIG_FLAGS (for passing "-static")
            line = line.replace('$(PKGCONFIG)', '$(PKGCONFIG) $(PKGCONFIG_FLAGS)')
            out.append(line)
        # rename source x11ui->gui + add gx_platform_[aplle|linux|mswin].c in GUI_OBJECTS
        elif (line.find('GUI_OBJECTS') > -1):
            line = line.replace('x11ui.c', 'gui.c $(GUI_PLATFORM_FILES)')
            out.append(line)
        # insert missing LGREEN before BLUE
        elif (line.find('\tBLUE') > -1):
            out.append('\tLGREEN = "\\033[1;92m"')
            out.append(line)
        # we are inside target "all : "
        elif (line.find('all : ') > -1):
            out.append(line)
            in_all = True
        # we are inside target "mod : "
        elif (line.find('mod : ') > -1):
            out.append(line)
            in_all = False
            in_mod = True
        # we are outside target "mod : " and "all : "
        elif (line.find('check : ') > -1):
            out.append(line)
            in_mod = False
        # add ttl-patch-commands to target "mod : " and "all : " after "@mv /:*"
        elif (line.find('\t@mv ./*.$(LIB_EXT)') > -1):
            out.append(line)
            if (in_all):
                out.append('\t$(TTLUPDATE)')
                out.append('\t$(TTLUPDATEGUI)')
            if (in_mod):
                out.append('\t$(TTLUPDATE)')
        # append new OS-Check block after VER
        elif (line.find('\tVER = ') > -1):
            out.append(line)
            out.append(oschecks)
        # read the NAME of the project
        elif (line.find('\tNAME = ') > -1):
            out.append(line)
            project = re.sub(r'.* = ', r'', line)
        # remove definition of "ECHO" found in some older Makefiles
        elif (line.find('\tECHO = $(shell which $(ECHO)) -e') > -1):
            pass # remove
        # add ABI_FLAGS to LDFLAGS
        elif (line.find('\tLDFLAGS += -I. -shared') > -1):
            line = line.replace('-lm $(ABI_LDFLAGS) ', '$(ABI_LDFLAGS) -lm')
            out.append(line)
        # remove accidental space
        elif (line.find('\tOBJECTS = plugin/$(NAME).cpp ') > -1):
            line = line.replace('.cpp ', '.cpp')
            out.append(line)
        # be verbose on generating object files
        elif (line.find('\t-@cd ./gui && $(LD)') > -1):
            line = line.replace('@cd', 'cd')
            out.append(line)
        # append PKGCONFIG_FLAGS (e.g. --static)
        elif (line.find('\t -fdata-sections -Wl,--gc-sections') > -1):
            line +=  ' `$(PKGCONFIG) $(PKGCONFIG_FLAGS) --cflags lv2`'
            out.append(line)
                
        else:
            out.append(line)
    make_fp = open(MakefileOut, 'w', newline='\n')
    make_fp.write('\n'.join(out))
    make_fp.close()

def find_line(haystack, needle):
    for i, line in enumerate(haystack):
        if line.find(needle) > -1:
            return i
    return -1

def save_snip(snip, filename):
    fp = open(filename, 'w', newline='\n')
    fp.write('\n'.join(snip))
    fp.close()

def patch_sourcefile():
    global project
    src_fp = open('gui/' + project + '_x11ui.c')
    src_data = src_fp.read()
    src_fp.close()
    # global: rename parentXwindow
    src_data = src_data.replace('parentXwindow', 'parentWindow')
    src_lines = src_data.split('\n')
    # copy common files
    guidir = 'gui/'
    gx_gui_header = [ '// vim:ts=4:sw=4:noet:',
                      '#ifndef __GX_GUI_H__',
                      '#define __GX_GUI_H__ 1\n',
                      '#include "gui/gx_platform.h"' ]
    forward_preamble = [
        '/*---------------------------------------------------------------------',
        '-----------------------------------------------------------------------',	
        '			forward declaration of compatibility functions',
        '			(have to be implemented in gx_platform_*.c)',
        '-----------------------------------------------------------------------',
        '----------------------------------------------------------------------*/']
    common = [ 'gx_platform_apple.c',
               'gx_platform_linux.c',
               'gx_platform_mswin.c',
               'gx_platform.h' ]
    #          'gx_gui.h' # generated
    for file in common:
        fp = open('../' + file)
        file_data = fp.read()
        fp.close()
        file_data = file_data.replace('gx_CreamMachine', project)
        fp = open(guidir + file, 'w', newline='\n')
        fp.write(file_data)
        fp.close
    # remove single forward declaration
    startidx = find_line(src_lines, '// forward declaration to resize')
    endidx = find_line(src_lines, 'load png data from') - 2
    snip_gui_c_forward = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_fp = open('gui/___00_gui_forward.h', 'w', newline='\n')
    src_fp.write('\n'.join(snip_gui_c_forward))
    src_fp.close()
    # shared functions (platform diversion)
    forwards_common = [
        'bool gx_gui_open_display(' + project + 'UI *ui);',
        'void gx_gui_create_window_and_surface(' + project + 'UI *ui);',
        'void gx_gui_register_controller_message(' + project + 'UI *ui);',
        'void gx_gui_destroy_main_window(' + project + 'UI *ui);',
        'void gx_gui_resize_surface(' + project + 'UI *ui);',
        'void gx_gui_send_controller_event(' + project + 'UI *ui, int controller);' ]
    # shared functions (add forward, remove "static")
    shared = [ 'void resize_event',
               'void event_handler',
               'void _expose',
               'void controller_expose',
               'void button1_event',
               'void scroll_event',
               'void set_previous_controller_active',
               'void set_next_controller_active',
               'void key_event',
               'void set_key_value',
               'void get_last_active_controller',
               'void motion_event',
               'bool get_active_ctl_num' ]
    # collect forward definitions; remove "static" keyword
    forwards = []
    for func in shared:    
        startidx = find_line(src_lines, func)
        if (startidx > -1):
            if (src_lines[startidx][0:7] == 'static '):
                src_lines[startidx] = src_lines[startidx][7:]
            forwards.append(src_lines[startidx].replace(' {', ';'))
    # move #includes up
    dstidx = src_lines.index('#include <string.h>')
    srcidx = src_lines.index('#include <stdlib.h>')
    src_lines.insert(dstidx + 1, src_lines.pop(srcidx))
    srcidx = src_lines.index('#include <stdio.h>')
    src_lines.insert(dstidx + 1, src_lines.pop(srcidx))
    if (src_lines[srcidx] == ''):
        src_lines.pop(srcidx)
    # remove cairo-xlib
    srcidx = src_lines.index('#include <cairo-xlib.h>')
    src_lines.pop(srcidx)
    # remove X11 includes
    src_lines.pop(src_lines.index('#include <X11/Xutil.h>'))
    src_lines.pop(src_lines.index('#include <X11/keysym.h>'))
    srcidx = src_lines.index('#include <X11/Xatom.h>')
    src_lines.pop(srcidx)
    if (src_lines[srcidx] == ''):
        src_lines.pop(srcidx)
    # append gui/gx_gui.h
    srcidx = src_lines.index('#include "./' + project + '.h"')
    src_lines.insert(srcidx + 1, '#include "gui/gx_gui.h"')
    # block defining CONTROLS and min/max
    startidx = find_line(src_lines, '/*-----')
    endidx = find_line(src_lines, 'define some MACROS') - 2 # 2 lines above
    snip_gui_h_controls = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    save_snip(snip_gui_h_controls, 'gui/___01_gui_controls.h')
    # block defining EXTLD/LDVAR/LDLEN
    startidx = find_line(src_lines, '/*-----')
    endidx = find_line(src_lines, '// png\'s linked in')
    snip_platform_h_extld = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    save_snip(snip_platform_h_extld, 'gui/___02_platform_extld.h')
    # block with platform specific members of main window struct
    startidx = find_line(src_lines, 'Display *dpy')
    endidx = find_line(src_lines, 'Atom DrawController') + 1
    snip_gui_h_platstructs = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_lines.insert(startidx, '\tplatform_ui_members // platform specific; see gx_Platform.h')
    save_snip(snip_gui_h_platstructs, 'gui/___03a_gui_platformstruct.h')
    # block with structure declarations
    startidx = find_line(src_lines, '/*-----')
    endidx = find_line(src_lines, 'load png data from') - 2 # 2 lines above
    snip_gui_h_structs = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    save_snip(snip_gui_h_structs, 'gui/___03_gui_structs.h')
    # move block with linked binary resources
    startidx = find_line(src_lines, '// png\'s linked in')
    endidx = find_line(src_lines, '/*-----')
    snip_gui_c_res = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    dstidx = find_line(src_lines, '// read png data from')
    for line in reversed(snip_gui_c_res):
        src_lines.insert(dstidx, line)
    save_snip(snip_gui_c_res, 'gui/___03a_gui_res.c')
    # block with XOpenDisplay call
    startidx = find_line(src_lines, 'ui->dpy = XOpenDisplay(0);')
    endidx = find_line(src_lines, 'if (ui->dpy == NULL)') + 1
    snip_gui_c_xopen = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_lines.insert(startidx, '\tif (!gx_gui_open_display(ui)) { // sets ui->dpy (only used by Linux)')
    save_snip(snip_gui_c_xopen, 'gui/___04_gui_xopen.c')
    # block with XCreateWindow call
    startidx = find_line(src_lines, 'ui->win = XCreateWindow')
    endidx = find_line(src_lines, 'ui->cr = cairo_create')
    snip_gui_c_xcreatewin = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_lines.insert(startidx, '\tgx_gui_create_window_and_surface(ui); // sets ui->win and ui->surface')
    save_snip(snip_gui_c_xcreatewin, 'gui/___05_gui_xcreatewin.c')
    # block with DrawController init
    startidx = find_line(src_lines, 'ui->DrawController = XInternAtom')
    endidx = startidx + 1
    snip_gui_c_drawctrl = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_lines.insert(startidx, '\tgx_gui_register_controller_message(ui); // message for redrawing a controller (only used by Linux)')
    save_snip(snip_gui_c_drawctrl, 'gui/___06_gui_drawcontroller.c')
    # block with DestroyWindow call
    startidx = find_line(src_lines, 'XDestroyWindow(ui->dpy')
    endidx = find_line(src_lines, 'XCloseDisplay(ui->dpy') + 1
    snip_gui_c_destroywin = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_lines.insert(startidx, '\tgx_gui_destroy_main_window(ui);')
    save_snip(snip_gui_c_destroywin, 'gui/___07_gui_destroywin.c')
    # block with resize event
    startidx = find_line(src_lines, 'XWindowAttributes attrs;')
    endidx = find_line(src_lines, 'cairo_xlib_surface_set_size') + 1
    snip_gui_c_resize = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_lines.insert(startidx, '\tgx_gui_resize_surface(ui);')
    save_snip(snip_gui_c_resize, 'gui/___08_gui_resize.c')
    # block with send_controller event
    startidx = find_line(src_lines, 'XClientMessageEvent xevent')
    endidx = find_line(src_lines, 'XSendEvent(ui->dpy') + 1
    snip_gui_c_sendcontroller = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    src_lines.insert(startidx, '\tgx_gui_send_controller_event(ui, controller);')
    save_snip(snip_gui_c_sendcontroller, 'gui/___09_gui_sendcontroller.c')
    # block with key_mappings
    startidx = find_line(src_lines, '// map supported key')
    endidx = find_line(src_lines, 'LV2 interface') - 2
    snip_gui_c_keymapping = src_lines[startidx:endidx]
    src_lines[startidx:endidx] = []
    save_snip(snip_gui_c_keymapping, 'gui/___10_gui_keymapping.c')

    # create gx_gui.h from snippets
    src_fp = open('gui/gx_gui.h', 'w', newline='\n')
    src_fp.write('\n'.join(gx_gui_header)+'\n')
    src_fp.write('#include "./' + project + '.h"\n\n')
    src_fp.write('\n'.join(snip_gui_h_controls)+'\n')
    src_fp.write('\n'.join(snip_gui_h_structs))
    src_fp.write('\n// forward declarations (internal)'+'\n')
    src_fp.write('\n'.join(forwards)+'\n')
    src_fp.write('\n')
    src_fp.write('\n'.join(forward_preamble)+'\n\n')
    src_fp.write('\n'.join(forwards_common)+'\n')
    src_fp.write('\n')
    src_fp.write('#endif /* __GX_GUI_H__ */\n')
    src_fp.close()

    # write remnants from gx_*_x11ui.c to gx_*_gui_new.c
    src_fp = open('gui/' + project + '_gui_new.c', 'w', newline='\n')
    src_fp.write('\n'.join(src_lines))
    src_fp.close()

os.system('git submodule init')
os.system('git submodule update')
os.system('git submodule foreach git pull origin master')
# get identical files for all projects fom GxCreamMachine
os.system('cp GxCreamMachine.lv2/gui/gx_platform.h .')
os.system('cp GxCreamMachine.lv2/gui/gx_platform_apple.c .')
os.system('cp GxCreamMachine.lv2/gui/gx_platform_linux.c .')
os.system('cp GxCreamMachine.lv2/gui/gx_platform_mswin.c .')

for dir in os.listdir('.'):
    if (dir.endswith('lv2')):
        if (dir == 'GxCreamMachine.lv2'):
            print('Skipping GxCreamMachine.lv2\n')
        elif (os.path.exists(dir + '/Makefile.org')):
            print('Skipping (Makefile.org exists)\n')
        else:
            print('Entering ' + dir)
            os.chdir(dir)
            os.rename('Makefile', 'Makefile.org')
            patch_makefile('Makefile.org', 'Makefile')
            print('Project: ' + project)
            patch_sourcefile()
            os.chdir('gui')
            os.system('git mv ' + project + '_x11ui.c ' + project + '_gui.c')
            os.system('mv ' + project + '_gui.c ' + project + '_gui_x11.c')
            os.system('mv ' + project + '_gui_new.c ' + project + '_gui.c')
            os.system('git add ' + project + '_gui.c gx_gui.h gx_platform.h '
                    + 'gx_platform_apple.c gx_platform_linux.c gx_platform_mswin.c')
            os.chdir('..') # back to project dir
            os.system('git add Makefile')
            os.chdir('..')

