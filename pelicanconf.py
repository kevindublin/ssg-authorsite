#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kevin Dublin'
SITENAME = 'Kevin Dublin | Educator, Writer, Programmer'
SITEURL = 'https://kevindublin.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

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
SOCIAL = (('Twitter', 'https://twitter.com/parteverything'),
          ('Instagram', 'https://www.instagram.com/kevdublin/'),)

DEFAULT_PAGINATION = 10
THEME = "themes/brutalist"
# Plugins Settings
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap', 'share_post']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Static Paths
STATIC_PATHS = ['images', 'pdfs']

# Theme Settings
THEME = 'themes/brutalist'
## used for OG tags and Twitter Card data on index page
SITEIMAGE = 'site-cover.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Author site & blog archive for Kevin Dublin'
## path to favicon
FAVICON = 'favicon.png'
## path to logo for nav menu (optional)
LOGO = 'logo.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Kevin'
## google analytics (fake code commented out)
GOOGLE_ANALYTICS = 'UA-40659889-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@parteverything'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = False
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [
			('archived blog', '/categories.html'),
			]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
TWITTER = 'https://twitter.com/parteverything'
INSTAGRAM = 'https://www.instagram.com/kevdublin/'
GITHUB = 'https://github.com/kevindublin'
FACEBOOK = 'https://www.facebook.com/kevindublin/'
LINKEDIN = 'https://www.linkedin.com/in/vindublin'
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
DISQUS_SITENAME = 'kevindublin'
## Gravatar
GRAVATAR = 'https://s.gravatar.com/avatar/ac0a0049d7c9a1c351d0ff85c265d441?s=80'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
