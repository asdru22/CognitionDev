summon interaction ~ ~ ~ {response:1b,width:0.5f,height:0.7f,Tags:["smithed.block","cgn.wispthorn","cgn.tick","cgn.block","cgn.interaction","cgn.wispthorn_setup","cgn.potted"],Passengers:[{id:"item_display",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.0f,-0.2f,0.f],scale:[0.75f,0.75f,0.75f]},item:{id:"minecraft:stone",count:1b,components:{"minecraft:item_model":"cgn:block/wispthorn","minecraft:custom_model_data":1}}}]}

execute as @n[type=interaction,tag=cgn.wispthorn_setup,limit=1,sort=nearest,distance=..1] run function cgn:block/wispthorn/setup