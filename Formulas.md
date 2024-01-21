Indexing is 0-based
Hex number is the enemy entry number in each section->difficulty table

# Forest

## Hildebear

### Jump

0.2 x 0x4a attack0

### Foie
unknown

## Dragon

### Fire Breath
0.2 x 0x11 movement0

### Multishot
0.2 x 0x11 movement1

### Tunnel
0.2 x 0x11 movement2

# Caves

## Poison lily
### Megid level
0x4 movement6

## Nar lily
### Megid level
0x5 movement6

## Nano dragon

### 2 Bullets 
0.2 x 0x1a movement7

### Single 
0.2 x 0x1a movement6

## Pofuilly Slime

### Tentacle
0.2 x ATP

### Spit
0.2 x idle movement speed (x30)

## Pan Arms

### red beam 
0.2 x 0x31 movement2

### Blue beam
0.2 x idle_animation_speed (49 0x31)

## DE ROL LE

### Orb wave
'idle_animation_speed'@0xf * .2 + 1
### Beam
'idle_move_speed'@0xf + 1

### mines 
0xf movement2 + 1

# Mines

## Gillchic

### Laser 
0.2 x movement[9]

## Dubchic

### Laser 
0.2 x movement[9]

## Canadine

### Zonde
0.2 x 0x07 movement1

## Canane

### Zonde
0.2 x 0x09 movement1


## GARANZ

### Missiles 
0.2 x 0x1d movement8

# Ruins

## Chaos Bringer

### Charge 
0xd movement8 x 0.2

### Cannon
min: 0.2 x 0xd movement9
max: double

## Chaos Sorcerer

### Rafoie
Tech level = 0xA one of movement6,7,8. (Values are same N-VH)
Damage = (Tech power + 0.5 * 0xA MST)/5

### Gibarta
Tech level = 0xA one of movement6,7,8. (Values are same N-VH)
Damage = (Tech power + 0.5 * 0xA MST)/5

### Grants
Tech level = 0xA one of movement6,7. (Values are same)
Damage = (Tech power + 0.5 * 0xA MST)/5

### Megid
Level comes from either 0xA movement6 or 0xA movement7

## Dark Gunner

### Shot 
0.2 x 0x1e movement9

## Dark Falz 1

### Divine punishment 
0x36 mov[8]/5+mst/10

### Rafoie
Level comes from 0x36 movement6
Damage = (Tech power + 0.5 0x36 MST)/5

### Rabarta
Level comes from 0x36 movement7
Damage = (Tech power + 0.5 0x36 MST)/5

## Dark Falz 2

### Divine punishment =
0x36 mov[8]/5+mst/10
USES DARK FALZ 1 ROW PARAMETER BUT ITS OWN MST

### Life drain 
50 + 0.2 0x37mst + 0x37 movement7

### Rafoie
Level comes from 0x36 movement6
Damage = (Tech power + 0.5 0x37 MST)/5

### Rabarta
Level comes from 0x36 movement7
Damage = (Tech power + 0.5 0x37 MST)/5

## Dark Falz 3

### Orb 
.1 x 0x38 mst + .2 x 0x38movement10


### swipe 
0.2 0x38 atp + 0.1 0x38 mst

### Megid level 
movement 0x38,unknown_a4 (0-based)

### Grants
Tech level from 0x38 movement6
Damage = (Tech power + 0.5 0x38 MST)/5