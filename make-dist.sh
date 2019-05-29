#!/bin/sh

VER=`git describe --tags $(git rev-list --tags --max-count=1) | cut -c2-`

dist=gxplugins.lv2_$VER.tar.gz

git submodule update --init
cd .. && rm -rf $dist && tar cfz $dist GxPlugins.lv2
