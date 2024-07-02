from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionError_")


@_attrs_define
class PermissionError_:
    """
    Attributes:
        code (Union[Unset, int]): Внутренний код ошибки Example: 600.
        error (Union[Unset, str]): Человекопонятное описание ошибки Example: Недостаточно прав.
        block_interval (Union[Unset, int]): Интервал блокировки повторного запроса, секунды
    """

    code: Union[Unset, int] = UNSET
    error: Union[Unset, str] = UNSET
    block_interval: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        error = self.error

        block_interval = self.block_interval

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if error is not UNSET:
            field_dict["error"] = error
        if block_interval is not UNSET:
            field_dict["block_interval"] = block_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        error = d.pop("error", UNSET)

        block_interval = d.pop("block_interval", UNSET)

        permission_error = cls(
            code=code,
            error=error,
            block_interval=block_interval,
        )

        permission_error.additional_properties = d
        return permission_error

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
