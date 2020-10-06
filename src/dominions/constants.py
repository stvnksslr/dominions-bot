# snek.earth constants
SNEK_BASE_URL = "https://snek.earth/api/games/"


# Packet Constants for scraping the game server itself
PACKET_HEADER = "<ccLB"
PACKET_BYTES_PER_NATION = 3
PACKET_NUM_NATIONS = 250
PACKET_GENERAL_INFO = "<BBBBBB{0}sBBBBBBLB{1}BLLB"  # to use format later
PACKET_NATION_INFO_START = 15
