import yaml
import json
from os.path import dirname, abspath
from jsonschema import validate

class ConfigurationEnvironment(object):
    def __init__(self):
        pass

    def get_stage(self, stage):
        with open(self.get_path('features') + "stage/environment.yml", "r") as f:
            try:
                self.env = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)
        return self.env['environment'][stage]

    def get_schema(self, schema_file, b):
        with open(self.get_path('features') + "schema/" + schema_file, "r") as fp:
            schema = json.load(fp)
        validate(b , schema)

    def get_path(self, f):
        if "\\" in dirname(abspath(__file__)):
            t = "\\"
        else:
            t = "/"
        path = ""
        root = [r + "/" for r in dirname(abspath(__file__)).split(t)]
        for r in root:
            if f in r:
                path += r
                break
            else:
                path += r
        return path

