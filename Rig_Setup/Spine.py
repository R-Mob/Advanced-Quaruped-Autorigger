import maya.cmds as cmds
from Utils import Libraries as lib
from Utils import JointPlacement as jPlacement
def ikSpineSystem():
    #grouping the locators and joint systems
    cmds.group(lib.project_Name+'_ikSpine_01_jnt',n=lib.project_Name+'_ikSpineSystem_grp')
    cmds.parent("SpineLoc_grp",lib.project_Name+'_ikSpineSystem_grp')
    cmds.select(d=True)

