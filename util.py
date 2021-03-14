import logging as log

def get_log(file):
    logger = log.getLogger()
    logger.setLevel('INFO')
    BASIC_FORMAT = "[%(asctime)s %(levelname)s] %(message)s"
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    formatter = log.Formatter(BASIC_FORMAT, DATE_FORMAT)
    chlr = log.StreamHandler() # 输出到控制台的handler
    chlr.setFormatter(formatter)
    chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
    fhlr = log.FileHandler(file) # 输出到文件的handler
    fhlr.setFormatter(formatter)
    logger.addHandler(chlr)
    logger.addHandler(fhlr)
    return logger