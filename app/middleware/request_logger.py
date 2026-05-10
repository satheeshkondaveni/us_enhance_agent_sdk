from app.loggins.logger import get_logger

log = get_logger()

class RequestLoggerMiddleware:
    @staticmethod
    def log_request(input_json):
        log.info(f"Incoming request: {input_json}")

    @staticmethod
    def log_response(output_json):
        log.info(f"Outgoing response: {output_json}")
