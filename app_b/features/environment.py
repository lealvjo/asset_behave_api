from util.config import Config
from services.test_support import TestSupport

def before_all(context):
    context.support = TestSupport()
    context.env = Config()
    context.stage = context.env.get_stage(context.config.userdata['STAGE'])

def after_all(context):
    print("report {}reports\n".format(context.env.get_path("features")))