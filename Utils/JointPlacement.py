import maya.cmds as cmds
from . import Libraries as lib

# Proxy locator placement
def ProxyLoc():
    #Spine Skeleton Chain
    spineLoc01 = lib.locatorPlacement('thoriac_vertibrae_C19_C', 2971, 3192)
    cmds.setAttr(spineLoc01[0]+'Shape.localPositionX', 0)
    spineLoc02 =lib.locatorPlacement('thoriac_vertibrae_C18_C',2971,3192)
    cmds.setAttr(spineLoc02[0] + 'Shape.localPositionX', 0)
    spineLoc03 =lib.locatorPlacement('thoriac_vertibrae_C17_C', 2971, 3192)
    cmds.setAttr(spineLoc03[0] + 'Shape.localPositionX', 0)
    spineLoc04 =lib.locatorPlacement('thoriac_vertibrae_C16_C', 2971, 3192)
    cmds.setAttr(spineLoc04[0] + 'Shape.localPositionX', 0)
    spineLoc05 =lib.locatorPlacement('thoriac_vertibrae_C15_C', 2971, 3192)
    cmds.setAttr(spineLoc05[0] + 'Shape.localPositionX', 0)
    spineLoc06 =lib.locatorPlacement('thoriac_vertibrae_C14_C', 2971, 3192)
    cmds.setAttr(spineLoc06[0] + 'Shape.localPositionX', 0)
    spineLoc07 =lib.locatorPlacement('thoriac_vertibrae_C13_C', 1025, 2660)
    cmds.setAttr(spineLoc07[0] + 'Shape.localPositionX', 0)
    spineLoc08 =lib.locatorPlacement('thoriac_vertibrae_C12_C', 1025, 2660)
    cmds.setAttr(spineLoc08[0] + 'Shape.localPositionX', 0)
    spineLoc09 =lib.locatorPlacement('thoriac_vertibrae_C11_C', 1025, 2660)
    cmds.setAttr(spineLoc09[0] + 'Shape.localPositionX', 0)
    spineLoc10 =lib.locatorPlacement('thoriac_vertibrae_C10_C', 1025, 2660)
    cmds.setAttr(spineLoc10[0] + 'Shape.localPositionX', 0)
    spineLoc11 =lib.locatorPlacement('thoriac_vertibrae_C09_C', 1025, 2660)
    cmds.setAttr(spineLoc11[0] + 'Shape.localPositionX', 0)
    spineLoc12 =lib.locatorPlacement('thoriac_vertibrae_C08_C', 2659, 1275)
    cmds.setAttr(spineLoc12[0] + 'Shape.localPositionX', 0)
    spineLoc13 =lib.locatorPlacement('thoriac_vertibrae_C07_C', 2659, 1275)
    cmds.setAttr(spineLoc13[0] + 'Shape.localPositionX', 0)
    spineLoc14 =lib.locatorPlacement('thoriac_vertibrae_C06_C', 325, 1319)
    cmds.setAttr(spineLoc14[0] + 'Shape.localPositionX', 0)
    spineLoc15 =lib.locatorPlacement('thoriac_vertibrae_C05_C', 325, 1325)
    cmds.setAttr(spineLoc15[0] + 'Shape.localPositionX', 0)
    spineLoc16 =lib.locatorPlacement('thoriac_vertibrae_C04_C', 330, 1325)
    cmds.setAttr(spineLoc16[0] + 'Shape.localPositionX', 0)
    spineLoc17 =lib.locatorPlacement('thoriac_vertibrae_C03_C', 326, 1324)
    cmds.setAttr(spineLoc17[0] + 'Shape.localPositionX', 0)
    spineLoc18 =lib.locatorPlacement('thoriac_vertibrae_C02_C', 338, 1324)
    cmds.setAttr(spineLoc18[0] + 'Shape.localPositionX', 0)
    spineLoc19 =lib.locatorPlacement('thoriac_vertibrae_C01_C', 2057, 2732)
    cmds.setAttr(spineLoc19[0] + 'Shape.localPositionX', 0)


def jointSetup():
    #Spine IK chain
    cmds.select(d=True)

    cmds.joint(p=(cmds.objectCenter('thoriac_vertibrae_C19_C_ProxyLocator',gl=1)), n=lib.project_Name + '_ikSpine_01_jnt')
    cmds.joint(p=(cmds.objectCenter('thoriac_vertibrae_C16_C_ProxyLocator',gl=1)), n=lib.project_Name + '_ikSpine_02_jnt')
    cmds.joint(lib.project_Name + '_ikSpine_02_jnt', e=True, zso=True, oj='xyz')

    cmds.joint(p=(cmds.objectCenter('thoriac_vertibrae_C13_C_ProxyLocator',gl=1)), n=lib.project_Name + '_ikSpine_03_jnt')
    cmds.joint(lib.project_Name + '_ikSpine_03_jnt', e=True, zso=True, oj='xyz')

    cmds.joint(p=(cmds.objectCenter('thoriac_vertibrae_C08_C_ProxyLocator',gl=1)), n=lib.project_Name + '_ikSpine_04_jnt')
    cmds.joint(lib.project_Name + '_ikSpine_04_jnt', e=True, zso=True, oj='xyz')

    cmds.joint(p=(cmds.objectCenter('thoriac_vertibrae_C05_C_ProxyLocator',gl=1)), n=lib.project_Name + '_ikSpine_05_jnt')
    cmds.joint(lib.project_Name + '_ikSpine_05_jnt', e=True, zso=True, oj='xyz')

    cmds.joint(p=(cmds.objectCenter('thoriac_vertibrae_C01_C_ProxyLocator',gl=1)), n=lib.project_Name + '_ikSpine_06_jnt')
    cmds.joint(lib.project_Name + '_ikSpine_06_jnt', e=True, zso=True, oj='xyz')

    cmds.select(lib.project_Name + '_ikSpine_01_jnt')
    cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)

    cmds.select(lib.project_Name + '_ikSpine_06_jnt')
    cmds.joint(e=True, zso=True, oj='none')






