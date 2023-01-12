""" Schemas to create Alerts from Alert Microservice """
from typing import TypedDict
from typing_extensions import NotRequired
from uuid import UUID

from marshmallow import Schema, fields
from marshmallow.validate import OneOf

from .types import AlertTypeEnum, ObjectTypeEnum, UserTypeEnum


class CreateAlertPayloadUserEntry(TypedDict):
    user_type: UserTypeEnum
    id: int


class CreateAlertPayloadObjectEntry(TypedDict):
    object_type: ObjectTypeEnum
    id: int | str | UUID


class CreateAlertPayload(TypedDict):
    title: str
    body: str
    type: AlertTypeEnum
    user: NotRequired[CreateAlertPayloadUserEntry]
    object: CreateAlertPayloadObjectEntry
    tags: NotRequired[list[str]]


class UserAlertSchema(Schema):
    user_type = fields.String()
    id = fields.Integer()


class ObjectAlertSchema(Schema):
    object_type = fields.String(
        validate=OneOf(
            ["advise_job", "s3_upload", "export_request", "background_check"]
        )
    )
    id = fields.Integer()


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
    user_id = fields.String()
    recruitment_partner_id = fields.String(required=False, allow_none=True)
    object_id = fields.String()
    active = fields.Boolean()
    created_at = fields.String()
    tags = fields.List(fields.String, load_default=list)


class AlertResponseDict(TypedDict):
    id: UUID
    title: str
    body: str
    type: AlertTypeEnum
    user_id: str
    recruitment_partner_id: NotRequired[UUID]
    object_id: NotRequired[UUID | str]
    active: bool
    created_at: str
    tags: list[str]
