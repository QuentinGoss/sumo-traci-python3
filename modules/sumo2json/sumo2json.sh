#!/bin/sh

# Recursively converts all .net.xml files in the directory to json.

find . | grep -E '*.net.xml' | xargs python3 sumo2json.py --net_xml
