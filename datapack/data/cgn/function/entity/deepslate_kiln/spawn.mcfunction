particle minecraft:soul_fire_flame ~ ~-0.5 ~ 0.4 0.4 0.4 0.01 10
scoreboard players add @s cgn.animation_timer 1
execute if entity @s[scores={cgn.animation_timer=2}] run function cgn:entity/deepslate_kiln/stop_spawning