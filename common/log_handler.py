import logging
from logging.handlers import TimedRotatingFileHandler
import settings
from common.config_loader import ConfigLoader
import os


# 指定只有在特定类型的异常（如 AssertionError）出现时，才进行重试
def retry_if_failure(exception):
    return isinstance(exception, AssertionError)


# 存储打印日志方法
def setup_logger(config: ConfigLoader):
    relative_log_path = config.get('logging', 'log_file', fallback='logs/logs.log')
    log_file = os.path.join(settings.BASE_DIR, relative_log_path)
    # .upper() 是字符串的方法，表示把字符串转换为全大写形式。
    log_level_str = config.get('logging', 'log_level', fallback='DEBUG').upper()
    log_format = config.get('logging', 'log_format', fallback='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    backup_count = config.get_int('logging', 'backup_count', fallback=30)
    log_level = getattr(logging, log_level_str, logging.DEBUG)
    """
    设置并返回一个日志记录器，使用 TimedRotatingFileHandler 实现按天生成日志文件。
    """
    # 创建一个 logger
    logger = logging.getLogger(__name__)
    # 设置日志记录级别
    logger.setLevel(log_level)
    if not logger.handlers:
        # 创建一个 TimedRotatingFileHandler，按天生成新日志文件
        # log_file 日志文件路径
        # when = 'midnight' 每天午夜轮换日志文件一次（新建一个新文件）
        # interval = 1 每1个周期（这里是1天）执行轮换
        # backupCount = 30 最多保留30个历史日志文件，超过的自动删除
        # encoding = 'utf-8' 避免中文乱码等问题
        handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=backup_count,
                                           encoding='utf-8')
        # 文件名后缀为日期
        handler.suffix = "%Y-%m-%d"
        # 设置日志格式
        handler.setFormatter(logging.Formatter(log_format))
        handler.setLevel(log_level)
        # 将处理器添加到 logger 中
        logger.addHandler(handler)
    return logger


# config = ConfigLoader(settings.INI_FILE)
# logger = setup_logger(config)
#
# logger.info("日志配置读取成功！")
