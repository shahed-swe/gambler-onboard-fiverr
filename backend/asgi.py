import os
import django

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django.setup()
django_asgi_app = get_asgi_application()


# start the rest of app setup after this line
from channels.routing import ProtocolTypeRouter


class CustomProtocolTypeRouter(ProtocolTypeRouter):
    async def __call__(self, scope, receive, send, *args):
        if scope['type'] in self.application_mapping:
            handler_obj = self.application_mapping[scope['type']](scope, receive, send)
            if args:
                return handler_obj(receive, send)
            return handler_obj
        raise ValueError("No application configured for scope type %r" % scope['type'])


application = ProtocolTypeRouter({
    'http': django_asgi_app,
})

print('HTTP & WebSocket protocol router is running')
