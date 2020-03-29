
def add_logger(app):
    if app.debug is not True:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('errors.log', maxBytes=1024 * 1024 * 100, backupCount=20)
        file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)