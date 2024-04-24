# https://github.com/pymug/website-AV19-AV20

import datetime
import sys
import uuid
from os.path import join
import os
from email import utils as emailutils
import time 

from flask import Flask
from jamstack.api.template import generate
from jamstack.api.template import base_context
from livereload import Server
import markdown
import toml

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

def gen_book(mdfile, cover, title, build_number, slug, download_link, edit_link):
    context = base_context()
    

    sqlite_book = mdfile
    with open(sqlite_book, encoding='utf8') as f:
        text = f.read()

    html = md_to_html(text)
    
    book = {
        'content': html,
        'cover': cover,
        'title': title,
        'download_link': download_link,
        'edit_link': edit_link
    }

    context.update({
        'settings': settings,
        'path': '../../',
        'book': book,
        'build_number': build_number
    })

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'books'))
    except Exception as e:
        pass 

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'books', slug))
    except Exception as e:
        pass
    generate('book.html', join(settings.OUTPUT_FOLDER, 'books', slug, 'index.html'), **context)


def gen_diary(mdfile, cover, title, build_number, slug, download_link, edit_link, weasy=False):
    book_title = title
    context = base_context()
    

    # sqlite_book = mdfile
    # with open(sqlite_book, encoding='utf8') as f:
    #     text = f.read()

    # html = md_to_html(text)

    data = toml.load(mdfile)


    content_elems = []
    toc_elems = ['<ol class="toc">']

    for i, elem in enumerate(data['elements']):
        title = elem['title']
        body = elem['body']
        title_slug = title.replace(' ', '-')
        index = str(i+1).zfill(2)
        toc_elems.append(f'''<li><a href="#{title_slug}">{index}. {title}</a></li>''')
        content_elems.append(f'<a href="#{title_slug}"><h1 id="{title_slug}" class="chapter">{title}</h1></a>')
        content_elems.append(md_to_html(body))
    toc_elems.append('</ol>')

    toc = '\n'.join(toc_elems)

    content_ = '\n'.join(content_elems)

    content = toc + '\n' + content_
    
    book = {
        'content': content,
        'cover': cover,
        'title': book_title,
        'download_link': download_link,
        'edit_link': edit_link
    }

    context.update({
        'settings': settings,
        'path': '../../',
        'book': book,
        'build_number': build_number
    })

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'diaries'))
    except Exception as e:
        pass 

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'diaries', slug))
    except Exception as e:
        pass
    generate('diary.html', join(settings.OUTPUT_FOLDER, 'diaries', slug, 'index.html'), **context)
    
    if weasy:
        try:
            os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'diaries', slug+'-weasy'))
        except Exception as e:
            pass
        generate('diary-weasy.html', join(settings.OUTPUT_FOLDER, 'diaries', slug+'-weasy', 'index.html'), **context)

def gen_books():
    gen_book('./data/books/sqlite_internals.md',
        '../../assets/books/sqlite-internals/cover.png',
        "SQLite Internals: How The World's Most Used Database Works",
        '0.12.0',
        'sqlite-internals',
        'https://www.compileralchemy.com/assets/books/foss_sqlite_internals.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/books/sqlite_internals.md',)
    # gen_book('./data/books/cracking_tough_parts_python.md',
    #     '../../assets/books/cracking-python/cover.png',
    #     "Cracking The Tough Parts In Python",
    #     '0.1.0',
    #     'cracking-python',
    #     'https://www.compileralchemy.com/assets/books/cracking_python.pdf',
    #     'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/books/cracking_tough_parts_python.md')

def gen_diaries():
    gen_diary('./data/diaries/2023.toml',
        '../../assets/diaries/2023.png',
        "Diary 2023",
        '0.1.0',
        '2023',
        'https://www.compileralchemy.com/assets/diaries/2023.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)
    
    gen_diary('./data/diaries/2024.toml',
        '../../assets/diaries/2024.png',
        "Diary 2024",
        '0.1.0',
        '2024',
        'https://www.compileralchemy.com/assets/diaries/2023.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)
    

def gen_blog():
    data = ['./data/diaries/2024.toml', './data/diaries/2023.toml', './data/diaries/2022.toml',
            './data/diaries/2021.toml',
            './data/diaries/2020.toml', './data/diaries/2019.toml']
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'blog'))
    except Exception as e:
        pass
    title_slug = []
    for source in data:
        toml_data = toml.load(source)
        
        for i, elem in enumerate(toml_data['elements'][::-1]):
            title = elem['title']
            slug = title.casefold().replace(' ', '-').replace('/', '').replace("'", '').replace('?',
                     '').replace('---', '-').replace(':', '')
            content_string = elem['body']
            content = md_to_html(elem['body'])

            title_slug.append([title, slug])

            try:
                os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'blog', slug))
            except Exception as e:
                pass
            context.update({
                'settings': settings,
                'path': '../../',
                'title': title,
                'content': content,
                'content_string': content_string
            })
            generate('blog.html', join(settings.OUTPUT_FOLDER, 'blog', slug, 'index.html'), **context)
    
    context.update({
                'settings': settings,
                'path': '../',
                'title_slug': title_slug,
            })
    generate('blog_index.html', join(settings.OUTPUT_FOLDER, 'blog', 'index.html'), **context)
def gen_writings():
    context.update({
        'path': '../'
    })
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'articles'))
    except Exception as e:
        pass
    generate('pages/writings.html', join(settings.OUTPUT_FOLDER, 'articles', 'index.html'), **context)

def gen_talks():
    context.update({
        'path': '../'
    })
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'talks'))
    except Exception as e:
        pass
    generate('pages/talks.html', join(settings.OUTPUT_FOLDER, 'talks', 'index.html'), **context)

def gen_journey():
    context.update({
        'path': '../'
    })
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'journey'))
    except Exception as e:
        pass
    generate('pages/journey.html', join(settings.OUTPUT_FOLDER, 'journey', 'index.html'), **context)

def main(args):
    def gen():
        generate('index.html', join(settings.OUTPUT_FOLDER, 'index.html'), **context)

        try:
            os.mkdir(join(settings.OUTPUT_FOLDER, 'alfa-podcast'))
        except Exception as e:
            print('skip', e)
            pass
        generate('podcast.html', join(settings.OUTPUT_FOLDER, 'alfa-podcast', 'index.html'), **podcontext)
        gen_podcast_rss()
        gen_books()
        gen_diaries()
        gen_writings()
        gen_talks()
        gen_journey()
        gen_blog()

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
