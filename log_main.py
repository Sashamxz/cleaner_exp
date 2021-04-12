import logging
import sys


def get_logger(name=__file__, file='log.txt', encoding='utf-8'):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] %(filename)s:%(lineno)d %(levelname)-8s %(message)s')

    fh = logging.FileHandler(file, encoding=encoding)
    fh.setFormatter(formatter)
    log.addHandler(fh)

    sh = logging.StreamHandler(stream=sys.stdout)
    sh.setFormatter(formatter)
    log.addHandler(sh)

    return log


log = get_logger()
print = log.debug

# Обходное решение надуманной проблемы несоответствия аргументов print и debug.
# Приятным "побочным" эффектом будет возможность просто писать print()
# print = lambda text="": log.debug(text)


if __name__ == '__main__':
    log.debug('foo')
    log.debug('bar')

    print('')
    print('foo')
    print('bar')
