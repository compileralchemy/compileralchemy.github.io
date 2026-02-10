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
import json
import html

import settings

from pathlib import Path

def extract_year(path: str) -> int:
    return int(Path(path).stem)

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
        'slug': slug,
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
        'slug': slug,
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
    gen_book('./data/books/freelancing_codex.md',
        '../../assets/books/freelancing-codex/cover.png',
        "The Programming Freelancing Codex",
        '0.1.0',
        'freelancing-codex',
        'https://www.compileralchemy.com/assets/books/foss_sqlite_internals.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/books/freelancing_codex.md',)

def gen_diaries():
    gen_diary('./data/diaries/2019.toml',
        '../../assets/diaries/2019.png',
        "Diary 2019",
        '0.1.0',
        '2019',
        'https://www.compileralchemy.com/assets/diaries/2019.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)
    gen_diary('./data/diaries/2020.toml',
        '../../assets/diaries/2020.png',
        "Diary 2020",
        '0.1.0',
        '2020',
        'https://www.compileralchemy.com/assets/diaries/2020.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)
    gen_diary('./data/diaries/2021.toml',
        '../../assets/diaries/2021.png',
        "Diary 2021",
        '0.1.0',
        '2021',
        'https://www.compileralchemy.com/assets/diaries/2021.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)
    gen_diary('./data/diaries/2022.toml',
        '../../assets/diaries/2022.png',
        "Diary 2022",
        '0.1.0',
        '2022',
        'https://www.compileralchemy.com/assets/diaries/2022.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)
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
        'https://www.compileralchemy.com/assets/diaries/2024.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)

    gen_diary('./data/diaries/2025.toml',
        '../../assets/diaries/2025.png',
        "Diary 2025",
        '0.1.0',
        '2025',
        'https://www.compileralchemy.com/assets/diaries/2025.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml',
        weasy=settings.book_generate)

    gen_diary('./data/diaries/silicon-valley.toml',
        '../../assets/diaries/silicon_valley.png',
        "Silicon Valley Diary",
        '0.1.0',
        'silicon-valley',
        'https://www.compileralchemy.com/assets/diaries/silicon-valley-abdurrahmaan-janhangeer.pdf',
        'https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/silicon-valley.toml',
        weasy=settings.book_generate)
    

def gen_blog():
    data = ['./data/diaries/2025.toml', './data/diaries/2024.toml', './data/diaries/2023.toml', './data/diaries/2022.toml',
            './data/diaries/2021.toml',
            './data/diaries/2020.toml', './data/diaries/2019.toml']
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'blog'))
    except Exception as e:
        pass
    title_slug = []
    for source in data:
        toml_data = toml.load(source)
        current_year = extract_year(source)
        
        for i, elem in enumerate(toml_data['elements'][::-1]):
            title = elem['title']
            slug = title.casefold().replace(' ', '-').replace('/', '').replace("'", '').replace('?',
                     '').replace('---', '-').replace(':', '').replace(',', '').replace('\u200b', '').replace('\u200c', '')
            content_string = elem['body']
            content = md_to_html(elem['body'])

            title_slug.append([title, slug, current_year])

            try:
                os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'blog', slug))
            except Exception as e:
                pass
            context.update({
                'settings': settings,
                'path': '../../',
                'title': title,
                'slug': slug,
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



def gen_faceblur():
    context.update({
        'path': '../'
    })
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'face-blur'))
    except Exception as e:
        pass
    generate('faceblur.html', join(settings.OUTPUT_FOLDER, 'face-blur', 'index.html'), **context)

ISLAMIC_MONTHS = {
    "01": "Muharram",
    "02": "Safar",
    "03": "Rabi' al-awwal",
    "04": "Rabi' al-thani",
    "05": "Jumada al-awwal",
    "06": "Jumada al-thani",
    "07": "Rajab",
    "08": "Sha'ban",
    "09": "Ramadan",
    "10": "Shawwal",
    "11": "Dhu al-Qi'dah",
    "12": "Dhu al-Hijjah"
}

def gen_islamic_months():
    context.update({
        'path': '../'
    })
    
    months_data = []
    
    try:
        with open('data/months.json', 'r') as f:
            data = json.load(f)
            
            # Navigate structure: months -> year -> month_num -> date
            if 'months' in data:
                for year, year_data in data['months'].items():
                    for month_num, month_info in year_data.items():
                        month_name = ISLAMIC_MONTHS.get(month_num, f"Month {month_num}")
                        
                        date_str = ""
                        src_link = ""
                        
                        if isinstance(month_info, dict):
                            date_str = month_info.get('date', '')
                            src_link = month_info.get('src', '')
                        else:
                            date_str = str(month_info)

                        months_data.append({
                            'year': year,
                            'month_num': month_num,
                            'month_name': month_name,
                            'date': date_str,
                            'src': src_link
                        })
                        
        # Sort by year (desc) then month (desc)
        months_data.sort(key=lambda x: (x['year'], x['month_num']), reverse=True)
        
    except Exception as e:
        print(f"Error processing months.json: {e}")
        pass

    islamic_context = context.copy()
    islamic_context.update({
        'months_data': months_data,
        'months_data_json': json.dumps(months_data),
        'years_count': len(data.get('months', {}))
    })

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, 'islamic-months-mauritius'))
    except Exception as e:
        pass
        
    generate('islamic-months-mauritius.html', join(settings.OUTPUT_FOLDER, 'islamic-months-mauritius', 'index.html'), **islamic_context)


def gen_seo():
    urls = [
        '/',
        '/alfa-podcast/',
        '/blog/',
        '/articles/',
        '/talks/',
        '/journey/',
        '/face-blur/',
        '/islamic-months-mauritius/',
        '/books/sqlite-internals/',
        '/books/freelancing-codex/',
        '/diaries/2019/',
        '/diaries/2020/',
        '/diaries/2021/',
        '/diaries/2022/',
        '/diaries/2023/',
        '/diaries/2024/',
        '/diaries/2025/',
        '/diaries/silicon-valley/',
    ]

    # Blog posts
    blog_data = ['./data/diaries/2025.toml', './data/diaries/2024.toml', './data/diaries/2023.toml', './data/diaries/2022.toml',
            './data/diaries/2021.toml',
            './data/diaries/2020.toml', './data/diaries/2019.toml']
    for source in blog_data:
        if os.path.exists(source):
            toml_data = toml.load(source)
            for elem in toml_data['elements']:
                title = elem['title']
                slug = title.casefold().replace(' ', '-').replace('/', '').replace("'", '').replace('?',
                         '').replace('---', '-').replace(':', '').replace(',', '').replace('\u200b', '').replace('\u200c', '')
                urls.append(f'/blog/{slug}/')

    # robots.txt
    robots_content = """User-agent: *
Allow: /

User-agent: OpenAI
Disallow: /

User-agent: GPTBot
Disallow: /

# Disallow Google AI crawlers
User-agent: Bard
Disallow: /

# Disallow Anthropic AI
User-agent: Claude
Disallow: /

# Disallow Microsoft AI crawlers
User-agent: BingAI
Disallow: /

# Disallow CommonCrawl (often used by AI models for datasets)
User-agent: CCBot
Disallow: /

# Disallow Neeva AI (deprecated but still included for completeness)
User-agent: NeevaBot
Disallow: /

# Disallow Baidu AI
User-agent: Baiduspider
Disallow: /

# Disallow Yandex AI
User-agent: YandexBot
Disallow: /

# Disallow other common web crawlers used for AI data collection
User-agent: DuckDuckGo-Bot
Disallow: /

User-agent: AhrefsBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: DotBot
Disallow: /

User-agent: BLEXBot
Disallow: /

User-agent: PetalBot
Disallow: /

Sitemap: https://compileralchemy.com/sitemap.xml
Sitemap: https://compileralchemy.com/sitemap.txt"""
    
    with open(join(settings.OUTPUT_FOLDER, 'robots.txt'), 'w') as f:
        f.write(robots_content)

    # sitemap.txt
    with open(join(settings.OUTPUT_FOLDER, 'sitemap.txt'), 'w') as f:
        for url in urls:
            f.write(f"{settings.BASE_URL}{url}\n")

    # sitemap.xml
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        escaped_url = html.escape(f"{settings.BASE_URL}{url}")
        sitemap_xml.append('  <url>')
        sitemap_xml.append(f'    <loc>{escaped_url}</loc>')
        sitemap_xml.append('  </url>')
    sitemap_xml.append('</urlset>')

    with open(join(settings.OUTPUT_FOLDER, 'sitemap.xml'), 'w') as f:
        f.write('\n'.join(sitemap_xml))


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
        gen_faceblur()
        gen_islamic_months()
        gen_seo()

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
