import maya.cmds as cmds
from . import Libraries as lib

# Proxy locator placement
def ProxyLoc():
    #Spine Skeleton Chain
    lib.locatorPlacement('thoriac_vertibrae_C19_C',2971,3192)
    lib.locatorPlacement('thoriac_vertibrae_C18_C',2971,3192)
    lib.locatorPlacement('thoriac_vertibrae_C17_C', 2971, 3192)
    lib.locatorPlacement('thoriac_vertibrae_C16_C', 2971, 3192)
    lib.locatorPlacement('thoriac_vertibrae_C15_C', 2971, 3192)
    lib.locatorPlacement('thoriac_vertibrae_C14_C', 2971, 3192)
    lib.locatorPlacement('thoriac_vertibrae_C13_C', 1025, 2660)
    lib.locatorPlacement('thoriac_vertibrae_C12_C', 1025, 2660)
    lib.locatorPlacement('thoriac_vertibrae_C11_C', 1025, 2660)
    lib.locatorPlacement('thoriac_vertibrae_C10_C', 1025, 2660)
    lib.locatorPlacement('thoriac_vertibrae_C09_C', 1025, 2660)
    lib.locatorPlacement('thoriac_vertibrae_C08_C', 2659, 1275)
    lib.locatorPlacement('thoriac_vertibrae_C07_C', 2659, 1275)
    lib.locatorPlacement('thoriac_vertibrae_C06_C', 325, 1319)
    lib.locatorPlacement('thoriac_vertibrae_C05_C', 325, 1325)
    lib.locatorPlacement('thoriac_vertibrae_C04_C', 330, 1325)
    lib.locatorPlacement('thoriac_vertibrae_C03_C', 326, 1324)
    lib.locatorPlacement('thoriac_vertibrae_C02_C', 338, 1324)
    lib.locatorPlacement('thoriac_vertibrae_C01_C', 2057, 2732)


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



