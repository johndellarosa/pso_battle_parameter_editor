Indexing is 0-based
Hex number is the enemy entry number in each section->difficulty table

## Hildebear

### Jump

0.2 x attack[0]

## Gillchic

### Laser 
0.2 x movement[9]

## Dubchic

### Laser 
0.2 x movement[9]

## nano dragon

### 2 bullets 
0.2 x 0x1a movement7

### single 
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


## GARANZ

### Missiles 
0.2 x 0x1d movement8

## Chaos Bringer

### Charge 
'0xd unknown_m5' x 0.2

## Dark Gunner

### Shot 
0.2 x 0x1e movement9

## Dark Falz 1

### Divine punishment 
0x36 mov[8]/5+mst/10

## Dark Falz 2

### Divine punishment =
0x36 mov[8]/5+mst/10
USES DARK FALZ 1 ROW PARAMETER BUT ITS OWN MST

### Life drain 
50 + 0.2 0x37mst + 0x37 movement7

## Dark Falz 3

### Orb 
.1 x 0x38 mst + .2 x 0x38movement10


### swipe 
0.2 0x38 atp + 0.1 0x38 mst

### Megid level 
movement 0x38,unknown_a4 (0-based)