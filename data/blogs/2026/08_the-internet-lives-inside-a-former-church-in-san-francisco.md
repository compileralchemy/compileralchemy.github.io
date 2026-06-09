title: The Internet Lives Inside A Former Church In San Francisco
---
The internet lives inside a former church in San Francisco. I dug into how the Internet Archive actually operates and it is a masterclass in building something massive without burning money.

The first lesson is cost discipline at extreme scale. The Internet Archive stores more than 200 petabytes of data with 99 petabytes being unique. This was not built by chasing hype. The founder came from Thinking Machines a company that built supercomputers decades ago and that engineering mindset shaped every decision. An ex-OpenAi member also built Thinking Machines (lab), not to be confused..

Their storage philosophy is aggressively practical. They use consumer grade hardware instead of expensive enterprise systems. Just a Bunch of Disks (JBOD as they call it). Across three generations their Petabox grew from 100 terabytes to 1.4 petabytes while power usage stayed around 6 to 8 kilowatts. Scaling like that only happens when efficiency is designed in from day one.

They cut costs in places most teams ignore. Cooling comes from outside air. In winter the hardware runs slightly hotter so it helps heat the building. Because data is mirrored failed disks are not replaced immediately. They wait because redundancy buys time and time saves money.

Web crawling evolved as the web evolved. They moved from Heritrix which handled mostly static content to Brozzler which runs a headless Chrome to execute JavaScript. They switch between the two depending on what needs to be captured. Crawls are stored in WARC files built specifically for long term web archiving.

Then come the legal realities. Digital lending triggered lawsuits from major publishing houses and the experiment weakly survived. Preserving information and owning information are very different things.

The Internet Archive is the only official memory of the internet, a bit scary! I am already thinking of a new feature for Linkversity.
