import socket
import struct
import zlib

PACKET_HEADER = "<ccLB"
mock_address = "snek.earth"
mock_address_ip = '172.19.134.2'
mock_port = 30604

# See http://www.cs.helsinki.fi/u/aitakang/dom3_serverformat_notes for
# descriptions for most of the protocol

# Python 2 doesn't support enums with the standard libraries, so...
era = {0: "None", 1: "EA", 2: "MA", 3: "LA"}

status = {
    0: "Empty",
    1: "Human",
    2: "AI",
    3: "Independent",
    253: "Closed",
    254: "Defeated this turn",
    255: "Defeated",
}


def query(address=mock_address, port=mock_port):
    sck = socket.socket()
    sck.settimeout(5.0)
    sck.connect((address, port))
    # Little endian, 'fH', 32 bit message length, message body (char)
    # f H 1 3
    sck.send(struct.pack(PACKET_HEADER, b'f', b'H', 1, 3))
    result = sck.recv(512)
    if result is not None:
        if len(result) < 50:
            print("error, received packet is not long enough")
            return None

        header = struct.unpack(PACKET_HEADER, result[0:7])
        compressed = header[1] == "J"
        packetlength = header[2]
        packettype = header[3]

        data = None

        if compressed:
            data = zlib.decompress(result[10:])
        else:
            data = result[10:]

        game_name_len = len(data) - 26 - 750
        game_name_buffer = (0, game_name_len)
        print('yes cats')


query()
