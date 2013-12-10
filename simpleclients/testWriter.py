
class wrx(object):


## the main function
    def main(self):
        import pni.io.nx.h5 as nx
        import numpy
        
        f = nx.create_file("test.h5",True,0);
        
        g = f.create_field("test","int32",[1000,2048],[1,4])
        buf = numpy.zeros(shape=(1000,2048),dtype="int32")

        print "buf", buf.shape
        for i in range(len(buf.shape)):
            if buf.shape[i] > g.shape[i]:
                g.grow(i, buf.shape[i]- g.shape[i])
        g.write(buf)        
        g.close()
        f.close()


if __name__ == "__main__":
    import resource
    import gc
    wr = wrx()
    gc.collect()
#    print "INIT", gc.get_referrers(wr)
    print "BEFORE", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    wr.main()
    wr = None
    gc.collect()
#    print "FINAL",gc.get_referrers(wr)
    print "AFTER", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
            
                
            
            

