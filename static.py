# https://github.com/pymug/website-AV19-AV20

import datetime
import sys
import uuid
from os.path import join
from email import utils as emailutils
import time 

from flask import Flask
from jamstack.api.template import generate
from jamstack.api.template import base_context
from livereload import Server
import markdown

import settings

import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)


def md_to_html_raw(text, extentions=["extra", "smarty", "meta"]):
    md = markdown.Markdown(extensions=extentions)
    html = md.convert(text)
    metadata = md.Meta
    return html, metadata

def md_to_html(*args, **kwargs):
    return md_to_html_raw(*args, **kwargs)[0]

def to_rfc822(t):
    now = datetime.datetime.strptime(t, f'%d-%m-%Y')
    nowtuple = now.timetuple()
    nowtimestamp = time.mktime(nowtuple)
    rfc822 = emailutils.formatdate(nowtimestamp)
    pub_date = rfc822
    return pub_date

context = base_context()
context.update({
    'testimonials': settings.testimonials,
    'writings': settings.writings,
    'talks': settings.talks,
    'str': str,
    'titlecase': titlecase,
    'settings': settings,
    'md_to_html': md_to_html,
    'path': '/'
})

podcontext = base_context()
podcontext.update({
    'settings': settings,
    'md_to_html': md_to_html,
    'path': '../'
    })


def gen_podcast_rss():
    podcast_info = settings.podcasts 

    for i,p in enumerate(podcast_info):

        podcast_info[i]['pubDate'] = to_rfc822(p['date'])

    prss_context = {
        'settings': settings,
        'podcast_info': podcast_info
    }
    generate('podcast.rss', join(settings.OUTPUT_FOLDER, 'alfa-podcast', 'podcast.rss'), **prss_context)


def main(args):
    def gen():
        generate('index.html', join(settings.OUTPUT_FOLDER, 'index.html'), **context)
        generate('podcast.html', join(settings.OUTPUT_FOLDER, 'alfa-podcast', 'index.html'), **podcontext)
        gen_podcast_rss()

    if len(args) > 1 and args[1] == '--server':
        app = Flask(__name__)

        # remember to use DEBUG mode for templates auto reload
        # https://github.com/lepture/python-livereload/issues/144
        app.debug = True
        server = Server(app.wsgi_app)

        # run a shell command
        # server.watch('.', 'make static')

        # run a function

        server.watch('.', gen, delay=5)
        server.watch('*.py')

        # output stdout into a file
        # server.watch('style.less', shell('lessc style.less', output='style.css'))

        server.serve()
    else:
        print(':::')
        gen()

if __name__ == '__main__':
    main(sys.argv)
