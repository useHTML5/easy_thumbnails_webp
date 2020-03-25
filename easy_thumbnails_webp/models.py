# coding: utf-8
from __future__ import unicode_literals

# поддержка webp
def store_as_webp(sender, **kwargs):
    webp_path = sender.storage.path('.'.join([sender.name, 'webp']))
    sender.image.save(webp_path, 'webp')


from easy_thumbnails.signals import thumbnail_created

thumbnail_created.connect(store_as_webp)