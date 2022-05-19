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
project_Name = "Ciervo"
#Custom controls
def controlType( ctrlType,ctrlName,scale,parentGrpName):
    if ctrlType == 'circle':
        circleCtrl = cmds.circle(n = ctrlName)

        cmds.scale(scale,scale,scale,circleCtrl[0]+'.cv[0:7]')
        cmds.group(ctrlName,n=parentGrpName)

    elif ctrlType == 'curvedTwoArrow':
        curvedtwoArrow = cmds.curve(p=[[0.0, -1.111, -2.426], [0.0, 0.773, -2.292], [0.0, -0.149, -2.089], [0.0, 0.379, -1.765],
                [0.0, 0.92, -0.955], [0.0, 1.111, -0.0], [0.0, 0.92, 0.955], [0.0, 0.379, 1.765], [0.0, -0.145, 2.093],
                [0.0, 0.773, 2.292], [0.0, -1.111, 2.426], [0.0, -0.197, 0.774], [0.0, -0.411, 1.745],
                [0.0, 0.058, 1.444], [0.0, 0.501, 0.782], [0.0, 0.656, -0.0], [0.0, 0.501, -0.782],
                [0.0, 0.058, -1.444], [0.0, -0.415, -1.738], [0.0, -0.197, -0.774], [0.0, -1.111, -2.426]], d=1 , n = ctrlName)
        cmds.scale(scale, scale, scale, curvedtwoArrow + '.cv[0:20]')
        cmds.group(ctrlName, n=parentGrpName)

# Locator placement : Proxy locator in joint positions
def locatorPlacement(skeletonName,vertexOne,vertexTwo):
    vertexPosOne = cmds.pointPosition(f"{skeletonName}.vtx[{vertexOne}]")
    vertexPosTwo = cmds.pointPosition(f"{skeletonName}.vtx[{vertexTwo}]")
    #we get two list and average the values inside zip
    LocatorPos = [(x1 + x2)/2 for (x1, x2) in zip(vertexPosOne, vertexPosTwo)]
    tempLocator = cmds.spaceLocator(name = f"{skeletonName}_ProxyLocator",p=LocatorPos)
    #center pivot the locator
    cmds.xform(tempLocator , cp=1)
    return tempLocator


