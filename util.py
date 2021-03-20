import logging as log


def get_log(file):
    logger = log.getLogger()
    logger.setLevel('INFO')
    basic_format = "[%(asctime)s %(levelname)s] %(message)s"
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = log.Formatter(basic_format, date_format)
    chlr = log.StreamHandler()
    chlr.setFormatter(formatter)
    chlr.setLevel('INFO')
    fhlr = log.FileHandler(file)
    fhlr.setFormatter(formatter)
    logger.addHandler(chlr)
    logger.addHandler(fhlr)
    return logger
