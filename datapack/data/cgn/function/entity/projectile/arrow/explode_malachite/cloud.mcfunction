data merge entity @s {Radius:1f,ReapplicationDelay:20,RadiusPerTick:0,RadiusOnUse:0f,Duration:200,DurationOnUse:0,Age:0,WaitTime:0,potion_contents:{custom_effects:[{id:"minecraft:poison",amplifier:1,duration:300,show_particles:1b,show_icon:1b,ambient:0b}]}}
data modify entity @s Owner set from storage cgn:storage root.temp.owner
execute store result entity @s Radius float 1 run scoreboard players get $temp cgn.dummy