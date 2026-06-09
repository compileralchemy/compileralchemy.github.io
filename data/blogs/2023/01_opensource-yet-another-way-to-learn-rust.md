title: OpenSource: Yet another way to learn Rust
---
I read the [Rust book](https://doc.rust-lang.org/book/) twice. Also [Comprehensive Rust](https://google.github.io/comprehensive-rust/) from Google. Things did not click as i forgot ownership fast when digesting other topics. The Rust book has a lot of concepts to cover. I lost a lot of time starting again. I really wanted to get my feet wet and started programming on some playgrounds as well as trying some [Maturin](https://www.maturin.rs/) examples.



Playgrounds are fine. Until you try to code something on your machine. I thought rustc was how you built things / run scripts. I tried cargo finally and everything worked like a charm. At this point i decided to code something fun which would have the right balance between motivation and fun. It should also ideally have some stuffs i can do, so that i can focus on upskilling in Rust rather than figuring out what to try out next.

I decided to port Python's library called [rich](https://github.com/Textualize/rich) over in a crate called [richterm](https://crates.io/crates/richterm). Since it's a port, i had a syllabus to cover, a lot of todos to tackle already. This in itself carved a path where i learnt Rust progressively. It was like learning Rust by tackling challenges meaningfully.

In the beginning i used only functions. I wanted the [print function](https://github.com/Abdur-rahmaanJ/richterm/blob/d26e7a9395571fcb846a5f48ecff2d6b8dc9e2e0/src/lib.rs#L10) to support both arrays and vectors. This introduced me to rust generics. I also got a gentle introduction to &str and String. Then i saw the need for classes, i explored struct. To hold data, i explored hashmap. Then attempting threads for [spinners](https://github.com/Abdur-rahmaanJ/richterm/blob/stable/src/spinners.rs). I even have the luxury to pause and continue working when i like, for example while coding the panel feature by saving it as a [pull request](https://github.com/Abdur-rahmaanJ/richterm/pull/16). I also got people [helping out](https://github.com/Abdur-rahmaanJ/richterm/pull/18).

Ah, i also got used to defining modules and adding a crate and use it. I discovered [crates.io](https://crates.io) and how to add projects to use.

I could not have asked for a better way to learn Rust. The community is willing to teach. Building an OpenSource product introduces you to some good practices. I'd say think of a nice-to-have thing and give it a try. I even learnt about `cargo fmt` while [contributing to libSQL](https://github.com/libsql/sqld/pull/551).

I'd say this way is far more lively, real and entertaining! 
I am not a Rust expert but it motivates me to keep pursuing my Rust journey.
