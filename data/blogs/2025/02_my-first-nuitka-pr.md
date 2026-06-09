title: My first Nuitka PR
---
OSS log: Had a go at contributing to Nuitka after Kevin Rodriguez-Turcios's suggestion. Nuitka converts Py programs into executables, all while applying some performance improvements etc.

Issue 3634 proposes to force launch Nuitka apps via the terminal when double clicking by enabling a flag. It's useful for terminal apps.

I told Kevin i knew nothing about Nuitka and did not have a Mac but he proposed solving it for Linux as it was needed as well.

I spent the first few days reading the docs and submitted an unrelated broken link PR. Since it's a bulky codebase i was confused on where to start. 

Fortunately Kevin PRed the MacOS part and i copied the logic and adapted it for Linux.

I knew C and pointers but not libraries and even less Nuitka. I was checking Linux as !windows and !apple XD but discovered they had if defined(__linux__)

They have an Ai tool that auto-reviews the PRs, pretty picky but helpful and understands the context of the project and draws flow diagrams (Sourcery).

I think it took we one week with some 4 hours of actual coding.

Was interesting to get a good note by the owner.

I also discovered execvp which replaces the process with the new code, maintaining the PID. Without it i was launching another process and waiting it to complete. Also with execvp i can list only the terminal executable name and not provide the full path of the executable.

I think the best way to dive in is to implement something small and learn as you go instead of learning everything before writing a single line. 

Some OpenSource motivation for the week!
