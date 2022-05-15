"""
setup Maya
import sys
import importlib as importlib
#Path import
if rigDir in sys.path:
    sys.path.remove(rigDir)
rigDir = "C:/Users/rupam/PycharmProjects/Advanced-Quaruped-Autorigger"
sys.path.append(rigDir)
#Modules import
import Utils
from Utils import Libraries
from Utils import JointPlacement
#Functions import
importlib.reload(JointPlacement)
jp = Utils.JointPlacement.ProxyLoc()

"""
import maya.cmds as cmds

# Locator placement : Proxy locator in joint positions
def locatorPlacement(skeletonName,vertexOne,vertexTwo):
    vertexPosOne = cmds.pointPosition(f"{skeletonName}.vtx[{vertexOne}]")
    vertexPosTwo = cmds.pointPosition(f"{skeletonName}.vtx[{vertexTwo}]")
    #we get two list and average the values inside zip
    LocatorPos = [(x1 + x2)/2 for (x1, x2) in zip(vertexPosOne, vertexPosTwo)]
    tempLocator = cmds.spaceLocator(name = f"{skeletonName}_ProxyLocator",p=LocatorPos)
    #center pivto the locator
    cmds.xform(tempLocator , cp=1)