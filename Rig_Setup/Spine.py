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
    cmds.move(0, 136.886, 23.252, pn + '_ikClavicleCtrl.scalePivot', pn + '_ikClavicleCtrl.rotatePivot', absolute=True)
    cmds.move(0, 132.478, 60.495, pn+'_ikClavicleCtrl_grp.scalePivot', pn+'_ikClavicleCtrl_grp.rotatePivot', absolute=True)
    cmds.select(d=True)
    #mid IK ctrl
    lib.controlType('midbody',pn+'_ikMidCtrl',1,pn+'_ikMidCtrl_grp')
    cmds.closeCurve(pn+'_ikMidCtrl',
                    ch = True,
                    ps = False,
                    rpo = True,
                    blendBias = 0.5,
                    blendKnotInsertion = False,
                    parameter = 0.1
                    )

    cmds.move(0, 136.886, 23.252, pn+'_ikMidCtrl_grp.scalePivot', pn+'_ikMidCtrl_grp.rotatePivot', absolute=True)
    cmds.move(0, 136.886, 23.252, pn + '_ikMidCtrl.scalePivot', pn + '_ikMidCtrl.rotatePivot', absolute=True)
    cmds.select(d=True)
    # back IK ctrl
    lib.controlType('hip',pn+'_ikHipCtrl',1,pn+'_ikHipCtrl_grp')
    cmds.move(0, 142.05, -29.629, pn + '_ikHipCtrl.scalePivot', pn + '_ikHipCtrl.rotatePivot', absolute=True)
    cmds.move(0, 142.05, -29.629, pn+'_ikHipCtrl_grp.scalePivot', pn+'_ikHipCtrl_grp.rotatePivot', absolute=True)
    cmds.select(d=True)

    #control joints for spine

    cmds.joint(p=(0,142.05,-29.625),n=pn+'_ikHipCtrl_jnt')
    cmds.select(d=True)
    cmds.joint(p=(0, 1136.886, 23.252), n=pn + '_ikMidCtrl_jnt')
    cmds.select(d=True)
    cmds.joint(p=(0, 132.478, 60.495), n=pn + '_ikClavicleCtrl_jnt')
    cmds.select(d=True)

    #parenting to respective ctrl

    cmds.parent(pn+'_ikHipCtrl_jnt',pn+'_ikHipCtrl')
    cmds.parent(pn + '_ikMidCtrl_jnt', pn+'_ikMidCtrl')
    cmds.parent(pn + '_ikClavicleCtrl_jnt', pn+'_ikClavicleCtrl')
    cmds.select(d=True)
    #skinning to curve

    cmds.skinCluster(pn+'_Spine_ikCurve',pn+'_ikClavicleCtrl_jnt',pn+'_ikMidCtrl_jnt',pn+'_ikHipCtrl_jnt',
                     n = 'ikBind')

    cmds.group(pn+'_ikHipCtrl_grp',pn+'_ikMidCtrl_grp',pn+'_ikClavicleCtrl_grp',n=pn+'ikCtrl_grp')
    cmds.parent(pn+'ikCtrl_grp',pn+'_ikSpineSystem_grp')

    #advanced twist controls

    cmds.spaceLocator(p=(0,200,-29.69),n='hipTwistLoc',a=0)
    cmds.move(0, 142.05, -29.629, 'hipTwistLoc.scalePivot','hipTwistLoc.rotatePivot', absolute=True)
    cmds.parent('hipTwistLoc',pn+'_ikHipCtrl_jnt')

    cmds.spaceLocator(p=(0, 200, 60.495), n='clavTwistLoc')
    cmds.move(0, 132.478, 60.495, 'clavTwistLoc.scalePivot', 'clavTwistLoc.rotatePivot', absolute=True)
    cmds.parent('clavTwistLoc', pn + '_ikClavicleCtrl_jnt')

    cmds.setAttr(pn+'_ikSplineHandle.dTwistControlEnable',1)
    cmds.setAttr(pn + '_ikSplineHandle.dWorldUpType', 4)

    cmds.connectAttr('hipTwistLoc.worldMatrix','Ciervo_ikSplineHandle.dWorldUpMatrix',f=1)
    cmds.connectAttr('clavTwistLoc.worldMatrix', 'Ciervo_ikSplineHandle.dWorldUpMatrixEnd', f=1)














