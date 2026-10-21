// Saludly · service worker de la PWA.
// Solo guarda la app (HTML, JS, CSS, imágenes propias) para que abra rápido y sin señal.
// Nunca guarda datos de salud: las llamadas a Supabase y a otros dominios siempre van a la red.
const CACHE = "saludly-app-v1";

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(["/", "/manifest.webmanifest", "/iconos/icono-192.png"])));
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k)))));
  self.clients.claim();
});

self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET" || url.origin !== self.location.origin) return;
  if (e.request.mode === "navigate") {
    // Páginas: primero la red; sin señal, la app guardada.
    e.respondWith(fetch(e.request).catch(() => caches.match("/")));
    return;
  }
  // Archivos de la app: primero lo guardado; si no está, la red y se guarda.
  e.respondWith(
    caches.match(e.request).then(
      (r) =>
        r ||
        fetch(e.request).then((res) => {
          if (res.ok) {
            const copia = res.clone();
            void caches.open(CACHE).then((c) => c.put(e.request, copia));
          }
          return res;
        }),
    ),
  );
});
