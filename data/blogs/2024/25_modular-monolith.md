title: Modular monolith
---
Modular monolith, an incredible twist in architecture. I was pleasantly surprised to encounter this term and view its applications. A monolith has been traditionally viewed as being unmaintainable with difficulties for teams managing features.

A monolith centralizes features and reduces the whole codebase into one unit. Features are all together and teams work across the codebase as they have to touch everywhere to implement features. Running the whole codebase runs every feature.

People have been thinking of isolating features and abstracting them into their own services for better organization and redundancy. But, they soon presented their own challenges, including complexity. Blindly migrating to microservices was a "mistake" apparently.

Google now offers serviceweaver, which is a modular monolith framework. \"The main advantage of components is that they decouple how you write your code from how you run your code. They let you write your application as a monolith, but when you go to run your code, you can run components in a separate process or on a different machine entirely.\" 

As to whether turning to monolith is a wrong turn, serviceweaver answers: \"
Service Weaver is trying to encourage a modular monolith model, where the application is written as a single modularized binary that runs as separate microservices. This is different from the monolith model, where the binary runs as a single (replicated) service.

We believe that the Service Weaver's modular monolith model has the best of both worlds: the ease of development of monolithic applications, with the runtime benefits of microservices.\"

Nice paper Ruoyu Su and Xiaozhou Li, but reference [1] seems super vague to me. Nothing specific to see where you concluded that.
