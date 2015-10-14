#!/usr/bin/env python
#   This file is part of nexdatas - Tango Server for NeXus data writer
#
#    Copyright (C) 2012-2013 DESY, Jan Kotanski <jkotan@mail.desy.de>
#
#    nexdatas is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    nexdatas is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with nexdatas.  If not, see <http://www.gnu.org/licenses/>.
# \package  ndtstools tools for ndts
## \file simpleScanClient.py
# example of simple client


import sys, os
import time
from datetime import datetime
from pytz import timezone
import pytz


import random

from math import exp

import PyTango 

xml = """<?xml version='1.0'?>
<definition>
  <group type="NXentry" name="entry">
    <attribute name="postrun" type="NX_CHAR">
      <strategy mode="INIT"/>
      <datasource type="CLIENT">
	<record name="test" />
      </datasource>
    </attribute>  
  </group>
</definition>
"""


## the main function    
def main():
    fname = sys.argv[1] if sys.argv else "/tmp/test.nxs"
    device = "p09/tdw/r228"
    
    dpx = PyTango.DeviceProxy(device)
    print " Connected to: ", device
    dpx.Init()
    
    dpx.FileName = fname

    print "opening the H5 file"
    dpx.OpenFile()
    
    dpx.XMLSettings = xml

    print "opening the entry"
    dpx.OpenEntry()



if __name__ == "__main__":
    main()

            
                
            
            


#  LocalWords:  nicePlot
