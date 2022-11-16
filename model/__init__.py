import logging
logger = logging.getLogger('base')


def create_model(opt):
    from .model import CDM
    m = CDM(opt)
    logger.info('Model [{:s}] is created.'.format(m.__class__.__name__))
    return m
