import logging as log
import os

_file_path = os.path.abspath(__file__)
_dir_path = os.path.dirname(_file_path)
_log_file_path = os.path.join(_dir_path, 'users_data_layer.log')

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s [%(filename)s:%(lineno)s] - %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        log.FileHandler(_log_file_path),
        log.StreamHandler(),
    ]
)
