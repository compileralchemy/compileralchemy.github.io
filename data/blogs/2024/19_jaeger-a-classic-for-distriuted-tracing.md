title: Jaeger, a classic for distriuted tracing
---
Jaeger (2017) is a classical tool for distributed tracing invented at Uber but used well outside it. It integrated Dapper-inspired traces (Google, 2010).  It's a Cloud Native Computing Foundation (CNCF) graduate project (2019). Distributed tracing involves following a request and the time taken for each step across services. Jaeger (ˈyā-gər) comes from German for hunter or hunting attendant (Jochen Kirstätter can help us pronounce it maybe). Its crafting comes off as gradual improvements to a Zipkin-like clone, which is another distributed tracing tool.

Distributed tracing works like this. Let's say we are recording a transaction. The whole recording of it involves several services.  

- Service 1: Check for fraud
- Service 2: Record in database
- Service 3: Effect payment

A transaction involves passing the data through the 3 services. 

Jaeger will record the time taken for each step as well as the return status. But, of course, if we record every single request path step, we will record a lot of data, most probably more than the system is generating. For this, a nice strategy is to sample the traffic, which it does. A span represents a logical unit of work in Jaeger that has an operation name, the start time of the operation, and the duration. A trace consists of spans.

Jaeger's predecessor is Merckx, which worked great for a monolith. It stored tracing data as blocks, and users could query the data. It also shipped with a UI for visualizations. It traced calls to other services, databases, and Redis queries but could not go one level deeper, lacking distributed context propagation. Also, data was stored in global states.

Uber began developing a network multiplexing and framing protocol for RPC called Tchannel. Tracing was specified in the protocol. Since they did not know tracing well then, they integrated with Zipkin. They had tchannel clients sending data to a collector which sent data to a Riak/Solr backend and they used Zipkin for UI and query. Since the backend experienced scaling problems, they switched to Cassandra, a db they had experience with. Clients implemented the OpenTracing API from the start.

Zipkin was good but lacked good instrumentation outside of Java/Scala and had a fixed strategy. Jaeger implemented a responsive sampling strategy. By now it had its own query service and UI, with the first versions still using tchannel. Later on, reporting was done via UDP. 

Jaeger at first had its own set of client libraries for instrumentation but now these have been deprecated and OpenTelemetry libraries are recommended instead.

The all-in-one version includes jaeger-collector, jaeger-query, and jaeger-agent.
