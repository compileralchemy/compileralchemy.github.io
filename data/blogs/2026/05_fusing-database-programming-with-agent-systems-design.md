title: Fusing Database Programming With Agent Systems Design
---
What happens when you fuse database engineering with agent systems programming? You stop thinking in terms of processes and start thinking in terms of state that survives anywhere. That's where some genuinely powerful ideas start to emerge.

Pekka Enberg lays this out clearly. A filesystem that does not depend on the OS is a massive win. Stateful agents that can be stopped, resumed, and continued from anywhere are even bigger. Once you see that, the old assumptions around agents and files start to feel outdated.

LLMs are actually quite good at file operations, but files are not universally available. Browsers don't have them. Serverless environments don't really have them. Agents get paused and resumed all the time. What you really want is a durable log of actions and state in a single place, both for debugging and for restarting agents from the exact point they stopped.

This is where AgentFS gets interesting. To understand it, it helps to understand Turso. AgentFS provides a filesystem that lives inside a SQLite file. Agents store their state and data directly in that SQLite database. Turso then takes that SQLite file, along with any associated files, and stores them in the cloud. The result is a single source of truth that can be synced across machines.

The implication is big: agents can store and retrieve data from almost anywhere, including the browser. No OS-level filesystem assumptions. No fragile workarounds. Just state that moves with the agent.

It's also worth noting that Turso's improved cloud backend was originally built to store Kubernetes state. That's not a toy problem. It's battle-tested infrastructure applied to a new domain.

There are limitations today, like handling very large files and checkpointing, but the direction is what matters. On top of that, AgentFS ships SDKs in multiple languages, including Python! https://penberg.org/blog/disaggregated-agentfs.html
