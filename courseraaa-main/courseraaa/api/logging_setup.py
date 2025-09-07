import logging

def setup_logging():
    logging.basicConfig(filename='api_logs.log',
                        level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    return logging.getLogger()
