#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Charlie Pauvert'
SITENAME = 'Charlie Pauvert webpages'
SITEURL = ''


PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('researchgate', 'https://www.researchgate.net/profile/Charlie_Pauvert'),
          ('linkedin', 'https://www.linkedin.com/in/charliepauvert'),
          ('github', 'https://github.com/cpauvert'))
DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Add paths for extra
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = { 'extra/favicon.ico': {'path': 'favicon.ico'} }

# Add a theme
THEME = "pelican-hyde"
# Theme configuration
COLOR_THEME = "0b"
PROFILE_IMAGE = "profile.jpg"
FONT_ACADEMICONS = True
FOOTER_TEXT = "(c) Copyright Charlie Pauvert 2020"


# Markdown configuration
#
MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.codehilite': {'css_class': 'highlight'},
            'markdown.extensions.extra': {},
            'markdown.extensions.meta': {},
            'markdown.extensions.smarty': {},
            },
        'output_format': 'html5',
        }
