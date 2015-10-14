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
## \file simpleScanWriter.py
# example of simple writer




class wrx(object):


## the main function
    def main(self):
        from ndts import TangoDataWriter as TDW
        import sys


        # Create a TDW object
    ## instance of TangoDataWriter
        tdw = TDW.TangoDataWriter()
        tdw.fileName = "test.h5"
        
        tdw.numThreads = 1
        
    ## xml file name
    #    xmlf = "../XMLExamples/test.xml"
        xmlf = "../XMLExamples/MNI.xml"
        
        print "usage: TangoDataWriter.py  <XMLfile1>  <XMLfile2>  ...  <XMLfileN>  <H5file>"

    ## No arguments
        argc = len(sys.argv)
        if argc > 2:
            tdw.fileName = sys.argv[argc-1]
            
        if argc > 1:
            print "opening the H5 file"
            tdw.openNXFile()



            for i in range(1, argc-1):
                xmlf = sys.argv[i]
                
            ## xml string    
                xml = open(xmlf, 'r').read()
                tdw.xmlSettings = xml
                
                print "opening the data entry "
                tdw.openEntry()
                
                print "recording the H5 file" 
                
                tdw.record('{ }')
            
            
                print "sleeping for 1s"
                print "recording the H5 file"
                print "recording the H5 file" 
                tdw.record('{}')
                print "sleeping for 1s"
                print "recording the H5 file"
                
                tdw.record('{}')
                print "closing the data entry "
                tdw.closeEntry()
                
                
            print "closing the H5 file"
            tdw.closeNXFile()



if __name__ == "__main__":
    import resource
    import gc
    wr = wrx()
    gc.collect()
    print "INIT", gc.get_referrers(wr)
    print "BEFORE", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    wr.main()
    wr = None
    gc.collect()
    print "FINAL",gc.get_referrers(wr)
    print "AFTER", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
            
                
            
            

