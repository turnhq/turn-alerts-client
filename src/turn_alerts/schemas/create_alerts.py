""" Schemas to create Alerts from Alert Microservice """
from typing import List, TypedDict, Union
from typing_extensions import NotRequired
from uuid import UUID

from marshmallow import Schema, fields
from marshmallow.validate import OneOf

from turn_alerts.schemas.tags import AlertTagEnum

from .types import AlertTypeEnum, ObjectTypeEnum, UserTypeEnum


class AlertBase(TypedDict):
    tags: List[AlertTagEnum]


class CreateAlertPayloadUserEntry(AlertBase):
    user_type: UserTypeEnum
    id: int


class CreateAlertPayloadObjectEntry(AlertBase):
    object_type: ObjectTypeEnum
    id: Union[int, str, UUID]


class CreateAlertPayload(AlertBase):
    title: str
    body: str
    type: AlertTypeEnum
    user: CreateAlertPayloadUserEntry
    object: NotRequired[CreateAlertPayloadObjectEntry]


class AlertObjectId(fields.Field):
    def _deserialize(self, value):
        if value is None:
            raise ValueError("Alert Object may not be None")
        return value


class UserAlertSchema(Schema):
    user_type = fields.String()
    id = AlertObjectId()


class ObjectAlertSchema(Schema):
    object_type = fields.Enum(AlertTypeEnum)
    id = AlertObjectId()


class AlertSchema(Schema):
    title = fields.String(required=True)
    body = fields.String(required=True)
    type = fields.String(required=True)
    user = fields.Nested(UserAlertSchema())
    object = fields.Nested(ObjectAlertSchema())
    tags = fields.List(fields.String(), load_default=list)


class AlertResponseSchema(Schema):
    id = fields.String()
    title = fields.String()
    body = fields.String()
    type = fields.String()
    user = ObjectAlertSchema()
    object = ObjectAlertSchema()
    active = fields.Boolean()
    created_at = fields.String()
    tags = fields.List(fields.Enum(AlertTagEnum), load_default=list)


class AlertObjectDict(TypedDict):
    id: Union[str, int]
    type: str


class AlertResponseDict(TypedDict):
    id: UUID
    title: str
    body: str
    type: AlertTypeEnum
    user: AlertObjectDict
    object: AlertObjectDict
    active: bool
    created_at: str
    tags: List[str]
