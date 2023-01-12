""" Schema for listing Alerts from Alert Microservice """

from marshmallow import Schema, fields


class AlertItemSchema(Schema):
    alert_type = fields.String()
    id = fields.String()
    title = fields.String()
    body = fields.String()
    type = fields.String()
    user_id = fields.String()
    recruitment_partner_id = fields.String(required=False)
    object_id = fields.String()
    active = fields.Boolean()
    created_at = fields.String()
    tags = fields.List(fields.String(), default=list)


class AlertFilterSchema(Schema):
    limit = fields.Integer()
    page = fields.Integer()
    unread_only = fields.Boolean()
    partner_id = fields.Integer()
    recruitment_marketing_partner_id = fields.String(required=False)
    advise_job_id = fields.String()
    type = fields.String()
    since = fields.DateTime()
    tags = fields.List(fields.String(), default=list)
    created_at = fields.String()


class AlertList(Schema):
    alerts = fields.List(fields.Nested(AlertItemSchema()))
    filters = fields.List(fields.Nested(AlertFilterSchema()))
    last_page = fields.Boolean()
    count = fields.Integer()
    unread_count = fields.Integer()
