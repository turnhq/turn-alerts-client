""" Session Object for Alerts API Microservice """
from typing import Dict
import requests


class RestAPI:
    __slots__ = ("__host", "__req")
    __host: str
    __req: requests.Session

    def __init__(self, host: str, headers=None) -> None:
        if headers is None:
            headers = {}
        self.__req = requests.Session()
        self.__host = host
        self.__req.headers.update(headers)

    def set_token(self, token) -> None:
        self.__req.headers.update({"Authorization": token})

    def get(self, resource: str):
        res = self.__req.get("".join([self.__host, resource]))
        return res

    def post(self, resource: str, data: Dict):
        res = self.__req.post("".join([self.__host, resource]), json=data)
        return res

    def put(self, resource: str, data: Dict):
        res = self.__req.put("".join([self.__host, resource]), data=data)
        return res

    def delete(self, resource):
        res = self.__req.put("".join([self.__host, resource]))
        return res
