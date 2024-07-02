import os

from icecream import ic

from linkvideo_client_wildberries_client import AuthenticatedClient
from linkvideo_client_wildberries_client.api.cameras import get_cameras_all_points
from linkvideo_client_wildberries_client.models import WBCamerasPoints


def test_basic_operations():
    token: str = os.getenv("LINKVIDEO_TOKEN")
    ic(token)
    client = AuthenticatedClient(base_url="https://api.b2o.goodline.info/ords/mobile/vc2", token=token)

    with client:
        points_and_cameras: WBCamerasPoints = get_cameras_all_points.sync(client=client)
        assert isinstance(points_and_cameras, WBCamerasPoints)
        ic(points_and_cameras)
