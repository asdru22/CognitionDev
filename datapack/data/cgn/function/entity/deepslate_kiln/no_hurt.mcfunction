execute store result score $cmd cgn.dummy run data get entity @s item.components."minecraft:custom_model_data"
execute store result entity @s item.components."minecraft:custom_model_data" int 1 run scoreboard players remove $cmd cgn.dummy 1

tag @s remove cgn.deepslate_kiln.hurt