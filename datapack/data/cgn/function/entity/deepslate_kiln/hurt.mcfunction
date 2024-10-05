execute if score $hurt cgn.dummy matches 9 run tag @s add cgn.deepslate_kiln.hurt
execute if score $hurt cgn.dummy matches 9 run playsound cgn:entity.deepslate_kiln.damage
execute store result entity @s item.components."minecraft:custom_model_data" int 1 run scoreboard players add $cmd cgn.dummy 1