/* ════════════════════════════════════════════════════════════════
   S.C.I — Service Worker para Notificações Nativas do Sistema
   ════════════════════════════════════════════════════════════════ */

const CACHE_NAME = 'sci-sw-v1';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

/* Recebe mensagens da aplicação e exibe notificações mesmo com a aba em segundo plano */
self.addEventListener('message', (event) => {
  if (!event.data) return;
  const { type, title, options } = event.data;
  if (type === 'SHOW_NOTIFICATION') {
    self.registration.showNotification(title || 'S.C.I — Saúde Coletiva Inteligente', {
      body: options?.body || '',
      icon: options?.icon || 'logo.png',
      badge: options?.badge || 'logo.png',
      vibrate: options?.vibrate || [100, 50, 100],
      data: options?.data || { url: './' },
      tag: options?.tag || 'sci-push',
      renotify: true,
      actions: options?.actions || [
        { action: 'open', title: 'Abrir App' }
      ]
    });
  }
});

/* Clique na notificação do sistema abre ou foca o aplicativo */
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const targetUrl = event.notification?.data?.url || './';

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if ('focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(targetUrl);
      }
    })
  );
});
