title: How marketing shapes Rust development
---
Rust always felt hypy. For the simple reason that if you try it, it leaves an unsavoury aftertaste which comes as a surprise not tallied with marketing. It's like a super-energy food which just has a bad mix of ingredients. Here we have the person who oversaw the introduction of async/await into the language. In a beautiful piece about Async Rust, he explains how marketing shapes features in Rustland.

"In early 2018, the Rust project had committed to the idea of releasing a new “edition” that year, to fix some of the syntactic issues that had emerged with 1.0. It was also decided to use this edition as an opportunity to promote a narrative around Rust being ready for prime-time; the Mozilla team was mostly compiler hackers and type theorists, but we had some basic idea about marketing and recognized the edition as an opportunity to get eyeballs on the product. I proposed to Aaron Turon that we should focus on four basic user stories which seemed like growth opportunities for Rust. These were:

- Embedded systems
- WebAssembly
- Command-line interfaces
- Network services

This remark was the jumping off point for the creation of the “Domain Working Groups”, which were intended to be cross-functional groups focused on a particular use “domains” (in contrast to the pre-existing “teams” controlling some technical or organizational bailiwick). The concept of working groups in the Rust project has morphed since then and mostly lost this sense, but I digress.
The work on async/await was pioneered by the “network services” working group, which eventually become known as simply the async working group (and still exists under this name today). However, we were also acutely aware that given its lack of runtime dependencies, async Rust could also be of great service in the other domains, especially embedded systems. We designed the feature with both of these use cases in mind.

It was clear, though usually left unsaid, that what Rust needed to succeed was industry adoption, so that it could continue to receive support once Mozilla stopped being willing to fund an experimental new language. And it was clear that the most likely path to short-term industry adoption was in network services, especially those with a performance profile that compelled them at the time to be written in C/C++. This use case fit the niche of Rust perfectly - these systems need high degrees of control to achieve their performance requirements but avoiding exploitable memory bugs is critical because they are exposed to the network."

-- withoutboats, https://lnkd.in/dEbNU26F

The pressing need for industry adoption might explain the entire culture around the Rust userbase.
