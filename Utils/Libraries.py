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

def bakeCustomToolPivot(pos=1, ori=1 , objectName=None):
    # Check 1) must have an object(s) selected
    cmds.select(objectName)
    objects = cmds.ls(sl=1, transforms=1)
    shapes = cmds.ls(sl=1, shapes=1)
    if len(shapes) > 0:
        transforms = cmds.listRelatives(path=1, parent=1, type='transform')
        objects += transforms

    if len(objects) == 0:
        cmds.error("m_bakeCustomToolPivot.kNoObjectsSelectedError")
        return None

    # Check 2) must be in the move/rotate/scale tool
    currentCtx = cmds.currentCtx()
    contextList = ["moveSuperContext", "manipMoveContext", "RotateSuperContext",
                   "manipRotateContext", "scaleSuperContext", "manipScaleContext"]


    if currentCtx not in contextList:
        cmds.error("m_bakeCustomToolPivot.kWrongToolError")
        return None

    # Check 3) must be in custom orientation mode
    customOri = []
    pivotModeActive = 0
    customModeActive = 0
    if currentCtx == "moveSuperContext" or currentCtx == "manipMoveContext":
        customOri = cmds.manipMoveContext('Move', q=1, orientAxes=1)
        pivotModeActive = cmds.manipMoveContext('Move', q=1, editPivotMode=1)
        customModeActive = cmds.manipMoveContext('Move', q=1, mode=1) / 6
    elif currentCtx == "RotateSuperContext" or currentCtx == "manipRotateContext":
        customOri = cmds.manipRotateContext('Rotate', q=1, orientAxes=1)
        pivotModeActive = cmds.manipRotateContext('Rotate', q=1, editPivotMode=1)
        customModeActive = cmds.manipRotateContext('Rotate', q=1, mode=1) / 3
    elif currentCtx == "scaleSuperContext" or currentCtx == "manipScaleContext":
        customOri = cmds.manipScaleContext('Scale', q=1, orientAxes=1)
        pivotModeActive = cmds.manipScaleContext('Scale', q=1, editPivotMode=1)
        customModeActive = cmds.manipScaleContext('Scale', q=1, mode=1) / 6

    if ori and not pos and not customModeActive:
        cmds.error("m_bakeCustomToolPivot.kWrongAxisOriModeError")
        return None

    # Get custom orientation
    if ori and customModeActive:
        customOri[0] = mel.eval('rad_to_deg({})'.format(customOri[0]))
        customOri[1] = mel.eval('rad_to_deg({})'.format(customOri[1]))
        customOri[2] = mel.eval('rad_to_deg({})'.format(customOri[2]))
        # Set object(s) rotation to the custom one (preserving child transform positions and geometry positions)
        cmds.rotate(customOri[0], customOri[1], customOri[2], objects, a=1, pcp=1, pgp=1, ws=1, fo=1)

    if pos:
        for object in objects:
            # Get pivot in parent space
            # object = 'pSphere4'
            old = [0, 0, 0]
            m = cmds.xform(object, q=1, m=1)
            p = cmds.xform(object, q=1, os=1, sp=1)
            old[0] = (p[0] * m[0] + p[1] * m[4] + p[2] * m[8] + m[12])
            old[1] = (p[0] * m[1] + p[1] * m[5] + p[2] * m[9] + m[13])
            old[2] = (p[0] * m[2] + p[1] * m[6] + p[2] * m[10] + m[14])

            # Zero out pivots
            cmds.xform(objects, zeroTransformPivots=1)

            # Translate object(s) back to previous pivot (preserving child transform positions and geometry positions)
            new = cmds.getAttr(object + ".translate")[0]
            cmds.move((old[0] - new[0]), (old[1] - new[1]), (old[2] - new[2]), object, pcp=1, pgp=1, ls=1, r=1)

    # Exit pivot mode
    if pivotModeActive:
        mel.eval('ctxEditMode;')

    # Set the axis orientation mode back to object
    if ori and customModeActive:
        if currentCtx == "moveSuperContext" or currentCtx == "manipMoveContext":
            cmds.manipMoveContext('Move', e=1, mode=0)
        elif currentCtx == "RotateSuperContext" or currentCtx == "manipRotateContext":
            cmds.manipRotateContext('Rotate', e=True, mode=0)
        elif currentCtx == "scaleSuperContext" or currentCtx == "manipScaleContext":
            cmds.manipScaleContext('Scale', e=1, mode=0)
print(mel.eval('whatIs bakeCustomToolPivot;'))
print(mel.eval('whatIs performBakeCustomToolPivot;'))


