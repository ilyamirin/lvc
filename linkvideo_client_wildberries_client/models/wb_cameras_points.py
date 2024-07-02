from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wb_camera_point import WBCameraPoint


T = TypeVar("T", bound="WBCamerasPoints")


@_attrs_define
class WBCamerasPoints:
    """
    Attributes:
        cameras (Union[Unset, List['WBCameraPoint']]):
    """

    cameras: Union[Unset, List["WBCameraPoint"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cameras: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cameras, Unset):
            cameras = []
            for cameras_item_data in self.cameras:
                cameras_item = cameras_item_data.to_dict()
                cameras.append(cameras_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cameras is not UNSET:
            field_dict["cameras"] = cameras

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wb_camera_point import WBCameraPoint

        d = src_dict.copy()
        cameras = []
        _cameras = d.pop("cameras", UNSET)
        for cameras_item_data in _cameras or []:
            cameras_item = WBCameraPoint.from_dict(cameras_item_data)

            cameras.append(cameras_item)

        wb_cameras_points = cls(
            cameras=cameras,
        )

        wb_cameras_points.additional_properties = d
        return wb_cameras_points

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
