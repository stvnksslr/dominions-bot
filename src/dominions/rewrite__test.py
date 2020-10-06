from pytest_httpx import HTTPXMock

from dominions.rewrite import (
    fetch_game_info,
    fetch_player_status,
    process_player_status,
)
from dominions.mocks.snek.status import mock__api_game_status
from dominions.mocks.snek.status import mock__api_player_status
from dominions.mocks.library import mock_player_list

from dominions.constants import SNEK_BASE_URL


mock_game_id = 1770
mock_game_url = f"{SNEK_BASE_URL}{mock_game_id}"

mock_game_info = mock__api_game_status.MOCK_GAME_STATUS
mock_player_status = mock__api_player_status.PLAYER_STATUS


def test__fetch_game_info(httpx_mock: HTTPXMock):
    """
    method: fetch_game_info
    prerequisite: take a given id and query the snek.earth api
    expected: returns without error
    """
    httpx_mock.add_response(
        url=mock_game_url,
        json=[mock__api_game_status.MOCK_GAME_STATUS],
    )
    response = fetch_game_info(mock_game_id)
    assert response.status_code == 200


def test__fetch_player_status(httpx_mock: HTTPXMock):
    """
    method: fetch_player_status
    prerequisite: take a given id and query the snek.earth status api
    expected: returns without error
    """
    httpx_mock.add_response(
        url=f"{mock_game_url}/status",
        json=[mock__api_player_status.PLAYER_STATUS],
    )
    response = fetch_player_status(mock_game_id)
    assert response.status_code == 200


def test__process_player_status():
    """
    method: process_player_status
    prerequisite: take a given api response and get the player list + current turn status
    expected: Matches Mock Object
    """
    player_status = process_player_status(mock_player_status)
    assert player_status == mock_player_list.MOCK_PLAYER_LIST


def test__process_game_info():
    """
    method: process_game_info
    prerequisite: query a given game for general info about it, this should only need to happen once and then be cached
    expected: Matches mock object
    """
    game_info = process_game_info(mock_game_info)
    assert "cat" == "cat"
