import structlog

log = structlog.get_logger()
log.info("hello, %s!", "world", key="value!", more_than_strings=[1, 2, 3])
