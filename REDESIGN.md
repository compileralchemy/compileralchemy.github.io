# Website Redesign Specification

## Executive Summary

Transform compileralchemy.com from a generic blog/portfolio into a **high-conversion, authority-building engineering site** that clearly communicates: "I build production systems, hire me."

---

## 1. Page Structure & Hierarchy

### New Section Order (Top to Bottom)

1. **Hero Section** - Value proposition + CTAs
2. **Authority/Trust Bar** - Numbers + credibility markers
3. **Selected Projects** - Production evidence (top 4-6)
4. **How I Think** - Differentiator section
5. **Writing** - Engineering notes (curated, not chronological)
6. **Book** - SQLite Internals (prominent)
7. **Testimonials** - Social proof (curated top 3)
8. **Contact** - Final CTA

---

## 2. Hero Section

### Headline Options

**Primary (Recommended):**
```
I build systems that don't break in production.
```

**Alternative:**
```
From data pipelines to deployed AI systems.
Engineering real-world systems, not demos.
```

### Subtext
```
Python | Systems | ML & NLP | Backend & Infrastructure
Independent developer based in Mauritius. Building open source since 2016.
```

### CTAs
- **Primary:** "View Projects" → scrolls to projects section
- **Secondary:** "Hire Me" → mailto:arj.python@gmail.com
- **Tertiary:** GitHub | Writing | Contact

### Background Animation
Subtle animated gradient mesh or flowing data streams (SVG). NOT particle noise. Use CSS-only for performance.

---

## 3. Authority/Trust Bar

Replace "Facts" section. Make it scannable cards:

| Card 1 | Card 2 | Card 3 | Card 4 |
|--------|--------|--------|--------|
| **25+** | **330k+** | **2** | **100+** |
| Open Source | PyPI Downloads | HN Front Page | Community Members |
| Projects | downloads | hits | helped into OSS |

Also include:
- "Author of the first free & open book on SQLite Internals"
- "Speaker at EuroPython, PyCon Sweden, PyCon South Africa, DevCon MU"
- "Organiser: PyMUG, FlaskCon, FlaskCWG"

---

## 4. Projects Section (Critical)

**NOT a table. Use project cards.**

### Card Structure

```
┌─────────────────────────────────────┐
│ [Project Logo]                      │
│                                     │
│ SHOPYO                              │
│ ─────────                           │
│ Problem: Needed modular Flask apps  │
│           without Django overhead   │
│                                     │
│ Approach: Self-contained modules,   │
│           Django-like CLI commands  │
│                                     │
│ Stack: Flask, SQLAlchemy, PostgreSQL│
│                                     │
│ Outcome: 2.5k+ stars, 100+ contrib, │
│          featured in Python Weekly  │
│                                     │
│ [GitHub] [Docs] [PyPI]              │
└─────────────────────────────────────┘
```

### Featured Projects (Top 6)

1. **Shopyo** - Flask framework (2.5k stars)
2. **Honeybot** - IRC bot (1k+ stars)
3. **Hooman** - PyGame wrapper
4. **Jamstack** - Static site generator (powers this site)
5. **GatewayD** - Database gateway (recent work)
6. **angel-recall** - Memory OS for agents

### Hover Behavior
- Subtle lift + shadow increase
- Border color shift to accent
- "View Details" appears

---

## 5. "How I Think" Section (Differentiator)

**This is your edge over other portfolios.**

### Content (Punchy, Opinionated)

```
┌──────────────────────────────────────────┐
│ HOW I THINK                               │
├──────────────────────────────────────────┤
│                                          │
│ Toy ML vs Production ML                  │
│ ─────────────────────────                │
│ 90% of ML projects die in production.    │
│ I build systems that survive the real    │
│ world: monitoring, retries, fallbacks.   │
│                                          │
│ ───────────────────────────────────────── │
│                                          │
│ Docs > Hype                              │
│ ──────────────                           │
│ The best code is useless without clear   │
│ docs. I prioritize readability over      │
│ cleverness every time.                   │
│                                          │
│ ───────────────────────────────────────── │
│                                          │
│ Automation Over Repetition                │
│ ───────────────────────────              │
│ If I do something twice, I automate it. │
│ Scripts, CLIs, templates—built for       │
│ speed, not vanity.                      │
│                                          │
└──────────────────────────────────────────┘
```

### Style
- Dark card background
- Accent color left border for each point
- Minimal, clean typography

---

## 6. Writing/Articles Section

**Reposition as "Engineering Notes from Real Systems"**

### Curated (NOT chronological) - Top 5:

1. "Ruff: Internals of a Rust-backed Python linter-formatter" (featured in PyCoder's Weekly)
2. "libSQL: Diving Into a Database Engineering Epic"
3. "Kubernetes Internals: Inside The Mind of A Monster"
4. "Scuba: Diving Into Facebook's Event Analysis System"
5. "The State of NLP in Production" (your talk, repurpose as article)

### Layout
- Card grid (3 columns on desktop, 1 on mobile)
- Each card shows: Title, 2-line excerpt, "Read →" link
- Add subtle hover effect (lift + shadow)

### Link to full archive at bottom: "View all articles →"

---

## 7. Book Section

**High authority placement - immediately after Writing**

```
┌─────────────────────────────────────────────────────┐
│  SQLite INTERNALS                                    │
│  How The World's Most Used Database Works            │
│                                                     │
│  [BOOK COVER - generate placeholder]                │
│                                                     │
│  The first free & open book on SQLite internals.   │
│  Dive into B-Trees, page allocation, query          │
│  optimization, and the magic that powers            │
│  billions of devices worldwide.                     │
│                                                     │
│  [Read Online] [Download PDF] [GitHub]              │
└─────────────────────────────────────────────────────┘
```

### Styling
- Large, prominent card
- Book cover placeholder (design needed)
- Accent color matching "engineering" aesthetic

---

## 8. Testimonials Section

**Select only the strongest 3:**

1. **James Luo** - Software Engineer, Facebook
   > "He was able to lead our team in terms of having a proper system design to documentation. He was able to make the engineering team more productive."

2. **Shamsuddin Rehmani** - Software Development Engineer, Amazon
   > "As my first open source contribution, I couldn't have asked for a better mentor... His attention to details, clear guidance, pursuit of best industry practices makes him a great leader."

3. **Donald Knuth** - Programming Legend
   > Personal correspondence (include LinkedIn source link)

### Layout
- Horizontal scroll or 3-column grid
- Quote styling with large quotation marks
- Name + Title + optional company logo

---

## 9. Contact/Final CTA

```
┌─────────────────────────────────────────┐
│ HAVE SOMETHING COMPLEX TO BUILD?        │
│                                         │
│ I build production systems that scale. │
│ Let's talk about your project.          │
│                                         │
│ arj.python@gmail.com                    │
│                                         │
│ [GitHub] [LinkedIn] [Twitter]          │
└─────────────────────────────────────────┘
```

### Style
- Centered, large typography
- Dark background
- Subtle animation on "Let's talk" text

---

## 10. Visual Design System

### Color Palette

| Role | Color | Hex |
|------|-------|-----|
| Background (Dark) | Near Black | #0a0a0b |
| Background (Light) | Off White | #fafafa |
| Surface (Dark) | Dark Gray | #141416 |
| Surface (Light) | White | #ffffff |
| Primary Accent | Electric Blue | #3b82f6 |
| Secondary Accent | Emerald | #10b981 |
| Text Primary (Dark) | White | #ffffff |
| Text Primary (Light) | Near Black | #111827 |
| Text Secondary | Gray | #6b7280 |
| Border | Subtle Gray | #27272a |

### Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Headings | Inter | 700 | 48px/36px/24px |
| Body | Inter | 400 | 16px |
| Code | JetBrains Mono | 400 | 14px |
| Accent Text | Space Mono | 400 | 14px |

### Spacing System

- Base unit: 4px
- Section padding: 96px vertical, 24px horizontal
- Card padding: 24px
- Grid gap: 24px

### Border Radius

- Cards: 12px
- Buttons: 8px
- Tags: 4px

---

## 11. Animations & Interactions

### Page Load
- Staggered fade-in for sections (animation-delay: 0.1s, 0.2s, etc.)
- Hero text slides up from 20px below

### Scroll Animations
- Elements fade in + slide up when entering viewport
- Use Intersection Observer or a library

### Micro-interactions
- Buttons: scale(1.02) on hover, background color shift
- Links: animated underline (width expand from center)
- Cards: translateY(-4px) + shadow increase on hover
- Project cards: border-left accent color slides in on hover

### Background Animation (Hero)
- CSS gradient mesh with slow animation (30s loop)
- OR subtle grid lines with perspective

---

## 12. Responsive Breakpoints

| Breakpoint | Width | Changes |
|------------|-------|---------|
| Mobile | < 640px | 1 column, stacked sections |
| Tablet | 640-1024px | 2 columns where applicable |
| Desktop | > 1024px | Full layout, max-width 1200px |

---

## 13. Tech Stack Recommendation

**Option A: Modern (Recommended)**
- **Framework:** Astro (fast, static-first) or Next.js
- **Styling:** Tailwind CSS
- **Content:** MDX for blog/writing
- **Animation:** Framer Motion (minimal use)
- **Deployment:** Vercel or Cloudflare Pages

**Option B: Keep Existing (Jinja)**
- Upgrade from Bulma to custom CSS/Tailwind
- Keep Jinja templates but refactor sections
- Improve typography and spacing

---

## 14. Implementation Priority

| Phase | Task | Priority |
|-------|------|----------|
| 1 | Hero section redesign | P0 |
| 2 | Authority bar | P0 |
| 3 | Projects as cards | P0 |
| 4 | "How I Think" section | P1 |
| 5 | Writing curation | P1 |
| 6 | Book section prominent | P1 |
| 7 | Testimonials (top 3) | P2 |
| 8 | Contact CTA | P2 |
| 9 | Animations | P2 |
| 10 | Mobile responsive | P2 |

---

## 15. Remove From Current Site

- ❌ Cluttered blog-first layout
- ❌ Weak hero with no clear value prop
- ❌ "About me" generic content
- ❌ Projects as table
- ❌ Testimonial carousel (upgrade to grid)
- ❌ "In The News" Twitter embed (too cluttered)
- ❌ Navigation menu overload
- ❌ Emoji icons (upgrade to clean icons)
- ❌ Multiple background colors per section

---

## 16. Component Snippets

### Hero Section (Tailwind-like classes)

```html
<section class="min-h-screen bg-[#0a0a0b] flex items-center justify-center relative overflow-hidden">
  <!-- Animated background -->
  <div class="absolute inset-0 bg-gradient-to-br from-[#0a0a0b] via-[#141416] to-[#0a0a0b] animate-pulse"></div>
  
  <div class="relative z-10 max-w-4xl mx-auto px-6 text-center">
    <h1 class="text-5xl md:text-7xl font-bold text-white mb-6 tracking-tight">
      I build systems that<br/><span class="text-[#3b82f6]">don't break in production.</span>
    </h1>
    <p class="text-xl text-[#6b7280] mb-10 max-w-2xl mx-auto">
      Python • Systems • ML & NLP • Backend & Infrastructure<br/>
      Independent developer. Building open source since 2016.
    </p>
    <div class="flex gap-4 justify-center">
      <a href="#projects" class="px-8 py-4 bg-[#3b82f6] text-white rounded-lg font-semibold hover:bg-[#2563eb] transition-all">
        View Projects
      </a>
      <a href="mailto:arj.python@gmail.com" class="px-8 py-4 border border-[#27272a] text-white rounded-lg font-semibold hover:border-[#3b82f6] transition-all">
        Hire Me
      </a>
    </div>
  </div>
</section>
```

### Project Card

```html
<div class="bg-[#141416] border border-[#27272a] rounded-xl p-6 hover:border-[#3b82f6] hover:-translate-y-1 transition-all duration-300">
  <div class="flex items-center gap-4 mb-4">
    <div class="w-12 h-12 bg-[#1f1f23] rounded-lg flex items-center justify-center">
      <span class="text-2xl">⚡</span>
    </div>
    <div>
      <h3 class="text-xl font-bold text-white">Shopyo</h3>
      <span class="text-sm text-[#6b7280]">Flask Framework</span>
    </div>
  </div>
  <p class="text-[#9ca3af] mb-4">Problem: Needed modular Flask apps without Django overhead.</p>
  <div class="flex gap-2 mb-4">
    <span class="px-3 py-1 bg-[#1f1f23] text-[#3b82f6] text-xs rounded">Flask</span>
    <span class="px-3 py-1 bg-[#1f1f23] text-[#10b981] text-xs rounded">SQLAlchemy</span>
  </div>
  <div class="text-sm text-[#6b7280]">2.5k stars • 100+ contributors • Featured in Python Weekly</div>
</div>
```

### Authority Bar

```html
<section class="py-16 bg-[#0a0a0b] border-t border-b border-[#27272a]">
  <div class="max-w-6xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8">
    <div class="text-center">
      <div class="text-4xl font-bold text-white mb-2">25+</div>
      <div class="text-[#6b7280]">Open Source Projects</div>
    </div>
    <div class="text-center">
      <div class="text-4xl font-bold text-white mb-2">330k+</div>
      <div class="text-[#6b7280]">PyPI Downloads</div>
    </div>
    <div class="text-center">
      <div class="text-4xl font-bold text-white mb-2">2</div>
      <div class="text-[#6b7280]">Hacker News Front Page</div>
    </div>
    <div class="text-center">
      <div class="text-4xl font-bold text-white mb-2">100+</div>
      <div class="text-[#6b7280]">Community Members Helped</div>
    </div>
  </div>
</section>
```

---

## 17. Content Copy Ready to Use

### Hero Headline
```
I build systems that don't break in production.
```

### Hero Subtext
```
Python | Systems | ML & NLP | Backend & Infrastructure
Independent developer based in Mauritius. Building open source since 2016.
```

### Authority Tagline
```
Author of the first free & open book on SQLite Internals
Speaker at EuroPython, PyCon Sweden, PyCon South Africa, DevCon MU
Organiser: PyMUG, FlaskCon, FlaskCWG
```

### "How I Think" Content Points

**Point 1:**
- Title: Toy ML vs Production ML
- Content: "90% of ML projects die in production. I build systems that survive the real world: monitoring, retries, fallbacks."

**Point 2:**
- Title: Docs > Hype
- Content: "The best code is useless without clear docs. I prioritize readability over cleverness every time."

**Point 3:**
- Title: Automation Over Repetition
- Content: "If I do something twice, I automate it. Scripts, CLIs, templates—built for speed, not vanity."

### Contact CTA
```
Have something complex to build?
I build production systems that scale. Let's talk.
arj.python@gmail.com
```

---

## 18. Summary

This redesign transforms compileralchemy.com from a generic personal site into an **authority-building engineering portfolio** that:

✓ Immediately answers "Why hire me?" in the hero
✓ Shows concrete numbers (25+ projects, 330k+ downloads)
✓ Presents projects as production evidence, not cool demos
✓ Differentiates with "How I Think" section
✓ Curates writing as engineering notes, not tutorials
✓ Features the SQLite Internals book prominently
✓ Uses social proof from top engineers (Facebook, Amazon)
✓ Has a clear, confident contact CTA

**Result:** Visitors think "This person builds serious systems" and "I want them on my team."

---

*Next steps: Choose tech stack (Astro/Next.js vs keep Jinja), then implement section by section.*