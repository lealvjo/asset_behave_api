from util.configuration_environment import ConfigurationEnvironment as CE

def before_all(context):
    context.env = CE()
    context.stage = context.env.get_env(context.config.userdata['STAGE'])


def after_step(context,step):
    if step.status == 'failed':
        name = 'scenario: ' + str(context.scenario.name) + ' step: ' + str(step.name) + ' = '
        status = str(step.status) + ' '
        print(name + status)
    else:
        print(step.status, step.name)

def after_all(context):
    pass