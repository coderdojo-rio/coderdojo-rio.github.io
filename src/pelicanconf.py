#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'coderdojorio'
SITENAME = u'CoderDojo Rio'
SITESUBTITLES = [u'CoderDojo Rio', '<img src="static/logo-coderdojo.png" alt="Logo" />']
SITEURL = 'corderdojorio.com.br'
THEME = 'pelican-bold'

PATH = 'content'
STATIC_PATHS = ['static']
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
INDEX_SAVE_AS = 'index.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
OUTPUT_PATH = '..'
DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
PLUS_ONE = True
DISQUS_SITENAME = 'coderdojorio'
GOOGLE_ANALYTICS = 'UA-58403599-2'

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/coderdojorio'),
          ('linkedin', 'https://www.linkedin.com/company/coderdojo-rio'),
          ('github', 'https://github.com/coderdojo-rio'),
          ('email', 'mailto:contato@coderdojorio.com.br'),
          ('google', 'https://groups.google.com/forum/#!forum/coderdojo-rio'),
          ('rss', '/feeds/all.atom.xml'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
