# Targets entities within macroed distance

$execute as @e[type=minecraft:item_display,distance=..$(distance),tag=cgn.prevents_hoppers] at @s positioned ~ ~-1 ~ run function cgn:block/vanilla/hopper_updating/fill