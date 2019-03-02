import os
import logging.handlers

def register_logging(app):
    if app.debug or app.testing:
        return

    # Set info level on logger, which might be overwritten by handlers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(os.getenv("LOG_FOLDER"), 'info.log')
    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)