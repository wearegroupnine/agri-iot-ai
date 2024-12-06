from configparser import ConfigParser
#from lib.logger_opt import *

config_file = './config.ini'
config = ConfigParser()
config.read(config_file)

version = ''

path_obj_yolo = ''

param_yolo_conf_thresh = None 
param_yolo_nms_thresh = None 

def get_version():
    return version

def check_config_section():
    if not config.has_section('common'):
        config.add_section('common')

    if not config.has_section('path'):
        config.add_section('path')

    config.write(open(config_file, 'w'))

def get_config():
    global version, path_obj_yolo, param_yolo_conf_thresh, param_yolo_nms_thresh
    try:
        version = config.get('common', 'version')
    except Exception as e:
        logger.warning(e)
        version = ''

    try:
        path_obj_yolo = config.get('path', 'obj_yolo')
    except Exception as e:
        logger.warning(e)
        path_obj_yolo = ''

    try:
        param_yolo_conf_thresh = config.get('param', 'yolo_conf_thresh')
    except Exception as e:
        logger.warning(e)
        param_yolo_conf_thres = ''

    try:
        param_yolo_nms_thresh  = config.get('param', 'yolo_nms_thresh')
    except Exception as e:
        logger.warning(e)
        param_yolo_nms_thresh = ''

def reload_config():
    check_config_section()
    get_config()

if __name__ == '__main__':
    reload_config()
