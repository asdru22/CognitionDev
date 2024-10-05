execute unless predicate cgn:entity_properties/has_vehicle run return run kill
execute on vehicle store result score $hurt cgn.dummy run data get entity @s HurtTime
execute store result score $cmd cgn.dummy run data get entity @s item.components."minecraft:custom_data".cgn.animation
# hurt
execute if score $hurt cgn.dummy matches 1.. run return run function cgn:entity/deepslate_kiln/hurt

# clear hurt effects
execute if entity @s[tag=cgn.deepslate_kiln.hurt] run return run function cgn:entity/deepslate_kiln/no_hurt

# default
execute store result entity @s item.components."minecraft:custom_model_data" int 1 run scoreboard players get $cmd cgn.dummy