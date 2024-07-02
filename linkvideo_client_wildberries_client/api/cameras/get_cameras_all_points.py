from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_error import AuthError
from ...models.internal_server_error import InternalServerError
from ...models.not_found_error import NotFoundError
from ...models.permission_error import PermissionError_
from ...models.request_error import RequestError
from ...models.wb_cameras_points import WBCamerasPoints
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/wb/cameras/points",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WBCamerasPoints.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RequestError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = AuthError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = PermissionError_.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFoundError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]:
    """Получение всех камер на ПВЗ Wildberries

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]:
    """Получение всех камер на ПВЗ Wildberries

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]:
    """Получение всех камер на ПВЗ Wildberries

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]]:
    """Получение всех камер на ПВЗ Wildberries

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthError, InternalServerError, NotFoundError, PermissionError_, RequestError, WBCamerasPoints]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
