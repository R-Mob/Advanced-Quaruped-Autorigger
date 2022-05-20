import maya.cmds as cmds
from Utils import Libraries as lib
from Utils import JointPlacement as jPlacement
pn = lib.project_Name
def ikSpineSystem():
    #grouping the locators and joint systems
    cmds.group(lib.project_Name+'_ikSpine_01_jnt',n=pn+'_ikSpineSystem_grp')
    cmds.parent("SpineLoc_grp",pn+'_ikSpineSystem_grp')
    cmds.hide("SpineLoc_grp")
    cmds.select(d=True)
    #ik spline handle
    cmds.ikHandle( n = pn+'_ikSplineHandle',
                   startJoint = pn+'_ikSpine_01_jnt',
                   endEffector = pn+'_ikSpine_06_jnt',
                   solver = 'ikSplineSolver',
                   createCurve = True,
                   simplifyCurve = False,
                   rootOnCurve = True,
                   parentCurve = False,
                   snapCurve = False,
                   numSpans = 6

                   )
    #renaming and grouping
    cmds.rename("curve1",pn+'_Spine_ikCurve')
    cmds.parent(pn+'_ikSplineHandle',pn+'_Spine_ikCurve',pn+'_ikSpineSystem_grp')
    cmds.select(d=True)
    #setting up controllers
    #front clavicle ctrl
    lib.controlType('clavicle',pn+'_ikClavicleCtrl',1,pn+'_ikClavicleCtrl_grp')
