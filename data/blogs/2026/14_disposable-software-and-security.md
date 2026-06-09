title: Disposable Software And Security
---
Sylvain Martinez wrote a piece about security. I appreciated one point: With the rise of disposable software, writing your own software might be safer as attackers don't know beforehand what vulnerabilities you have. Whereas if you use widely known software, attackers have a list to choose from.

Unless of course the custom software is using existing libraries, but then, they have to know that you are using the library. We can code custom software and audit them for security issues and ensure we don't have issues. But realistically, it is virtually impossible to create custom software without existing libs.

Let's say we want to write something from scratch, we'd have to start from writing bootloader software, the OS, the app layer, the language, then the app, which is possible but not realistic. Let's say we are writing our own web server. What if there is a vulnerability in our programming language itself? So even when we say writing software from scratch, we are still using existing software somewhere. And, it is easier to fix / audit existing software for vulnerabilities.

As the article points out, we must assume that the attacker has an Ai in the loop. The fix is to, i guess:

1. Use well know software
2. But, always keep them updated 
3. If the library is unmaintained, search for an alternative 
4. If the library is small enough and we cannot find other options, we can fork and maintain it internally. As companies already do.

Security is the same as before, just, it evolves at a faster pace and makes the discovery of vulnerabilities easier.
