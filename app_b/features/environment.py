from util.configuration_environment import ConfigurationEnvironment as ce

def before_all(context):
    context.env = ce()
    context.stage = context.env.get_stage(context.config.userdata['STAGE'])

def after_all(context):
    print("report {} reports\n".format(context.env.get_path("features")))