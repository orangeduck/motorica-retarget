import os

def select_branch(node):
    if isinstance(node, pyfbsdk.FBModel):
        
        node.Selected = True
        
        for child in node.Children:
            select_branch(child)

def deselect_all():
    selected_models = FBModelList()
    FBGetSelectedModels(selected_models, None, True)
    for select in selected_models:
        select.Selected = False;

data_path = 'C:/Data/motorica_dance_dataset/bvh'
out_path = 'C:/Dev/motorica-retarget/fbx'

bvh_files = [f for f in os.listdir(data_path) if f.endswith('.bvh')]

for file in bvh_files:
    
    bvh_file = os.path.join(data_path, file)
    fbx_file = os.path.join(out_path, file.replace('.bvh', '.fbx'))

    print('Creating %s' % fbx_file)
    
    FBApplication().FileOpen('C:/Dev/motorica-retarget/motorica_character.fbx')
    FBApplication().FileImport(bvh_file, True)
    
    options = FBFbxOptions(True)
    options.TakeSpan = FBTakeSpanOnLoad.kFBLeaveAsIs
    
    FBApplication().FileMerge('C:/Dev/motorica-retarget/Geno.fbx', False, options)
    
    FBSystem().Scene.Characters[1].InputCharacter = FBSystem().Scene.Characters[0]
    FBSystem().Scene.Characters[1].InputType = FBCharacterInputType.kFBCharacterInputCharacter
    FBSystem().Scene.Characters[1].ActiveInput = True
    
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorLeftWrist').Data = 100.0
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorLeftWristRotation').Data = 100.0
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorRightWrist').Data = 100.0
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorRightWristRotation').Data = 100.0
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorLeftFingerBase').Data = 100.0
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorLeftFingerBaseRotation').Data = 100.0
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorRightFingerBase').Data = 100.0
    # FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorRightFingerBaseRotation').Data = 100.0
    FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorChest').Data = 100.0
    FBSystem().Scene.Characters[1].PropertyList.Find('ReachActorChestRotation').Data = 100.0

    deselect_all()
    select_branch(FBFindModelByLabelName('Hips'))
    
    print('Plotting...')

    start_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
    stop_frame = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame()
    FBSystem().CurrentTake.LocalTimeSpan = FBTimeSpan(FBTime(0,0,0,start_frame), FBTime(0,0,0,stop_frame))

    FBSystem().CurrentTake.PlotTakeOnSelected(FBTime(0,0,0,1))

    FBFindModelByLabelName('Geno').Selected = True
    
    save_options = FBFbxOptions(False)
    save_options.SaveSelectedModelsOnly = True
    
    print('Saving FBX...')
    
    FBApplication().FileSave(fbx_file, save_options)
    
    # break