#!/usr/bin/python
import os
import sys
import glob
import inspect
import unittest
from sets import Set

print sys.path
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
print cmd_folder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
print cmd_subfolder

if len(sys.argv) > 1:
    testCases = glob.glob('test_*')
    testTargets = Set([])
    for testTarget in sys.argv:
        if testTarget == "test_all":
            testTargets = testCases
            break
        else:
            for testCase in testCases:
                if testCase == testTarget:
                    testTargets.add(testCase)
                    break
    if len(testTargets) > 0:
        suiteList = []
        for testTarget in testTargets:
            cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],testTarget)))
            if cmd_subfolder not in sys.path:
                sys.path.insert(0, cmd_subfolder)
            suiteList.append(unittest.defaultTestLoader.loadTestsFromName(testTarget+"."+testTarget))
        mainSuite = unittest.TestSuite(suiteList)
        unittest.TextTestRunner().run(mainSuite)
    else:
        "No Proper Test Targets Specified"    
else:
    print "No Test Targets Specified"
