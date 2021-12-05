from struct import pack, unpack
from socket import socket
from zlib import decompress

from dominions.constants import (
    PACKET_HEADER,
    PACKET_GENERAL_INFO,
    PACKET_BYTES_PER_NATION,
    PACKET_NUM_NATIONS,
    GameStatus,
)


def query(address, port):
    sck = socket()
    sck.settimeout(5.0)
    sck.connect((address, port))

    # request info
    pack_game_request = pack(
        "<ccssssccccccc",
        b"f",
        b"H",
        b"\a",
        b"\x00",
        b"\x00",
        b"\x00",
        b"=",
        b"\x1e",
        b"\x02",
        b"\x11",
        b"E",
        b"\x05",
        b"\x00",
    )
    sck.send(pack_game_request)
    result = sck.recv(512)

    # close connection
    sck.send(pack(PACKET_HEADER, b"f", b"H", 1, 11))
    sck.close()

    header = unpack(PACKET_HEADER, result[0:7])
    compressed = header[1] == b"J"

    if compressed:
        data = decompress(result[10:])
    else:
        data = result[10:]

    game_name_length = (
        len(data)
        - len(PACKET_GENERAL_INFO.format("", ""))
        - PACKET_BYTES_PER_NATION * PACKET_NUM_NATIONS
        - 6
    )

    data_array = unpack(
        PACKET_GENERAL_INFO.format(
            game_name_length, PACKET_BYTES_PER_NATION * PACKET_NUM_NATIONS
        ),
        data,
    )
    hours_remaining = round(data_array[13] / (1000 * 60 * 60), 2)

    return GameStatus(
        name=data_array[6].decode().rstrip("\x00"),
        turn=data_array[-3],
        hours_remaining=hours_remaining,
    )
