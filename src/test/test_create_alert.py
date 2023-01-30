import vcr
from turn_alerts.alerts import AlertAPI

from turn_alerts.schemas.create_alerts import CreateAlertPayload
from turn_alerts.schemas.types import AlertTypeEnum, ObjectTypeEnum, UserTypeEnum
from turn_alerts.schemas.tags import AlertTagEnum

base_vcr = vcr.VCR(
    cassette_library_dir="src/test/cassettes",
)


def test_create_alert(host: str, internal_token: str):
    alert = AlertAPI(token=internal_token, host=host)

    alert_data: CreateAlertPayload = {
        "title": "Testing alert",
        "body": "Prueba de alerta",
        "type": AlertTypeEnum.IMPORT_START_PROCESSING,
        "object": {
            "object_type": ObjectTypeEnum.advise_job,
            "id": "b34eba69-f1cd-49ec-813a-b88a268198f5",
        },
        "partner_id": 1,
        "team_member_id": 1,
        "tags": [AlertTagEnum.SCREEN],
    }
    with base_vcr.use_cassette("create_alert1.yml", match_on=["url"]):
        response_alert = alert.create(alert_data)
        assert response_alert
        assert response_alert["body"] == alert_data["body"]
        assert response_alert["object"]["type"] == alert_data["object"]["object_type"]
        assert response_alert["user"]["partner_id"] == alert_data["partner_id"]
        assert response_alert["user"]["team_member_id"] == alert_data["team_member_id"]
