title: Documention is also about documenting internals
---
When talking about documentation, people often refer to the end-user experience. However, when things go wrong internally, the end-users don't have a clue on how to solve it.

It is not only necessary to state the how of things. But the why and rationale also. It's a pleasure to read well-documented code, for sure. But, if you have 100Ks of lines, it's not enough.

There are various techniques to document internals. If ever I am doing it, I'd explain:

- The what and why of the project, including the context
- A conceptual overview of the project
- An internal overview
- Techniques to achieve features
- Codebase layout in brief

Current documentation advice is like people advising on how to write good books. But, you always deal with libraries. Sure, you can start shelf by shelf until you find the book you are looking for and get an overview of the library along the way. But, if you need a particular book, it makes sense to have a catalog so that you know what book exists and a library layout, enabling you to navigate your way to the book. Once you get to the book, of course, you'd relish a well-written book.

Documentation is a time investment you make to save someone else's time. People often say that you should not invest too much in the docs as when changing code, it takes time to re-write the docs and sometimes it slogs you down. True. But, documenting the internals as well as techniques used is not mirrored at the code-line level. It's a high-level explanation to get an idea of how things are achieved. This way you can replace a whole code section if needed.

At the end of the day, it's about enabling users to use the product as if you cannot support them. Imagine launching some people on a planet, for one year, with no outside contact. You'd like to produce documentation that is self-reliant as far as possible. It's about giving more power to your users.
