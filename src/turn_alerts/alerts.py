from typing import Type, cast
from .config import Config
from .exceptions import AlertException
from .rest import RestAPI
from .schemas.create_alerts import (
    AlertResponseDict,
    AlertResponseSchema,
    CreateAlertPayload,
)


class AlertAPI:
    """Alert API Class

    This is the main client class to create, list,
    and mark as inactive alerts through the microservice.
    """

    __slots__ = ("__session", "__config")
    __session: RestAPI
    __config: Type[Config]

    def __init__(self, token: str, host: str):

        self.__session = RestAPI(
            host=host,
            headers={
                "Content-Type": "application/json",
            },
        )
        self.__config = Config
        self.__session.set_token(token)

    def create(self, alert_data: CreateAlertPayload) -> AlertResponseDict:
        res = self.__session.post(self.__config.CREATE_ALERT, dict(alert_data))
        if res.status_code == 200:
            alert_response = AlertResponseSchema()
            data: AlertResponseDict | list = alert_response.dump(res.json())
            return cast(AlertResponseDict, data)
        else:
            raise AlertException()

    def list(self):
        pass

    def mark_all_inactive(self):
        pass

    def get_all_export(self):
        pass

    def register_upload(self):
        pass
