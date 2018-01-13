#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Izabela Borges'
SITENAME = 'the worthless data science blog ever'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('globe', 'http://izabelacborges.com'),
         ('twitter', 'https://twitter.com/belacb_'),
	 ('linkedin', 'https://br.linkedin.com/in/izabelacborges'),
	 ('github', 'https://github.com/izabelacborges'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/belacb/pelican-themes/hyde'

BIO = "A Data Scientist wannabe, AI enthusiast that likes to discuss it's ethics, front-ender by fun, bookworm, yogini and painter on the free hours."
PROFILE_IMAGE = 'avatar.jpg'

DISQUS_SITENAME = 'izabelacborges-com-blog'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
