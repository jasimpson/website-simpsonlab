#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jim Simpson'
SITENAME = u'Simpson Lab'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGES_PATHS = ['pages']
STATIC_PATHS = ['uploads']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

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
SOCIAL = (('twitter', '#'),
		  ('github', '#'),
          ('linkedin', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Template related
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False



####################### Theme-Specific Settings #########################
THEME = 'theme/pelican-bootstrap3'

# Pelican Theme-Specific Variables  
BOOTSTRAP_THEME = 'clean'

# Article Info
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = False

# Sidebar Info
HIDE_SIDEBAR = True

# Banne Image
BANNER = 'uploads/home-bg.jpg'
BANNER_SUBTITLE = 'I like building things'
