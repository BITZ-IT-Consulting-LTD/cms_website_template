import time
import logging

logger = logging.getLogger(__name__)

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        logger.info(f"Request start: {request.method} {request.path}")

        response = self.get_response(request)

        duration = time.time() - start_time
        logger.info(f"Request end: {request.method} {request.path} ({duration:.2f}s)")

        return response
