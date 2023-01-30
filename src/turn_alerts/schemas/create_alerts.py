""" Schemas to create Alerts from Alert Microservice """
from typing import List, TypedDict, Union
from typing_extensions import NotRequired
from uuid import UUID

from marshmallow import Schema, fields
from marshmallow.validate import OneOf

from turn_alerts.schemas.tags import AlertTagEnum

from .types import AlertTypeEnum, ObjectTypeEnum, UserTypeEnum


class CreateAlertPayloadObjectEntry(TypedDict):
    object_type: ObjectTypeEnum
    id: Union[int, str, UUID]


class CreateAlertPayload(TypedDict):
    title: str
    body: str
    type: AlertTypeEnum
    partner_id: int
    team_member_id: int
    object: NotRequired[CreateAlertPayloadObjectEntry]
    tags: List[AlertTagEnum]


class AlertObjectId(fields.Field):
    def _deserialize(self, value):
        if value is None:
            raise ValueError("Alert Object may not be None")
        return value


class UserAlertSchema(Schema):
    id = fields.UUID()
    partner_id = fields.Integer()
    team_member_id = fields.Integer(required=False)


class ObjectAlertSchema(Schema):
    type = fields.String(validate=OneOf([entry for entry in ObjectTypeEnum]))
    id = AlertObjectId()


class AlertSchema(Schema):
    title = fields.String(required=True)
    body = fields.String(required=True)
    type = fields.String(required=True)
    user = fields.Nested(UserAlertSchema())
    object = fields.Nested(ObjectAlertSchema())
    tags = fields.List(fields.String(), load_default=list)


class AlertResponseSchema(Schema):
    id = fields.UUID()
    title = fields.String()
    body = fields.String()
    type = fields.String()
    user = fields.Nested(UserAlertSchema)
    object = fields.Nested(ObjectAlertSchema)
    active = fields.Boolean()
    created_at = fields.String()
    tags = fields.List(
        fields.Str(validate=OneOf([entry for entry in AlertTagEnum])),
        load_default=list,
    )


class AlertObjectDict(TypedDict):
    id: Union[str, int]
    type: str


class AlertUserDict(TypedDict):
    id: UUID
    partner_id: int
    team_member_id: int


class AlertResponseDict(TypedDict):
    id: UUID
    title: str
    body: str
    type: AlertTypeEnum
    user: AlertUserDict
    object: AlertObjectDict
    active: bool
    created_at: str
    tags: List[str]
