const CACHE_NAME = "gongkao-idiom-pwa-v18";
const ASSETS = [
  "./",
  "./index.html",
  "./manifest.json?v=18",
  "./apple-touch-icon.png?v=18",
  "./icon-192.png?v=18",
  "./icon-512.png?v=18",
  "./icon-maskable-512.png?v=18",
  "https://cdn.tailwindcss.com/3.4.17"
];

self.addEventListener("install", (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)).catch(() => {})
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const isNav = event.request.mode === "navigate";
  const netFetch = isNav
    ? fetch(event.request.url, { cache: "no-cache" })
    : fetch(event.request);
  event.respondWith(
    netFetch
      .then((resp) => {
        if (resp && resp.status === 200) {
          const clone = resp.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return resp;
      })
      .catch(() => caches.match(event.request).then((cached) => cached || caches.match("./index.html")))
  );
});
