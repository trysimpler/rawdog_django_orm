import time
from starlette.types import ASGIApp, Receive, Scope, Send
from django.db import connections
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

class OptOutOfRandomConnectionCrashFastapiMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, *args, **kwargs) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # Pre-processing
        response = await call_next(request)  
        app = request.app
        if not hasattr(app.state, "last_pruned"):
            app.state.last_pruned = 0
            
        if app.state.last_pruned + 5 < time.time():
            start = time.time()
            app.state.last_pruned = start
            for conn in connections.all():
                conn.close_if_unusable_or_obsolete()
            print(f"Pruned all connections. Took {round((time.time() - start) * 1000, 1)} miliseconds")
        

        # Post-processing
        return response