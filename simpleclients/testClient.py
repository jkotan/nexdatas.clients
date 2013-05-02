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
## \file simpleClient.py
# first example of simple client


## the main function
def main(i):
    import sys, os
    import time
    import gc
    
    import PyTango
    if  len(sys.argv) < 3:
        print "usage: simpleClient.py  <XMLfile>  <pid>"
        return

    xmlf = sys.argv[1]
    if os.path.exists(xmlf):
        
        sp = xmlf.split(".")
        print sp
        if sp[-1] == 'xml' :
            fname = ''.join(sp[0:-1])
        else:
            fname = xmlf
        fname = fname.strip() + ".h5"
        print "storing in ", fname 
        pid = sys.argv[2].strip()
        print "Pid:", pid
        device = "p09/tdw/r228"
    

        print "########################################"
        print "loaded", i
        for l in open('/proc/%s/status' % pid):
            if l.startswith('VmSize'):
                print l.rstrip()
            if l.startswith('VmRSS'):
                print l.rstrip()
        print "########################################"
        
        dpx = PyTango.DeviceProxy(device)
        dpx.set_timeout_millis(25000)
        dpx.Init()
        print " Connected to: ", device
    
        xml = open(xmlf, 'r').read()


        dpx.FileName = fname

        print "opening the H5 file"
        dpx.OpenFile()

        dpx.TheXMLSettings = xml

        print "opening the entry"
        dpx.OpenEntry()

        print "recording the H5 file"
        dpx.record('{"data": {"emittance_x": 0.1},  "triggers":["trigger1", "trigger2"]  }')
            
        print "sleeping for 1s"
#        time.sleep(1)

        print "recording the H5 file"
        dpx.record('{"data": {"emittance_x": 0.3} }')


        print "sleeping for 1s"
#        time.sleep(1)
            
        print "recording the H5 file"
        dpx.record('{"data": {"emittance_x": 0.6},  "triggers":["trigger1"]  }')
            

        print "sleeping for 1s"
#        time.sleep(1)

        print "recording the H5 file"
        dpx.record('{"data": {"emittance_x": 0.5} }')

        print "sleeping for 1s"
#        time.sleep(1)

        print "recording the H5 file"
        dpx.record('{"data": {"emittance_x": 0.1},  "triggers":["trigger2"]  }')
            


        print "closing the  entry"
        dpx.closeEntry()
        print "closing the H5 file"
        dpx.closeFile()

        del dpx

        print "########################################"
        print "cleared", i
        for l in open('/proc/%s/status' % pid):
            if l.startswith('VmSize'):
                print l.rstrip()
            if l.startswith('VmRSS'):
                print l.rstrip()
        print "########################################"
                


if __name__ == "__main__":
    for i in range(1000):
        main(i)
            
                
            
            

