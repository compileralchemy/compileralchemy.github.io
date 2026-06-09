title: Cinammon - Uber's load shedder
---
Uber released Cinnamon, a load-shedder (Using Century Old Tech to Build a Mean Load Shedder). While a load balancer balances loads across servers, load shedding prioritizes important requests and drops less important ones. Well, a load balancer can have surge queues, but a load shedder has far more appropriate elements. This fits in the concept of graceful degradation, where a system reduces its performance predictably rather than go bust abruptly. 

Uber previously had the QALM framework, but, it had quirks. It required configurations which meant that for the thousands of services, values had to be set, and that too routinely as these get outdated. This means lots of man-hours lost. Also, these values were not optimum often. Cinnamon in contrast requires no configuration, has low latencies, and adjusts load-shedding dynamically. Also, in contrast with QALM, this one has priority propagation, and service priority could be tagged.

Cinnamon is implemented as an RPC middleware, with priorities having 6 tiers (0-5) and a cohort value (0 - 127) where 0 is the highest priority. The component sits behind business logic, dropping requests where needed. Requests pass through a priority checker, rejector, priority queue, scheduler and timeout component with 2 background services: the PID controller (minimize the number of queued requests) and auto-tuner (maximize the throughput of the service, without sacrificing the response latencies much, using a modified TCP Vegas algo).

The century-old tech is the idea of a PID controller, originating as early as the 17th century. They took inspirations from:

- Jaeger: Distributed Tracing at Uber
- WeChat: DAGOR: individual service-level load shedding, acting collaboratively
- Facebook: Fail at Scale: Reliability in the face of rapid change, particularly the Controlled Delay part.
- Netflix: Performance Under Load (adaptive concurrency limits)
- Amazon: Using load shedding to avoid overload (Elements of load-shedding)

Cinnamon is being rapidly adopted due to it's performance but also ease of integration and use.
