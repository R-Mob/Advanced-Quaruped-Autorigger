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
import maya.mel as mel

project_Name = "Ciervo"
#Custom controls
def controlType( ctrlType,ctrlName,scale,parentGrpName):
    if ctrlType == 'circle':
        circleCtrl = cmds.circle(n = ctrlName)

        cmds.scale(scale,scale,scale,circleCtrl[0]+'.cv[0:7]')
        cmds.group(ctrlName,n=parentGrpName)
    #custom controllers
    elif ctrlType == 'clavicle':
        clavicleCtrl = cmds.curve(p=[[23.016, 129.082, 44.824], [23.809, 124.719, 47.165], [25.288, 120.343, 54.998],
                                     [21.337, 129.628, 63.298], [17.019, 140.578, 60.457], [12.909, 150.272, 55.588],
                                     [6.993, 157.418, 52.31], [0.0, 159.444, 51.365], [-6.993, 157.418, 52.31], [-12.909, 150.272, 55.588],
                                     [-17.019, 140.578, 60.457], [-21.337, 129.628, 63.298], [-25.288, 120.343, 54.998], [-23.809, 124.719, 47.165],
                                     [-23.016, 129.082, 44.824]],d=3,n=ctrlName)

        cmds.scale(scale, scale, scale, clavicleCtrl + '.cv[0:14]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'midbody':
        midbodyCtrl = cmds.curve(p=[[16.534, 151.064, 23.714], [0.0, 158.031, 23.714], [-16.534, 151.064, 23.714],
                                    [-35.268, 119.06, 19.27], [-19.44, 84.038, 20.365], [-0.0, 80.634, 20.365],
                                    [19.44, 84.038, 20.365], [35.268, 119.06, 19.27]],d=3,n=ctrlName)


        cmds.scale(scale, scale, scale, midbodyCtrl + '.cv[0:7]')
        cmds.group(ctrlName, n=parentGrpName)

    elif ctrlType == 'hip':
        hipCtrl = cmds.curve(p=[[30.0, 118.268, -45.637], [30.0, 119.783, -41.928], [30.126, 121.802, -38.32], [28.875, 128.553, -27.229],
                                [27.073, 141.562, -36.108], [16.24, 154.802, -35.507], [-0.0, 158.208, -35.84], [-16.24, 154.802, -35.507],
                                [-27.073, 141.562, -36.108], [-28.875, 128.553, -27.229], [-30.126, 121.802, -38.32], [-30.0, 119.783, -41.928],
                                [-30.0, 118.268, -45.637]],d=5,n=ctrlName)



        cmds.scale(scale, scale, scale, hipCtrl + '.cv[0:12]')
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




