from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WBCameraPoint")


@_attrs_define
class WBCameraPoint:
    """
    Attributes:
        uuid (Union[Unset, str]): Идентификатор камеры Example: 1234.
        point_id (Union[Unset, str]): Идентификатор ПВЗ Example: 12345.
        stream_url (Union[Unset, str]): Ссылка на поток HLS (с сигнатурой) Example:
            https://example.video/example/camera_1234/playlist_dvr_range-1700.m3u8.
    """

    uuid: Union[Unset, str] = UNSET
    point_id: Union[Unset, str] = UNSET
    stream_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid

        point_id = self.point_id

        stream_url = self.stream_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["UUID"] = uuid
        if point_id is not UNSET:
            field_dict["point_id"] = point_id
        if stream_url is not UNSET:
            field_dict["stream_url"] = stream_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("UUID", UNSET)

        point_id = d.pop("point_id", UNSET)

        stream_url = d.pop("stream_url", UNSET)

        wb_camera_point = cls(
            uuid=uuid,
            point_id=point_id,
            stream_url=stream_url,
        )

        wb_camera_point.additional_properties = d
        return wb_camera_point

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
