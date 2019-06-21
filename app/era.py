from dataclasses import dataclass
from enum import Enum


class Era(Enum):
    EA = 0
    MA = 1
    LA = 2


class Status(Enum):
    Empty = 0
    Human = 1
    AI = 2
    Independent = 2
    Closed = 253
    Defeated_this_turn = 254
    Defeated = 255


@dataclass
class Nation:
    id: int
    name: str
    era: Era


class Nations(Enum):
    Arcoscephale = Nation(id=5, name='Arcoscephale', era=Era.EA)
    Ermor = Nation(id=6, name='Ermor', era=Era.EA)
    ULM_EA = Nation(id=7, name='Ulm', era=Era.EA)
    Marverni = Nation(id=8, name='Marverni', era=Era.EA)
    Sauromatia = Nation(id=9, name='Sauromatia', era=Era.EA)
    TienChi = Nation(id=10, name="T'ien Ch'i", era=Era.EA)
    Machaka = Nation(id=11, name="Machaka", era=Era.EA)
    Mictlan = Nation(id=12, name="Mictlan", era=Era.EA)
    Abysia = Nation(id=13, name="Abysia", era=Era.EA)
    Caelum = Nation(id=14, name="Caelum", era=Era.EA)
    C_tis = Nation(id=15, name="C'tis", era=Era.EA)
    Pangaea = Nation(id=16, name="Pangaea", era=Era.EA)
    Agartha = Nation(id=17, name="Agartha", era=Era.EA)
    TirNanOG = Nation(id=18, name="Tir na n'Og", era=Era.EA)
    Fomoria = Nation(id=19, name="Fomoria", era=Era.EA)
    Vanheim = Nation(id=20, name="Vanheim", era=Era.EA)
    Helheim = Nation(id=21, name="Helheim", era=Era.EA)
    Niefelheim = Nation(id=22, name="Niefelheim", era=Era.EA)
    Rus = Nation(id=24, name="Rus", era=Era.EA)
    Kailasa = Nation(id=25, name="Kailasa", era=Era.EA)
    Lanka = Nation(id=26, name="Lanka", era=Era.EA)
    Yomi = Nation(id=27, name="Yomi", era=Era.EA)
    Hinnom = Nation(id=28, name="Hinnom", era=Era.EA)
    Ur = Nation(id=29, name="Ur", era=Era.EA)
    Berytos = Nation(id=30, name="Berytos", era=Era.EA)
    Xibalba = Nation(id=31, name="Xibalba", era=Era.EA)
    Mekone = Nation(id=32, name="Mekone", era=Era.EA)
    Atlantis = Nation(id=36, name="Atlantis", era=Era.EA)
    R_lyeh = Nation(id=37, name="R'lyeh", era=Era.EA)
    Pelagia = Nation(id=38, name="Pelagia", era=Era.EA)
    Oceania = Nation(id=39, name="Oceania", era=Era.EA)
    Therodos = Nation(id=40, name="Therodos", era=Era.EA)
    Arcoscephale_MA = Nation(id=43, name="Therodos", era=Era.MA)
    Ermor_MA = Nation(id=44, name="Ermor", era=Era.MA)
    Sceleria = Nation(id=45, name="Sceleria", era=Era.MA)
    Pythium = Nation(id=46, name="Pythium", era=Era.MA)
    Man = Nation(id=47, name="Man", era=Era.MA)
    Eriu = Nation(id=48, name="Eriu", era=Era.MA)
    Ulm_MA = Nation(id=49, name="Ulm", era=Era.MA)
    Marignon = Nation(id=50, name="Marignon", era=Era.MA)
    Mictlan_MA = Nation(id=51, name="Mictlan", era=Era.MA)
    TienChi_MA = Nation(id=52, name="T'ien Ch'i", era=Era.MA)
    Machaka_MA = Nation(id=53, name="Machaka", era=Era.MA)
    Agartha_MA = Nation(id=54, name="Agartha", era=Era.MA)
    Abysia_MA = Nation(id=55, name="Abysia", era=Era.MA)
    Caelum_MA = Nation(id=56, name="Caelum", era=Era.MA)
    C_tis_MA = Nation(id=57, name="C'tis", era=Era.MA)
    Pangaea_MA = Nation(id=58, name="Pangaea", era=Era.MA)
    Asphodel = Nation(id=59, name="Asphodel", era=Era.MA)
    Vanheim_MA = Nation(id=60, name="Vanheim", era=Era.MA)
    Jotunheim = Nation(id=61, name="Jotunheim", era=Era.MA)
    Vanarus = Nation(id=62, name="Vanarus", era=Era.MA)
    Bandar_Log = Nation(id=63, name="Bandar Log", era=Era.MA)
    Shinuyama = Nation(id=64, name="Shinuyama", era=Era.MA)
    Ashdod = Nation(id=65, name="Ashdod", era=Era.MA)
    Uruk = Nation(id=66, name="Uruk", era=Era.MA)
    Nazca = Nation(id=67, name="Nazca", era=Era.MA)
    Xibalba_MA = Nation(id=68, name="Xibalba", era=Era.MA)
    Phlegra = Nation(id=69, name="Phlegra", era=Era.MA)
    Phaeacia = Nation(id=70, name="Phaeacia", era=Era.MA)
    Atlantis_MA = Nation(id=73, name="Atlantis", era=Era.MA)
    R_lyeh_MA = Nation(id=74, name="R'lyeh", era=Era.MA)
    Pelagia_MA = Nation(id=75, name="Pelagia", era=Era.MA)
    Oceania_MA = Nation(id=76, name="Oceania", era=Era.MA)
    Ys = Nation(id=77, name="Ys", era=Era.MA)
    Arcoscephale_LA = Nation(id=80, name="Arcoscephale", era=Era.LA)
    Pythium_LA = Nation(id=81, name="Pythium", era=Era.LA)
    Lemur = Nation(id=82, name="Lemur", era=Era.LA)
    Man_LA = Nation(id=83, name="Man", era=Era.LA)
    Ulm_LA = Nation(id=84, name="Ulm", era=Era.LA)
    Marignon_LA = Nation(id=85, name="Marignon", era=Era.LA)
    Mictlan_LA = Nation(id=86, name="Mictlan", era=Era.LA)
    TienChi_LA = Nation(id=87, name="T'ien Ch'i", era=Era.LA)
    Jomon = Nation(id=89, name="Jomon", era=Era.LA)
    Agartha_LA = Nation(id=90, name="Agartha", era=Era.LA)
    Abysia_LA = Nation(id=91, name="Abysia", era=Era.LA)
    Caelum_LA = Nation(id=92, name="Caelum", era=Era.LA)
    C_tis_LA = Nation(id=93, name="C'tis", era=Era.LA)
    Pangaea_LA = Nation(id=94, name="Pangaea", era=Era.LA)
    Midgard = Nation(id=95, name="Midgard", era=Era.LA)
    Utgard = Nation(id=96, name="Utgard", era=Era.LA)
    Bogarus = Nation(id=97, name="Bogarus", era=Era.LA)
    Patala = Nation(id=98, name="Patala", era=Era.LA)
    Gath = Nation(id=99, name="Gath", era=Era.LA)
    Ragha = Nation(id=100, name="Ragha", era=Era.LA)
    Xibalba_LA = Nation(id=101, name="Xibalba", era=Era.LA)
    Phlegra_LA = Nation(id=102, name="Phlegra", era=Era.LA)
    Atlantis_LA = Nation(id=106, name="Atlantis", era=Era.LA)
    R_lyeh_LA = Nation(id=107, name="R'lyeh", era=Era.LA)
    Erytheia = Nation(id=108, name="Erytheia", era=Era.LA)
