from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
EN: Lang
RU: Lang

class DocObj(_message.Message):
    __slots__ = ["_class", "article_id", "date", "entities", "keywords", "lang", "locations", "semantic_vector", "text", "themes", "title"]
    class Class(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Entity(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Keyword(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Location(_message.Message):
        __slots__ = ["lat", "lon"]
        LAT_FIELD_NUMBER: _ClassVar[int]
        LON_FIELD_NUMBER: _ClassVar[int]
        lat: float
        lon: float
        def __init__(self, lat: _Optional[float] = ..., lon: _Optional[float] = ...) -> None: ...
    class Theme(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Vector(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...
    ARTICLE_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_VECTOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    _CLASS_FIELD_NUMBER: _ClassVar[int]
    _class: _containers.RepeatedCompositeFieldContainer[DocObj.Class]
    article_id: int
    date: str
    entities: _containers.RepeatedCompositeFieldContainer[DocObj.Entity]
    keywords: _containers.RepeatedCompositeFieldContainer[DocObj.Keyword]
    lang: Lang
    locations: _containers.RepeatedCompositeFieldContainer[DocObj.Location]
    semantic_vector: _containers.RepeatedCompositeFieldContainer[DocObj.Vector]
    text: str
    themes: _containers.RepeatedCompositeFieldContainer[DocObj.Theme]
    title: str
    def __init__(self, article_id: _Optional[int] = ..., text: _Optional[str] = ..., title: _Optional[str] = ..., date: _Optional[str] = ..., lang: _Optional[_Union[Lang, str]] = ..., locations: _Optional[_Iterable[_Union[DocObj.Location, _Mapping]]] = ..., semantic_vector: _Optional[_Iterable[_Union[DocObj.Vector, _Mapping]]] = ..., keywords: _Optional[_Iterable[_Union[DocObj.Keyword, _Mapping]]] = ..., entities: _Optional[_Iterable[_Union[DocObj.Entity, _Mapping]]] = ..., themes: _Optional[_Iterable[_Union[DocObj.Theme, _Mapping]]] = ..., _class: _Optional[_Iterable[_Union[DocObj.Class, _Mapping]]] = ...) -> None: ...

class Lang(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
