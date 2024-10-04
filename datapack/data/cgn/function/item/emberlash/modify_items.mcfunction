execute if items entity @s weapon.mainhand *[item_name='{"translate": "item.cgn.emberlash"}'] run return run function cgn:item/emberlash/charge {slot:"mainhand"}
execute if items entity @s weapon.offhand *[item_name='{"translate": "item.cgn.emberlash"}'] run return run function cgn:item/emberlash/charge {slot:"offhand"}

scoreboard players remove @s[gamemode=!creative] cgn.electroplasm.current 10
