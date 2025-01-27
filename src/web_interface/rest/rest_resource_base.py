from typing import Type

from flask import request
from flask_restx import Model, Resource, marshal

from intercom.front_end_binding import InterComFrontEndBinding
from web_interface.frontend_database import FrontendDatabase


class RestResourceBase(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = kwargs.get('config', None)
        self.db: FrontendDatabase = kwargs.get('db', None)
        self.intercom: Type[InterComFrontEndBinding] = kwargs.get('intercom', None)

    @staticmethod
    def validate_payload_data(model: Model) -> dict:
        model.validate(request.json or {})
        return marshal(request.json, model)

    def _setup_db(self, config):
        pass
