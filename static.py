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
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(), s)


def md_to_html_raw(text, extentions=["extra", "smarty", "meta"]):
    md = markdown.Markdown(extensions=extentions)
    html = md.convert(text)
    metadata = md.Meta
    return html, metadata


def md_to_html(*args, **kwargs):
    return md_to_html_raw(*args, **kwargs)[0]


def to_rfc822(t):
    now = datetime.datetime.strptime(t, f"%d-%m-%Y")
    nowtuple = now.timetuple()
    nowtimestamp = time.mktime(nowtuple)
    rfc822 = emailutils.formatdate(nowtimestamp)
    pub_date = rfc822
    return pub_date


COLORS = ['#f0f7ff', '#fff7ec', '#f8f5ff', '#f5fdf8']

SECTION_ORDER = [
    'talks', 'publish', 'writings', 'papers',
    'blog_index_snippet', 'tools', 'projects',
    'facts', 'community', 'privacy',
]

section_colors = {}
for i, name in enumerate(SECTION_ORDER):
    section_colors[name] = COLORS[i % len(COLORS)]

def section_bg(name):
    return section_colors.get(name, 'transparent')

context = base_context()
context.update(
    {
        "testimonials": settings.testimonials,
        "writings": settings.writings,
        "talks": settings.talks,
        "str": str,
        "titlecase": titlecase,
        "settings": settings,
        "md_to_html": md_to_html,
        "path": "/",
        "seo_title": "Abdur-Rahmaan Janhangeer | Python Software Engineer & Author",
        "seo_description": "Software Engineer, Author of SQLite Internals, and Python freelancer specializing in backend systems and open source.",
        "page_path": "",
        "section_bg": section_bg,
    }
)

podcontext = base_context()
podcontext.update({"settings": settings, "md_to_html": md_to_html, "path": "../", "page_path": "alfa-podcast/"})


def gen_podcast_rss():
    podcast_info = settings.podcasts

    for i, p in enumerate(podcast_info):
        podcast_info[i]["pubDate"] = to_rfc822(p["date"])

    prss_context = {"settings": settings, "podcast_info": podcast_info}

    generate(
        "podcast.rss",
        join(settings.OUTPUT_FOLDER, "alfa-podcast", "podcast.rss"),
        **prss_context,
    )


def gen_book(mdfile, cover, title, build_number, slug, download_link, edit_link):
    context = base_context()

    sqlite_book = mdfile
    with open(sqlite_book, encoding="utf8") as f:
        text = f.read()

    html = md_to_html(text)

    book = {
        "content": html,
        "cover": cover,
        "title": title,
        "download_link": download_link,
        "edit_link": edit_link,
    }

    context.update(
        {
            "settings": settings,
            "path": "../../",
            "book": book,
            "slug": slug,
            "build_number": build_number,
        }
    )

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "books"))
    except Exception as e:
        pass
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "books", slug))
    except Exception as e:
        pass
    context.update(
        {
            "seo_title": f"{title} | Abdur-Rahmaan Janhangeer",
            "seo_description": f"Explore {title} by Abdur-Rahmaan Janhangeer. Deep dive into database internals, systems engineering, and advanced Python.",
            "page_path": f"books/{slug}/",
            "og_type": "book",
        }
    )
    generate(
        "book.html",
        join(settings.OUTPUT_FOLDER, "books", slug, "index.html"),
        **context,
    )


def gen_diary(
    mdfile, cover, title, build_number, slug, download_link, edit_link, weasy=False
):
    book_title = title
    context = base_context()

    # sqlite_book = mdfile
    # with open(sqlite_book, encoding='utf8') as f:
    #     text = f.read()

    # html = md_to_html(text)

    data = toml.load(mdfile)

    content_elems = []
    toc_elems = ['<ol class="toc">']

    for i, elem in enumerate(data["elements"]):
        title = elem["title"]
        body = elem["body"]
        title_slug = title.replace(" ", "-")
        index = str(i + 1).zfill(2)
        toc_elems.append(f"""<li><a href="#{title_slug}">{index}. {title}</a></li>""")
        content_elems.append(
            f'<a href="#{title_slug}"><h1 id="{title_slug}" class="chapter">{title}</h1></a>'
        )
        content_elems.append(md_to_html(body))
    toc_elems.append("</ol>")

    toc = "\n".join(toc_elems)

    content_ = "\n".join(content_elems)

    content = toc + "\n" + content_

    book = {
        "content": content,
        "cover": cover,
        "title": book_title,
        "download_link": download_link,
        "edit_link": edit_link,
    }

    context.update(
        {
            "settings": settings,
            "path": "../../",
            "book": book,
            "slug": slug,
            "build_number": build_number,
        }
    )

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "diaries"))
    except Exception as e:
        pass

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "diaries", slug))
    except Exception as e:
        pass
    generate(
        "diary.html",
        join(settings.OUTPUT_FOLDER, "diaries", slug, "index.html"),
        **context,
    )

    if weasy:
        try:
            os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "diaries", slug + "-weasy"))
        except Exception as e:
            pass
        generate(
            "diary-weasy.html",
            join(settings.OUTPUT_FOLDER, "diaries", slug + "-weasy", "index.html"),
            **context,
        )


def gen_books():
    gen_book(
        "./data/books/sqlite_internals.md",
        "../../assets/books/sqlite-internals/cover.png",
        "SQLite Internals: How The World's Most Used Database Works",
        "0.12.0",
        "sqlite-internals",
        "https://www.compileralchemy.com/assets/books/foss_sqlite_internals.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/books/sqlite_internals.md",
    )
    gen_book(
        "./data/books/freelancing_codex.md",
        "../../assets/books/freelancing-codex/cover.png",
        "The Programming Freelancing Codex",
        "0.1.0",
        "freelancing-codex",
        "https://www.compileralchemy.com/assets/books/foss_sqlite_internals.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/books/freelancing_codex.md",
    )

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "books"))
    except Exception as e:
        pass

    book_context = context.copy()
    book_context.update({"page_path": "books/"})
    generate(
        "pages/books.html",
        join(settings.OUTPUT_FOLDER, "books", "index.html"),
        **book_context,
    )


def gen_diaries():
    gen_diary(
        "./data/diaries/2019.toml",
        "../../assets/diaries/2019.png",
        "Diary 2019",
        "0.1.0",
        "2019",
        "https://www.compileralchemy.com/assets/diaries/2019.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml",
        weasy=settings.book_generate,
    )
    gen_diary(
        "./data/diaries/2020.toml",
        "../../assets/diaries/2020.png",
        "Diary 2020",
        "0.1.0",
        "2020",
        "https://www.compileralchemy.com/assets/diaries/2020.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml",
        weasy=settings.book_generate,
    )
    gen_diary(
        "./data/diaries/2021.toml",
        "../../assets/diaries/2021.png",
        "Diary 2021",
        "0.1.0",
        "2021",
        "https://www.compileralchemy.com/assets/diaries/2021.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml",
        weasy=settings.book_generate,
    )
    gen_diary(
        "./data/diaries/2022.toml",
        "../../assets/diaries/2022.png",
        "Diary 2022",
        "0.1.0",
        "2022",
        "https://www.compileralchemy.com/assets/diaries/2022.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml",
        weasy=settings.book_generate,
    )
    gen_diary(
        "./data/diaries/2023.toml",
        "../../assets/diaries/2023.png",
        "Diary 2023",
        "0.1.0",
        "2023",
        "https://www.compileralchemy.com/assets/diaries/2023.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml",
        weasy=settings.book_generate,
    )

    gen_diary(
        "./data/diaries/2024.toml",
        "../../assets/diaries/2024.png",
        "Diary 2024",
        "0.1.0",
        "2024",
        "https://www.compileralchemy.com/assets/diaries/2024.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml",
        weasy=settings.book_generate,
    )

    gen_diary(
        "./data/diaries/2025.toml",
        "../../assets/diaries/2025.png",
        "Diary 2025",
        "0.1.0",
        "2025",
        "https://www.compileralchemy.com/assets/diaries/2025.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/2023.toml",
        weasy=settings.book_generate,
    )

    gen_diary(
        "./data/diaries/silicon-valley.toml",
        "../../assets/diaries/silicon_valley.png",
        "Silicon Valley Diary",
        "0.1.0",
        "silicon-valley",
        "https://www.compileralchemy.com/assets/diaries/silicon-valley-abdurrahmaan-janhangeer.pdf",
        "https://github.com/compileralchemy/compileralchemy.github.io/blob/source/data/diaries/silicon-valley.toml",
        weasy=settings.book_generate,
    )


def parse_blog_md(filepath):
    """Parse a blog markdown file: title: <title>\n---\n<body>"""
    with open(filepath, encoding="utf-8") as f:
        text = f.read()
    parts = text.split("---", 1)
    if len(parts) != 2:
        return None, None
    header = parts[0].strip()
    body = parts[1].strip()
    if header.startswith("title:"):
        title = header[6:].strip()
    else:
        return None, None
    return title, body


def gen_blog():
    blogs_dir = "./data/blogs/"
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "blog"))
    except Exception as e:
        pass

    # Discover all blog posts from data/blogs/<year>/<seq>_<slug>.md
    all_posts = []
    if os.path.exists(blogs_dir):
        for year_str in sorted(os.listdir(blogs_dir), reverse=True):
            year_dir = os.path.join(blogs_dir, year_str)
            if not os.path.isdir(year_dir):
                continue
            try:
                year = int(year_str)
            except ValueError:
                continue
            year_posts = []
            for fn in os.listdir(year_dir):
                if not fn.endswith(".md"):
                    continue
                name = fn[:-3]
                parts = name.split("_", 1)
                if len(parts) != 2:
                    continue
                seq_str, slug = parts
                try:
                    seq = int(seq_str)
                except ValueError:
                    continue
                filepath = os.path.join(year_dir, fn)
                title, body = parse_blog_md(filepath)
                if title is None:
                    continue
                year_posts.append((seq, slug, title, body))
            year_posts.sort(key=lambda x: x[0], reverse=True)
            for seq, slug, title, body in year_posts:
                all_posts.append((year, slug, title, body))

    # all_posts: newest year first, oldest-first within each year
    total_posts = len(all_posts)
    title_slug = []
    current_post_num = total_posts
    for year, slug, title, body in all_posts:
        title_slug.append(
            {
                "title": title,
                "slug": slug,
                "year": year,
                "num": current_post_num,
            }
        )
        current_post_num -= 1

    # Pre-load post bodies
    post_bodies = {slug: body for _, slug, _, body in all_posts}

    for idx, post in enumerate(title_slug):
        slug = post["slug"]
        try:
            os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "blog", slug))
        except Exception as e:
            pass

        prev_post = title_slug[idx + 1] if idx + 1 < len(title_slug) else None
        next_post = title_slug[idx - 1] if idx - 1 >= 0 else None

        body = post_bodies.get(slug, "")

        blog_context = context.copy()
        blog_context.update(
            {
                "settings": settings,
                "path": "../../",
                "title": post["title"],
                "slug": slug,
                "content": md_to_html(body),
                "content_string": body,
                "article_num": post["num"],
                "seo_title": f"{post['title']} | Abdur-Rahmaan Janhangeer Blog",
                "seo_description": (post["title"][:155] + "...")
                if len(post["title"]) > 160
                else post["title"],
                "page_path": f"blog/{slug}/",
                "og_type": "article",
                "prev_post": prev_post,
                "next_post": next_post,
            }
        )
        generate(
            "blog.html",
            join(settings.OUTPUT_FOLDER, "blog", slug, "index.html"),
            **blog_context,
        )

    index_context = context.copy()
    index_context.update(
        {
            "settings": settings,
            "path": "../",
            "title_slug": title_slug,
            "page_path": "blog/",
        }
    )
    generate(
        "blog_index.html",
        join(settings.OUTPUT_FOLDER, "blog", "index.html"),
        **index_context,
    )
    return title_slug


def gen_writings():
    context.update(
        {
            "path": "../",
            "seo_title": "Luminotes | Technical Deep Dives by Abdur-Rahmaan Janhangeer",
            "seo_description": "Luminotes — a technical newsletter read by engineers at Google, Amazon, Apple, IBM, and Facebook. Deep dives into Python, databases, systems internals, and AI.",
            "page_path": "articles/",
            "og_type": "website",
        }
    )
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "articles"))
    except Exception as e:
        pass
    generate(
        "pages/writings.html",
        join(settings.OUTPUT_FOLDER, "articles", "index.html"),
        **context,
    )


def gen_talks():
    context.update(
        {
            "path": "../",
            "seo_title": "Conference Talks & Presentations | Abdur-Rahmaan Janhangeer",
            "seo_description": "Conference talks by Abdur-Rahmaan Janhangeer on Flask, Python internals, and Open Source.",
            "page_path": "talks/",
            "og_type": "website",
        }
    )
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "talks"))
    except Exception as e:
        pass
    generate(
        "pages/talks.html",
        join(settings.OUTPUT_FOLDER, "talks", "index.html"),
        **context,
    )


def gen_opensource():
    opensource_context = context.copy()
    opensource_context.update(
        {
            "path": "../",
            "seo_title": "OpenSource Projects | Abdur-Rahmaan Janhangeer",
            "seo_description": "Open source projects by Abdur-Rahmaan Janhangeer.",
            "page_path": "opensource/",
            "og_type": "website",
        }
    )
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "opensource"))
    except Exception as e:
        pass
    generate(
        "pages/opensource.html",
        join(settings.OUTPUT_FOLDER, "opensource", "index.html"),
        **opensource_context,
    )


def gen_papers():
    papers_context = context.copy()
    papers_context.update(
        {
            "path": "../",
            "seo_title": "Papers | Abdur-Rahmaan Janhangeer",
            "seo_description": "Paper walkthroughs and commentary by Abdur-Rahmaan Janhangeer.",
            "page_path": "papers/",
            "og_type": "website",
        }
    )
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "papers"))
    except Exception as e:
        pass
    generate(
        "pages/papers.html",
        join(settings.OUTPUT_FOLDER, "papers", "index.html"),
        **papers_context,
    )


def gen_journey():
    context.update(
        {
            "path": "../",
            "seo_title": "My Software Engineering Journey | Abdur-Rahmaan Janhangeer",
            "seo_description": "How I broke into tech, my open-source contributions, and my path as a Python developer.",
            "page_path": "journey/",
            "og_type": "website",
        }
    )
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "journey"))
    except Exception as e:
        pass
    generate(
        "pages/journey.html",
        join(settings.OUTPUT_FOLDER, "journey", "index.html"),
        **context,
    )


def gen_faceblur():
    context.update(
        {
            "path": "../",
            "seo_title": "FaceBlur Tool | Privacy First Photo Editing",
            "seo_description": "A tool by Abdur-Rahmaan Janhangeer to blur faces in photos for privacy.",
            "page_path": "face-blur/",
            "og_type": "website",
        }
    )
    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "face-blur"))
    except Exception as e:
        pass
    generate(
        "faceblur.html",
        join(settings.OUTPUT_FOLDER, "face-blur", "index.html"),
        **context,
    )


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
    "12": "Dhu al-Hijjah",
}


def gen_islamic_months():
    context.update({"path": "../"})

    months_data = []

    try:
        with open("data/months.json", "r") as f:
            data = json.load(f)

            # Navigate structure: months -> year -> month_num -> date
            if "months" in data:
                for year, year_data in data["months"].items():
                    for month_num, month_info in year_data.items():
                        month_name = ISLAMIC_MONTHS.get(month_num, f"Month {month_num}")

                        date_str = ""
                        src_link = ""

                        if isinstance(month_info, dict):
                            date_str = month_info.get("date", "")
                            src_link = month_info.get("src", "")
                        else:
                            date_str = str(month_info)

                        months_data.append(
                            {
                                "year": year,
                                "month_num": month_num,
                                "month_name": month_name,
                                "date": date_str,
                                "src": src_link,
                            }
                        )

        # Sort by year (desc) then month (desc)
        months_data.sort(key=lambda x: (x["year"], x["month_num"]), reverse=True)

    except Exception as e:
        print(f"Error processing months.json: {e}")
        pass

    islamic_context = context.copy()
    islamic_context.update(
        {
            "months_data": months_data,
            "months_data_json": json.dumps(months_data),
            "years_count": len(data.get("months", {})),
        }
    )

    try:
        os.mkdir(os.path.join(settings.OUTPUT_FOLDER, "islamic-months-mauritius"))
    except Exception as e:
        pass

    generate(
        "islamic-months-mauritius.html",
        join(settings.OUTPUT_FOLDER, "islamic-months-mauritius", "index.html"),
        **islamic_context,
    )


def gen_seo():
    urls = [
        "/",
        "/alfa-podcast/",
        "/books/",
        "/blog/",
        "/articles/",
        "/talks/",
        "/journey/",
        "/face-blur/",
        "/islamic-months-mauritius/",
        "/opensource/",
        "/papers/",
        "/annotated-transformer-commentary/",
    ]

    # Dynamically discover books
    data_books_dir = "./data/books/"
    if os.path.exists(data_books_dir):
        for book_file in os.listdir(data_books_dir):
            if book_file.endswith(".md"):
                slug = book_file.replace(".md", "").replace("_", "-")
                urls.append(f"/books/{slug}/")

    # Dynamically discover diaries
    data_diaries_dir = "./data/diaries/"
    if os.path.exists(data_diaries_dir):
        for diary_file in os.listdir(data_diaries_dir):
            if diary_file.endswith(".toml") and diary_file != "silicon-valley.toml":
                year = diary_file.replace(".toml", "")
                urls.append(f"/diaries/{year}/")
        if os.path.exists(os.path.join(data_diaries_dir, "silicon-valley.toml")):
            urls.append("/diaries/silicon-valley/")

    # Blog posts
    blogs_dir = "./data/blogs/"
    if os.path.exists(blogs_dir):
        for year_str in os.listdir(blogs_dir):
            year_dir = os.path.join(blogs_dir, year_str)
            if not os.path.isdir(year_dir):
                continue
            for fn in os.listdir(year_dir):
                if not fn.endswith(".md"):
                    continue
                name = fn[:-3]
                parts = name.split("_", 1)
                if len(parts) != 2:
                    continue
                slug = parts[1]
                urls.append(f"/blog/{slug}/")

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

    with open(join(settings.OUTPUT_FOLDER, "robots.txt"), "w") as f:
        f.write(robots_content)

    # sitemap.txt
    with open(join(settings.OUTPUT_FOLDER, "sitemap.txt"), "w") as f:
        for url in urls:
            f.write(f"{settings.BASE_URL}{url}\n")

    # sitemap.xml
    sitemap_xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        escaped_url = html.escape(f"{settings.BASE_URL}{url}")
        sitemap_xml.append("  <url>")
        sitemap_xml.append(f"    <loc>{escaped_url}</loc>")
        sitemap_xml.append("  </url>")
    sitemap_xml.append("</urlset>")

    with open(join(settings.OUTPUT_FOLDER, "sitemap.xml"), "w") as f:
        f.write("\n".join(sitemap_xml))


def gen_annotated_commentary():
    context_data = base_context()
    path_prefix = "../"

    commentary_md = "./data/annotated-transformer/commentary.md"
    with open(commentary_md, encoding="utf-8") as f:
        text = f.read()

    content_html, _ = md_to_html_raw(text)

    # Post-process: add CSS classes to blockquotes containing commentary/dive markers
    def add_commentary_class(m):
        label = m.group(1)
        css_class = "commentary" if "Commentary" in label else "deep-dive"
        return f'<blockquote class="{css_class}"><p><span class="commentary-label">{label}</span>'
    content_html = re.sub(
        r'<blockquote>\s*<p>\s*<strong>(Commentary|Deep Dive):</strong>',
        add_commentary_class,
        content_html,
    )

    context_data.update(
        {
            "settings": settings,
            "path": path_prefix,
            "title": "Commentary of The Annotated Transformer",
            "content": content_html,
            "seo_title": "The Annotated Transformer with Commentary | Abdur-Rahmaan Janhangeer",
            "seo_description": "A line-by-line walkthrough of the Transformer architecture from 'Attention is All You Need', with added commentary and explanations.",
            "page_path": "annotated-transformer-commentary/",
            "og_type": "article",
        }
    )

    try:
        os.mkdir(
            os.path.join(settings.OUTPUT_FOLDER, "annotated-transformer-commentary")
        )
    except FileExistsError:
        pass

    generate(
        "annotated_commentary.html",
        join(
            settings.OUTPUT_FOLDER,
            "annotated-transformer-commentary",
            "index.html",
        ),
        **context_data,
    )


def main(args):
    def gen():
        try:
            os.mkdir(join(settings.OUTPUT_FOLDER, "alfa-podcast"))
        except Exception as e:
            pass

        # 1. Generate blog posts and get slugs
        all_blog_posts = gen_blog()

        # 2. Create home page specific context to avoid shadowing/mutation issues
        home_context = context.copy()
        home_context.update(
            {
                "path": "",
                "seo_title": "Abdur-Rahmaan Janhangeer | Python Software Engineer & Author",
                "seo_description": "Software Engineer, Author of SQLite Internals, and Python freelancer specializing in backend systems and open source.",
                "page_path": "",
            }
        )

        # Get latest 5 blog posts for the dedicated homepage section
        blog_posts = []
        for post in all_blog_posts[:5]:
            blog_posts.append(
                {
                    "title": post["title"],
                    "url": f"blog/{post['slug']}/",
                    "num": post["num"],
                }
            )

        home_context.update(
            {
                "blog_posts": blog_posts,
                "writings": settings.writings,  # Restore original technical writings
            }
        )

        # 3. Generate the Home page
        generate(
            "index.html", join(settings.OUTPUT_FOLDER, "index.html"), **home_context
        )

        # 4. Generate other sections
        gen_podcast_rss()
        gen_books()
        gen_diaries()
        gen_writings()
        gen_talks()
        gen_journey()

        generate(
            "podcast.html",
            join(settings.OUTPUT_FOLDER, "alfa-podcast", "index.html"),
            **podcontext,
        )
        gen_faceblur()
        gen_islamic_months()
        gen_opensource()
        gen_papers()
        gen_annotated_commentary()
        gen_seo()

    if len(args) > 1 and args[1] == "--server":
        app = Flask(__name__)

        # remember to use DEBUG mode for templates auto reload
        # https://github.com/lepture/python-livereload/issues/144
        app.debug = True
        server = Server(app.wsgi_app)

        # run a shell command
        # server.watch('.', 'make static')

        # run a function

        server.watch(".", gen, delay=5)
        server.watch("*.py")

        # output stdout into a file
        # server.watch('style.less', shell('lessc style.less', output='style.css'))

        server.serve()
    else:
        print(":::")
        gen()


if __name__ == "__main__":
    main(sys.argv)
