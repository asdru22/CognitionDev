scoreboard players remove $temp cgn.dummy 1
execute as @n[type=!#cgn:inanimate,predicate=cgn:entity_properties/hostile_target,distance=..10,dx=0] positioned ~-0.5 ~-0.5 ~-0.5 if entity @s[dx=0] run function cgn:entity/projectile/pyroplastic_beam/apply_damage with entity @n[type=item_display,tag=cgn.pyroplastic_beam_temp] item.components."minecraft:custom_data".cgn

execute if score $temp cgn.dummy matches 1.. positioned ^ ^ ^-0.1 if block ~ ~ ~ #cgn:raycast_ignore run function cgn:entity/projectile/pyroplastic_beam/raycast