title: Multi-layer cache at DoorDash
---
DoorDash implemented a multi-layered cache to homogenize caching across all services (How DoorDash Standardized and Improved Microservices Caching). Caching has its twists which teams have to solve when each one implements their own. Oftentimes they all face similar challenges. 

Doordash teams most commonly use 
- Caffeine, a high-performance in-memory Java library (for local caching)
- Lettuce, an advanced Java Redis client for thread-safe sync, async, and reactive usage (for distributed caching)
- HashMaps
But, as these were not caches as such and each team had to write caches from scratch, caching problems like staleness appeared, and each team chose their own key schemes, which also made observability less accessible.

They tested the new cache on the DashPass backend, which was also experiencing spikes. When it was successfully tested, they deployed it everywhere. They set up a single code interface CacheManager, with a suspend function withCache to standardize caching APIs. With a multi-layer cache, if a key is not found in the first layer, it is searched until the source of truth (SoT) is reached. Once this is done, the key is inserted in the first layers to reduce the need to reach the SoT.

They implemented 3 layers:
- Request local Cache: Uses HashMap, for the lifetime of the request 
- Local Cache: Uses a cache made of Caffeine, accessible within a JVM
- Redis Cache: Uses Lettuce and accessible to all pods sharing the same Redis cluster
The suspend function (withCache) is the intermediary between databases and services and the layers (suspend -> Redis -> local -> request local).

Runtime control was also introduced to switch off layers, useful in the case of a bug for example and to enable cache shadowing at a particular percentage. Since all caching uses a single interface, metrics are built in to measure cache hits and generate logs on misses. Using a shadowing mechanism, fresh cache entries are also compared with the SoT. Staleness is measured by the latency between cache updated and cache entry creation, critical for evaluating invalidation strategies.

Codewise, each cache key has 3 components (abstract class CacheKey with 3 components):
- unique cache name
- key type (to categorise keys) and key type id
- configuration (as CacheKeyConfig)

A key is referenced by cache_name->cache_key->cache_key_id, across all services.
