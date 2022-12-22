import base64
import json
import logging
import os
import allure
import curlify
from requests import Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url=kwargs.pop('base_url')
        super().__init__()


    def request(self, method, url,**kwargs):
        with allure.step(f'{method} {url}'):
            response= super().request(method, f'{self.base_url}{url}', **kwargs)

            massege_curl = curlify.to_curl(response.request)
            logging.info(f'{response.status_code} {massege_curl}')
            allure.attach(
                body=massege_curl.encode('utf=8'),
                name=f'Request {response.request.method} {response.status_code}',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt')
            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf=8'),
                    name=f'Response {response.request.method} {response.status_code}',
                    attachment_type=allure.attachment_type.JSON,
                    extension='json')
            except ValueError as error:
                allure.attach(
                    body=response.text.encode('utf=8'),
                    name=f'Response {response.request.method} {response.status_code}',
                    attachment_type=allure.attachment_type.TEXT,
                    extension='txt')
            return response














