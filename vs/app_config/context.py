import logging

from elasticsearch import Elasticsearch

logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s', level=logging.ERROR)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class ESContext(object):
    """
    Elasticsearch application context
    """

    def __init__(self, config):

        log.info('Initialize context of application using elasticsearch...')
        # elasticsearch
        self.es_host = config.get('elasticsearch', 'elastic.host')
        self.es_port = config.getint('elasticsearch', 'elastic.port')
        self.es_xpack = config.getboolean('elasticsearch', 'elastic.xpack.enabled')
        if self.es_xpack:
            self.es_user = config.get('elasticsearch', 'elastic.xpack.user')
            self.es_password = config.get('elasticsearch', 'elastic.xpack.password')
            self.es_client = Elasticsearch(
                hosts=[self.es_host],
                http_auth=(self.es_user, self.es_password),
                scheme="http",
                port=self.es_port,
            )
        else:
            self.es_client = Elasticsearch(hosts=[self.es_host], port=self.es_port)

        self.elastic_endpoint = 'http://%s:%s' % (self.es_host, self.es_port)
