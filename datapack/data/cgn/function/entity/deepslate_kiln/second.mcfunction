execute if entity @s[tag=cgn.deepslate_kiln.spawning] run return run function cgn:entity/deepslate_kiln/spawn

execute if entity @s[scores={cgn.animation_timer=7}] run return run function cgn:entity/deepslate_kiln/start_spawning
execute if entity @p[gamemode=!creative,gamemode=!spectator,distance=..16] run return run scoreboard players add @s cgn.animation_timer 1
scoreboard players reset @s cgn.animation_timer