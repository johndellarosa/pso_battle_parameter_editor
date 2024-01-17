import enum
import struct
import numpy as np
import os
import os.path
import pandas as pd

# Created by John Della Rosa 2024
# Uses information gotten from Newserv


class EnemyStatEp1:
    MOTHMANT = 0x00
    MONEST = 0x01
    SAVAGE_WOLF = 0x02
    BARBAROUS_WOLF = 0x03
    POISON_LILY = 0x04
    NAR_LILY = 0x05
    SINOW_BEAT = 0x06
    CANADINE = 0x07
    CANADINE_GROUP = 0x08
    CANANE = 0x09
    CHAOS_SORCERER = 0x0A
    BEE: 0x0B
    CHAOS_BRINGER = 0x0D
    DARK_BELRA = 0x0E
    DE_ROL_LE = 0x0F
    DE_ROL_LE_SHELL = 0x10
    DE_ROL_LE_MINE = 0x11
    DRAGON = 0x12
    SINOW_GOLD = 0x13
    RAG_RAPPY = 0x18
    AL_RAPPY = 0x19
    NANO_DRAGON = 0x1A
    DUBCHIC = 0x1B
    GILLCHIC = 0x1C
    GARANZ = 0x1D
    DARK_GUNNER = 0x1E
    BULCLAW = 0x1F
    CLAW = 0x20
    VOL_OPT_1 = 0x21
    VOL_OPT_1_PILLAR = 0x22
    VOL_OPT_1_MONITOR = 0x23
    VOL_OPT_1_SPIRE = 0x24
    VOL_OPT_2 = 0x25
    VOL_OPT_2_PRISON = 0x26
    POUILLY_SLIME = 0x34
    POFUILLY_SLIME = 0x30
    PAN_ARMS = 0x31
    HIDOOM = 0x32
    MIGIUM = 0x33
    DARVANT = 0x35
    DARVANT_ULTIMATE = 0x39
    DARK_FALZ_1 = 0x36
    DARK_FALZ_2 = 0x37
    DARK_FALZ_3 = 0x38
    HILDEBEAR = 0x49
    HILDEBLUE = 0x4A
    BOOMA = 0x4B
    GOBOOMA = 0x4C
    GIGOBOOMA = 0x4D
    GRASS_ASSASSIN = 0x4E
    EVIL_SHARK = 0x4F
    PAL_SHARK = 0x50
    GUIL_SHARK = 0x51
    DELSABER = 0x52
    DIMENIAN = 0x53
    LA_DIMENIAN = 0x54
    SO_DIMENIAN = 0x55

class EnemyResistEp1:
    MOTHMANT = 0x00
    MONEST = 0x01
    SAVAGE_WOLF = 0x02
    BARBAROUS_WOLF = 0x03
    POISON_LILY = 0x04
    NAR_LILY = 0x05
    SINOW_BEAT = 0x06
    CANADINE = 0x07
    CANADINE_GROUP = 0x08
    CANANE = 0x09
    CHAOS_SORCERER = 0x0A
    BEE = 0x0B
    CHAOS_BRINGER = 0x0D
    DARK_BELRA = 0x0E
    DE_ROL_LE = 0x0F
    DE_ROL_LE_SHELL = 0x10
    DE_ROL_LE_MINE = 0x11
    DRAGON = 0x12
    SINOW_GOLD = 0x13
    RAG_RAPPY = 0x18
    AL_RAPPY = 0x19
    NANO_DRAGON = 0x1A
    DUBCHIC = 0x1B
    GILLCHIC = 0x1C
    GARANZ = 0x1D
    DARK_GUNNER = 0x1E
    BULCLAW = 0x1F
    CLAW = 0x20
    VOL_OPT_1 = 0x21
    VOL_OPT_1_PILLAR = 0x22
    VOL_OPT_1_MONITOR = 0x23
    VOL_OPT_1_SPIRE = 0x24
    VOL_OPT_2 = 0x25
    VOL_OPT_2_PRISON = 0x26
    POUILLY_SLIME = 0x34
    POFUILLY_SLIME = 0x30
    PAN_ARMS = 0x31
    HIDOOM = 0x32
    MIGIUM = 0x33
    DARVANT = 0x35
    DARVANT_ULTIMATE = 0x39
    DARK_FALZ_1 = 0x36
    DARK_FALZ_2 = 0x37
    DARK_FALZ_3 = 0x38
    HILDEBEAR = 0x49-1
    HILDEBLUE = 0x4A-1
    BOOMA = 0x4B-1
    GOBOOMA = 0x4C-1
    GIGOBOOMA = 0x4D-1
    GRASS_ASSASSIN = 0x4E-1
    EVIL_SHARK = 0x4F-1
    PAL_SHARK = 0x50-1
    GUIL_SHARK = 0x51-1
    DELSABER = 0x52-1
    DIMENIAN = 0x53-1
    LA_DIMENIAN = 0x54-1
    SO_DIMENIAN = 0x55-1

class EnemyStatEp2:
    MOTHMANT = 0x00
    MONEST = 0x01
    SAVAGE_WOLF = 0x02
    BARBAROUS_WOLF = 0x03
    POISON_LILY = 0x04
    NAR_LILY = 0x05
    SINOW_BERILL = 0x06
    GEE = 0x07
    CHAOS_SORCERER = 0x0A
    BEE = 0x0B
    DELBITER = 0x0D
    DARK_BELRA = 0x0E
    BARBA_RAY = 0x0F
    PIG_RAY = 0x10
    UL_RAY = 0x11
    GOL_DRAGON = 0x12
    SINOW_SPIGELL = 0x13
    RAG_RAPPY = 0x18
    LOVE_RAPPY = 0x19  # LOVE_RAPPY, SAINT_RAPPY, EGG_RAPPY, HALLO_RAPPY all return 0x19
    # SAINT_RAPPY = 0x19
    # EGG_RAPPY = 0x19
    # HALLO_RAPPY = 0x19
    GI_GUE = 0x1A
    DUBCHIC = 0x1B
    GILLCHIC = 0x1C
    GARANZ = 0x1D
    GAL_GRYPHON = 0x1E
    EPSILON = 0x23
    EPSIGUARD = 0x24
    DEL_LILY = 0x25
    ILL_GILL = 0x26
    OLGA_FLOW_1 = 0x2B
    OLGA_FLOW_2 = 0x2C
    GAEL = 0x2D
    GIEL = 0x2E
    DELDEPTH = 0x30
    PAN_ARMS = 0x31
    HIDOOM = 0x32
    MIGIUM = 0x33
    MERICAROL = 0x3A
    UL_GIBBON = 0x3B
    ZOL_GIBBON = 0x3C
    GIBBLES = 0x3D
    MORFOS = 0x40
    RECOBOX = 0x41
    RECON = 0x42
    SINOW_ZOA = 0x43
    SINOW_ZELE = 0x44
    MERIKLE = 0x45
    MERICUS = 0x46
    HILDEBEAR = 0x49
    HILDEBLUE = 0x4A
    MERILLIA = 0x4B
    MERILTAS = 0x4C
    GRASS_ASSASSIN = 0x4E
    DOLMOLM = 0x4F
    DOLMDARL = 0x50
    DELSABER = 0x52
    DIMENIAN = 0x53
    LA_DIMENIAN = 0x54
    SO_DIMENIAN = 0x55


class EnemyResistEp2:
    MOTHMANT = 0x00
    MONEST = 0x01
    SAVAGE_WOLF = 0x02
    BARBAROUS_WOLF = 0x03
    POISON_LILY = 0x04
    NAR_LILY = 0x05
    SINOW_BERILL = 0x06
    GEE = 0x07
    CHAOS_SORCERER = 0x0A
    BEE = 0x0B
    DELBITER = 0x0D
    DARK_BELRA = 0x0E
    BARBA_RAY = 0x0F
    PIG_RAY = 0x10
    UL_RAY = 0x11
    GOL_DRAGON = 0x12
    SINOW_SPIGELL = 0x13
    RAG_RAPPY = 0x18
    LOVE_RAPPY = 0x19  # LOVE_RAPPY, SAINT_RAPPY, EGG_RAPPY, HALLO_RAPPY all return 0x19
    # SAINT_RAPPY = 0x19
    # EGG_RAPPY = 0x19
    # HALLO_RAPPY = 0x19
    GI_GUE = 0x1A
    DUBCHIC = 0x1B
    GILLCHIC = 0x1C
    GARANZ = 0x1D
    GAL_GRYPHON = 0x1E
    EPSILON = 0x23
    EPSIGUARD = 0x24
    DEL_LILY = 0x25
    ILL_GILL = 0x26
    OLGA_FLOW_1 = 0x2B
    OLGA_FLOW_2 = 0x2C
    GAEL = 0x2D
    GIEL = 0x2E
    DELDEPTH = 0x30
    PAN_ARMS = 0x31
    HIDOOM = 0x32
    MIGIUM = 0x33
    MERICAROL = 0x3A
    UL_GIBBON = 0x3B
    ZOL_GIBBON = 0x3C
    GIBBLES = 0x3D
    MORFOS = 0x40
    RECOBOX = 0x41
    RECON = 0x42
    SINOW_ZOA = 0x43
    SINOW_ZELE = 0x44
    MERIKLE = 0x45
    MERICUS = 0x46
    HILDEBEAR = 0x49-1
    HILDEBLUE = 0x4A-1
    MERILLIA = 0x4B-1
    MERILTAS = 0x4C-1
    GRASS_ASSASSIN = 0x4E-1
    DOLMOLM = 0x4F-1
    DOLMDARL = 0x50-1
    DELSABER = 0x51
    DIMENIAN = 0x52
    LA_DIMENIAN = 0x53
    SO_DIMENIAN = 0x54


class EnemyTypeEp4:
    BOOTA = 0x00
    ZE_BOOTA = 0x01
    BA_BOOTA = 0x03
    SAND_RAPPY = 0x05
    DEL_RAPPY = 0x06
    ZU = 0x07
    PAZUZU = 0x08
    ASTARK = 0x09
    SATELLITE_LIZARD = 0x0D
    YOWIE = 0x0E
    DORPHON = 0x0F
    DORPHON_ECLAIR = 0x10
    GORAN = 0x11
    PYRO_GORAN = 0x12
    GORAN_DETONATOR = 0x13
    SAND_RAPPY_ALT = 0x17
    DEL_RAPPY_ALT = 0x18
    MERISSA_A = 0x19
    MERISSA_AA = 0x1A
    ZU_ALT = 0x1B
    PAZUZU_ALT = 0x1C
    SATELLITE_LIZARD_ALT = 0x1D
    YOWIE_ALT = 0x1E
    GIRTABLULU = 0x1F
    SAINT_MILLION_1 = 0x20
    SPINNER_SAINT_1 = 0x21
    SAINT_MILLION_2 = 0x22  # SAINT_MILLION, SHAMBERTIN, KONDRIEU all return 0x22
    SPINNER_SAINT_2 = 0x23

    SHAMBERTIN_1 = 0x24
    SPINNER_SHAMBERTIN_1 = 0x25
    SHAMBERTIN_2 = 0x26
    SPINNER_SHAMBERTIN_2 = 0x27
    KONDRIEU_1 = 0x28
    SPINNER_KONDRIEU_1 = 0x29
    KONDRIEU_2 = 0x2A
    SPINNER_KONDRIEU_2 = 0x2B


# Create a reverse mapping from number to enum

ep1_stat_num_to_str = {value: key for key, value in EnemyStatEp1.__dict__.items() if not key.startswith('__')}
ep1_stat_str_to_num = {key: value for key, value in EnemyStatEp1.__dict__.items() if not key.startswith('__')}

ep1_resist_num_to_str = {value: key for key, value in EnemyResistEp1.__dict__.items() if not key.startswith('__')}
ep1_resist_str_to_num = {key: value for key, value in EnemyResistEp1.__dict__.items() if not key.startswith('__')}


ep2_stat_num_to_str = {value: key for key, value in EnemyStatEp2.__dict__.items() if not key.startswith('__')}
ep2_stat_str_to_num = {key: value for key, value in EnemyStatEp2.__dict__.items() if not key.startswith('__')}


ep2_resist_num_to_str = {value: key for key, value in EnemyResistEp2.__dict__.items() if not key.startswith('__')}
ep2_resist_str_to_num = {key: value for key, value in EnemyResistEp2.__dict__.items() if not key.startswith('__')}


ep4_stat_num_to_str = {value: key for key, value in EnemyTypeEp4.__dict__.items() if not key.startswith('__')}
ep4_stat_str_to_num = {key: value for key, value in EnemyTypeEp4.__dict__.items() if not key.startswith('__')}

ep4_resist_num_to_str = ep4_stat_num_to_str
ep4_resist_str_to_num = ep4_stat_str_to_num

char_stats_format = '<HHHHHHH'  # 7 fields of 'H' (2 bytes each)
player_stats_format = char_stats_format + 'HffIII'
movement_format_str = '<ffffffIIIIII'
attack_format_str = '<hhhHfffHHHHIIIII'
resist_format_str = '<hHHHHHIIIIi'

files = {'Online':{}, 'Offline':{}}


def load_files():
    print("Attempting to read battleparam files in same directory")
    files['Online'][1] = load_file('BattleParamEntry_on.dat', 1)
    files['Online'][2] =load_file('BattleParamEntry_lab_on.dat', 2)
    files['Online'][4] =load_file('BattleParamEntry_ep4_on.dat', 4)
    files['Offline'][1] =load_file('BattleParamEntry.dat', 1)
    files['Offline'][2] =load_file('BattleParamEntry_lab.dat', 2)
    files['Offline'][4] =load_file('BattleParamEntry_ep4.dat', 4)

def load_file(file_path:str, episode:int):
    if os.path.isfile(file_path):
        try:
            # with open(file_path, 'rb') as f:
            #     file = bytearray(f.read())
            #     return file
            return Table(file_path=file_path,episode=episode)
        except:
            print(f"Error reading file")

    else:
        print(f"Unable to locate file. Please check file path argument.")
    return None



class Table:

    episode = 0
    data = []
    stat_num_to_str_map = []
    stat_str_to_num_map = []
    resist_num_to_str_map = []
    resist_str_to_num_map = []

    def __init__(self,file_path, episode):
        self.episode = episode
        if episode == 1:
            self.stat_num_to_str_map = ep1_stat_num_to_str
            self.resist_num_to_str_map = ep1_resist_num_to_str
            self.stat_str_to_num_map = ep1_stat_str_to_num
            self.resist_str_to_num_map = ep1_resist_str_to_num

        elif episode == 2:
            self.stat_num_to_str_map = ep2_stat_num_to_str
            self.resist_num_to_str_map = ep2_resist_num_to_str
            self.stat_str_to_num_map = ep2_stat_str_to_num
            self.resist_str_to_num_map = ep2_resist_str_to_num
        elif episode == 4:
            self.stat_num_to_str_map = ep4_stat_num_to_str
            self.resist_num_to_str_map = ep4_resist_num_to_str
            self.stat_str_to_num_map = ep4_stat_str_to_num
            self.resist_str_to_num_map = ep4_resist_str_to_num
        else:
            raise KeyError("Invalid Episode Number")

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'rb') as f:
                    self.data = bytearray(f.read())

            except:
                print(f"Error reading file")
        else:
            raise OSError("File not found. Please check file path.")

    def write(self, new_file_name, overwrite=False):
        if ~overwrite:
            if os.path.isfile(new_file_name):
                raise OSError("Output filename already exists. Either change new_file_name or set overwrite=True")

        with open(new_file_name, "wb") as binary_file:
            # Write bytes to file
            binary_file.write(self.data)
        print('File has been written!')

    def get_keys(self):

        print("Stat map keys:")
        print(self.get_stat_keys())
        print('-----')
        print("Resist map keys:")
        print(self.get_resist_keys())

    def get_stat_keys(self):

        return self.stat_str_to_num_map.keys()

    def get_resist_keys(self):
        return self.resist_str_to_num_map.keys()



    def get_address_resist(self,enemy, difficulty):

        if enemy in self.resist_str_to_num_map.keys():
            enemy_position = self.resist_str_to_num_map[enemy]
        else:
            raise KeyError("Check enemy spelling. List of keys in get_keys(episode num).")


        table_length = 0x60
        resist_size = struct.calcsize(resist_format_str)

        pointer = 0x7E00 + difficulty * (table_length * resist_size) + enemy_position * resist_size
        print(
            f'{enemy} resist at difficulty {difficulty} is at {hex(pointer)} ({pointer}) to {hex(pointer + resist_size)} ({pointer + resist_size})')
        pointer += 2
        value = struct.unpack('<H', self.data[pointer:pointer + 2])[0]
        print(f'EFR le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer += 2
        value = struct.unpack('<H', self.data[pointer:pointer + 2])[0]
        print(f'EIC le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer += 2
        value = struct.unpack('<H', self.data[pointer:pointer + 2])[0]
        print(f'ETH le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer += 2
        value = struct.unpack('<H', self.data[pointer:pointer + 2])[0]
        print(f'ELT le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer += 2
        value = struct.unpack('<H', self.data[pointer:pointer + 2])[0]
        print(f'EDK le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')


    def get_address_stats(self, enemy,difficulty):


        if enemy in self.stat_str_to_num_map.keys():
            enemy_position = self.stat_str_to_num_map[enemy]
        else:
            raise KeyError("Check enemy spelling. List of keys in get_keys(episode num).")

        # stats
        table_length = 0x60
        stat_size = struct.calcsize(player_stats_format)

        pointer = 0x0 + difficulty * (table_length * stat_size) + enemy_position * stat_size

        print(f'{enemy} stats at difficulty {difficulty} is at {hex(pointer)} ({pointer}) to {hex(pointer+stat_size)} ({pointer+stat_size})')
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'ATP le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer+=2
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'MST le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer+=2
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'EVP le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer+=2
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'HP le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer+=2
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'DFP le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer+=2
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'ATA le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer+=2
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'LCK le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')
        pointer+=2
        value = struct.unpack('<H', self.data[pointer:pointer+2])[0]
        print(f'ESP le_uint16 is set to {value} starting at at {hex(pointer)} ({pointer})')

    def set_stat_property(self, value, stat, enemy, difficulty):

        if enemy in self.stat_str_to_num_map.keys():
            enemy_position = self.stat_str_to_num_map[enemy]
        else:
            raise KeyError("Check enemy spelling. List of keys in get_keys(episode num).")

        # stats
        table_length = 0x60
        stat_size = struct.calcsize(player_stats_format)

        pointer = 0x0 + difficulty * (table_length * stat_size) + enemy_position * stat_size
        output_string = '<'
        stat = stat.lower()
        if stat == 'atp':
            pointer += 0
            output_string = output_string + "H"
        elif stat == 'mst':
            pointer += 2
            output_string = output_string + "H"
        elif stat == 'evp':
            pointer += 4
            output_string = output_string + "H"
        elif stat == 'hp':
            pointer += 6
            output_string = output_string + "H"
        elif stat == 'dfp':
            pointer += 8
            output_string = output_string + "H"
        elif stat == 'ata':
            pointer += 10
            output_string = output_string + "H"
        elif stat == 'lck':
            pointer += 12
            output_string = output_string + "H"
        elif stat == 'esp':
            pointer += 14
            output_string = output_string + "H"
        else:
            raise KeyError("please use lower case attribute name")

        width = struct.calcsize(output_string)
        print(f'Pointer is at {hex(pointer)} ({pointer})')
        old_value = struct.unpack(output_string, self.data[pointer:pointer + width])[0]
        print(f"Previous value was {old_value} ({bytes(self.data[pointer:pointer + width])})")
        new_value = struct.pack(output_string, value)
        self.data[pointer:pointer + width] = new_value
        print(f"Value is now {value} ({new_value}) at {hex(pointer)}")

    def set_resist_property(self, value, stat, enemy, difficulty):

        if enemy in self.resist_str_to_num_map.keys():
            enemy_position = self.resist_str_to_num_map[enemy]
        else:
            raise KeyError("Check enemy spelling. List of keys in get_keys(episode num).")

        # stats
        table_length = 0x60
        resist_size = struct.calcsize(resist_format_str)
        output_string = '<'
        pointer = 0x7E00 + difficulty * (table_length * resist_size) + enemy_position * resist_size

        stat = stat.lower()
        if stat == 'evp_bonus':
            pointer += 0
            output_string = output_string + "h"

        elif stat == 'efr':
            pointer += 2
            output_string = output_string + "H"
        elif stat == 'eic':
            pointer += 4
            output_string = output_string + "H"
        elif stat == 'eth':
            pointer += 6
            output_string = output_string + "H"
        elif stat == 'elt':
            pointer += 8
            output_string = output_string + "H"
        elif stat == 'edk':
            pointer += 10
            output_string = output_string + "H"

        else:
            raise KeyError("please use lower case attribute name")
        print(f'Pointer is at {hex(pointer)} ({pointer})')
        width = struct.calcsize(output_string)
        old_value = struct.unpack(output_string, self.data[pointer:pointer + width])[0]
        print(f"Previous value was {old_value} ({bytes(self.data[pointer:pointer + width])})")
        new_value = struct.pack(output_string, value)
        self.data[pointer:pointer + width] = new_value
        print(f"Value is now {value} ({new_value}) at {hex(pointer)}")

    def get_stat_table(self,difficulty:int,verbose:bool=False):
        table_length = 0x60
        stat_size = struct.calcsize(player_stats_format)
        pointer = 0x0 + difficulty * (table_length * stat_size)

        stat_table = pd.DataFrame(columns=['HP', 'XP', 'ATP', 'DFP', 'MST', 'ATA', 'EVP', 'LCK', 'ESP'])
        i = 0x0

        # while pointer < 0x3600:
        for i in range(table_length):
            subset = self.data[pointer:pointer + stat_size]
            if i in self.stat_num_to_str_map.keys():
                if verbose: print(self.stat_num_to_str_map[i], i)
                new_name = ' '.join([i.capitalize() for i in self.stat_num_to_str_map[i].split('_')])
                atp, mst, evp, hp, dfp, ata, lck, esp, unk_2, unk_3, _, exp, _ = struct.unpack(player_stats_format,
                                                                                               subset)
                #             print(unk_1,unk_2,unk_3)
                stat_table.loc[new_name] = hp, exp, atp, dfp, mst, ata, evp, lck, esp
            if verbose:
                print(struct.unpack(player_stats_format, subset))
            pointer += stat_size
            i += 1
        return stat_table

    def get_stat_table_raw(self,difficulty:int):
        table_length = 0x60
        stat_size = struct.calcsize(player_stats_format)
        pointer = 0x0 + difficulty * (table_length * stat_size)

        stat_table = pd.DataFrame(columns=[i for i in range(13)])
        i = 0x0

        # while pointer < 0x3600:
        for i in range(table_length):
            subset = self.data[pointer:pointer + stat_size]
            # print(subset)
            stat_table.loc[i] = struct.unpack(player_stats_format,subset)

            pointer += stat_size
            i += 1
        return stat_table

    def get_resist_table(self,difficulty:int,verbose:bool=False):
        table_length = 0x60

        resist_table = pd.DataFrame(columns=['EFR', 'EIC', 'ETH', 'ELT', 'EDK', ])

        resist_size = struct.calcsize(resist_format_str)
        pointer = 0x7E00 + difficulty * (table_length * resist_size)
        i = 0x0

        for i in range(table_length):
            subset = self.data[pointer:pointer + resist_size]
            if i in self.resist_num_to_str_map.keys():
                if verbose: print(self.resist_num_to_str_map[i], i)
                new_name = ' '.join([i.capitalize() for i in self.resist_num_to_str_map[i].split('_')])
                _, efr, eic, eth, elt, edk, _, _, _, _, _ = struct.unpack(resist_format_str, subset)
                resist_table.loc[new_name] = efr, eic, eth, elt, edk
            if verbose:
                print(struct.unpack(resist_format_str, subset))
            pointer += resist_size
            i += 1
        return resist_table

    def get_resist_table_raw(self,difficulty:int):
        table_length = 0x60

        resist_table = pd.DataFrame(columns=[i for i in range(11)])

        resist_size = struct.calcsize(resist_format_str)
        pointer = 0x7E00 + difficulty * (table_length * resist_size)
        i = 0x0

        for i in range(table_length):
            subset = self.data[pointer:pointer + resist_size]
            # print(subset)
            resist_table.loc[i] = struct.unpack(resist_format_str, subset)

            pointer += resist_size
            i += 1
        return resist_table

    def get_attack_table_raw(self,difficulty:int):
        table_length = 0x60

        attack_table = pd.DataFrame(columns=[i for i in range(16)])

        attack_size = struct.calcsize(attack_format_str)
        pointer = 0x3600 + difficulty * (table_length * attack_size)
        i = 0x0

        for i in range(table_length):
            subset = self.data[pointer:pointer + attack_size]
            # print(subset)
            attack_table.loc[i] = struct.unpack(attack_format_str, subset)

            pointer += attack_size
            i += 1
        return attack_table

    def get_movement_table_raw(self,difficulty:int):
        table_length = 0x60

        movement_table = pd.DataFrame(columns=[i for i in range(12)])

        movement_size = struct.calcsize(movement_format_str)
        pointer = 0xAE00 + difficulty * (table_length * movement_size)
        i = 0x0

        for i in range(table_length):
            subset = self.data[pointer:pointer + movement_size]
            # print(subset)
            movement_table.loc[i] = struct.unpack(movement_format_str, subset)

            pointer += movement_size
            i += 1
        return movement_table

    def get_merged_table(self, difficulty:int,verbose:bool=False):

        stat_table = self.get_stat_table(difficulty=difficulty, verbose=verbose)
        resist_table = self.get_resist_table(difficulty=difficulty, verbose=verbose)

        merged_table = pd.merge(stat_table, resist_table, left_index=True, right_index=True)
        merged_table.index.rename('Enemy', inplace=True)

        return merged_table

    def set_with_data_type(self,value, data_type, location ,little_endian=True, verbose=True):
        pointer = location
        format_string = ''
        if little_endian:
            format_string = format_string + '<'
        else:
            format_string = format_string + '>'
        if data_type == 'float':
            format_string = format_string + 'f'
        elif data_type == 'double':
            format_string = format_string + 'd'
        elif data_type == 'int32':
            format_string = format_string + 'i'
        elif data_type == 'uint32':
            format_string = format_string +'I'
        elif data_type == 'int16':
            format_string = format_string + 'h'
        elif data_type == 'uint16':
            format_string = format_string + 'H'
        else:
            raise Exception('Error with data_type parameter')


        width = struct.calcsize(format_string)
        new_value = struct.pack(format_string, value)
        if verbose:
            print(f'Settings bytes in region from {hex(location)} to {hex(location+width-1)}')
            print(f'Was {self.data[pointer:pointer+width]}')
        self.data[pointer:pointer + width] = new_value
        if verbose:
            print(f"Now {self.data[pointer:pointer+width]}")

    def set_with_bytes(self, value : bytes, location, verbose=True):
        pointer = location
        width = len(value)
        if verbose:
            print(f'Settings bytes in region from {hex(location)} to {hex(location+width-1)}')
            print(f'Was {self.data[pointer:pointer+width]}')
        self.data[pointer:pointer + width] = value
        if verbose:
            print(f"Now {self.data[pointer:pointer+width]}")

    def get_bytes(self,start,end):
        return self.data[start:end+1]

    def search_bytes(self, sequence):
        results = []
        data_copy = self.data.copy()
        while True:
            # print('doing loop')
            test_index = data_copy.find(sequence)
            if test_index >= 0:

                # print(test_index)
                if results:
                    # print(results)
                    results.append(test_index+results[-1]+1)
                else:
                    results.append(test_index)
                if test_index+2 < len(self.data):
                    data_copy = data_copy[test_index+1:]
                else:
                    return [hex(i) for i in results]
            else:
                return [hex(i) for i in results]

    def __repr__(self):
        return f'Episode {self.episode} table object'