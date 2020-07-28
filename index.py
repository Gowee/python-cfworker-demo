async def handleRequest(request):
    visitor_ip = request.headers.js_get('CF-Connecting-IP')
    console.log(visitor_ip)
    r = await fetch("https://api.ip.sb/geoip/" + visitor_ip)
    d = await r.json()
    d['time'] = Date.now()
    return __new__(Response(JSON.stringify(d), {
        'headers' : { 'content-type' : 'text/plain' }
    }))

addEventListener('fetch', (lambda event: event.respondWith(handleRequest(event.request))))
