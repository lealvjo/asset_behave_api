import json
from util.config import Config
from jsonschema import validate

class TestSupport(Config):
    def __init__(self):
        Config.__init__(self)

    def validate_schema(self, schema_file, req):
        with open(self.get_path('features') + "schema/" + schema_file, "r") as fp:
            schema = json.load(fp)
        validate(req, schema)