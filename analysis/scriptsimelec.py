import os
for scale in [1,10,50,100,200]:
    for iter in [10]:
        script = "python simeleconevent.py -det helix"
        torun = script + " -scale " + str(scale) + " -iter " + str(iter)
        print torun
        os.system(torun)
    
