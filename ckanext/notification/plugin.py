import logging

import twitter

import ckan.plugins as plugins
import ckan.plugins.interfaces as interfaces


log = logging.getLogger(__name__)

class TwitterNotificationPlugin(plugins.SingletonPlugin):

    plugins.implements(interfaces.IConfigurable)
    plugins.implements(interfaces.IDomainObjectModification)

    # Consumer key
    consumer_key = None
    # Consumer secret key
    consumer_secret = None
    # oAuth access token
    access_token_key = None
    # oAuth access secret key
    access_token_secret = None

    def _is_active(self):
        return self.consumer_key and\
               self.consumer_secret and\
               self.access_token_key and\
               self.access_token_secret

    def _tweet(self, name, url):
        api = twitter.Api(consumer_key=self.consumer_key,
                          consumer_secret=self.consumer_secret,
                          access_token_key=self.access_token_key,
                          access_token_secret=self.access_token_secret)
        api.PostUpdate(self.message_template % {'name': name, 'url': url})

    def configure(self, config):
        log.debug("config type %s" % type(config))
        self.consumer_key = config.get('twitter.consumer_key', None)
        self.consumer_secret = config.get('twitter.consumer_secret', None)
        self.access_token_key = config.get('twitter.access_token_key', None)
        self.access_token_secret = config.get('twitter.access_token_secret', None)
        if not self._is_active():
            log.debug("Configration is not enough, Notification plugin is deactivate")
        self.target_format = config.get('twitter.target_format', "").split()
        self.message_template = config.get('twitter.message_template',
                                          "New file comes. %(name)s\nPlease check details in %(url)s")

    def notify(self, entity, operation):
        log.debug("entity %s" % entity)
        log.debug("operation %s" % operation)
        if 'new' == operation and self._is_active() and hasattr(entity, 'format'):
            fmt = entity.format
            if fmt in self.target_format or not self.target_format:
                self._tweet(entity.name, entity.url)
 
