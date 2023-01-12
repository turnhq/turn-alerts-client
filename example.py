import os
from src.turn_alerts.alerts import AlertAPI

from src.schemas.create_alerts import CreateAlertPayload
from src.schemas.types import AlertTypeEnum, ObjectTypeEnum, UserTypeEnum

token = os.environ.get("TOKEN")
host = os.environ.get("HOST")
if not (host and token):
    raise Exception("No host or token set")
alert = AlertAPI(token=token, host=host)

alert_data: CreateAlertPayload = {
    "title": "Testing alert",
    "body": "Prueba de alerta",
    "type": AlertTypeEnum.IMPORT_START_PROCESSING,
    "user": {"user_type": UserTypeEnum.partner, "id": 23},
    "object": {
        "object_type": ObjectTypeEnum.advise_job,
        "id": "b34eba69-f1cd-49ec-813a-b88a268198f5",
    },
    "tags": [],
}

response_alert = alert.create(alert_data)
print(response_alert)
