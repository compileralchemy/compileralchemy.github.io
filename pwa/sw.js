/* Mauritius speed camera map - service worker */
const CACHE = 'mauritius-map-v2';
const ASSETS = ['./', './index.html', './manifest.webmanifest'];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  const isTile = url.hostname === 'tile.openstreetmap.org';
  const sameOrigin = url.origin === self.location.origin;
  e.respondWith(
    fetch(e.request)
      .then((res) => {
        /* cache: own files, CORS libs, OSM tiles (opaque) - tiles = offline map */
        const ownOk = res && res.status === 200 && (sameOrigin || res.type === 'basic' || res.type === 'cors');
        const tileOk = res && isTile && (res.type === 'opaque' || res.status === 200);
        if (ownOk || tileOk) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(e.request, copy));
        }
        return res;
      })
      .catch(() => caches.match(e.request).then((m) => m || caches.match('./index.html')))
  );
});
