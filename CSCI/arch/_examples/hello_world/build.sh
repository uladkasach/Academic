#!/bin/bash
CL_ARGUMENTS_ARRAY=( "$@" )

## configure environment
#CURRENT_DIR=`pwd`;
export PATH=$PATH:$HOME/esp32/xtensa-esp32-elf/bin # path to compiler
export IDF_PATH=~/esp32/esp-idf # root where esp-idf is 'installed'

## make the file
cd "src";
if [[ " ${CL_ARGUMENTS_ARRAY[@]} " =~ " --config " ]]; then
    make menuconfig # trigger config if required
fi;
make
