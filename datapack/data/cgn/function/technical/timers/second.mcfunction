execute store result score #difficulty cgn.dummy run difficulty

execute as @e[tag=cgn.second,type=#cgn:affected/second] at @s run function cgn:technical/timers/entity_second
execute as @a at @s run function cgn:entity/player/timers/second

schedule function cgn:technical/timers/second 1s replace