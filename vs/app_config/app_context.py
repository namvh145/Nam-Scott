from vs.app_config.context import ESContext
from vs.common.config import Config

"""
Use lazy loading to initiate all instances need for backend application and store in 'globals'
"""


def use_config(config_file):
    config = Config(config_file)
    register('config', config)


def register(instance_name, instance):
    globals()[instance_name] = instance


def get(instance_name):
    instance = globals().get(instance_name)
    if instance is None:
        if instance_name == 'es_context':
            config = get('config')
            instance = ESContext(config)
        elif instance_name == 'es_client':
            es_context = get('es_context')
            instance = es_context.es_client

        # register instance
        register(instance_name, instance)

    return instance
