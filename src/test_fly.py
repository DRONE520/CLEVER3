import logging
import logging.config
import rospy_proxy
import service_logger
import time

# Cервисы квадрокоптера, через объекты-прокси
rospy_proxy = rospy_proxy.RospyProxy()
# Сервис логирования
logger = service_logger.run("test_fly", rospy_proxy)


def land_wait():
    """Посадка и ожидание окончания посадки"""
    rospy_proxy.land()
    while rospy_proxy.get_telemetry().armed:
        rospy_proxy.rospy.sleep(0.2)


logger.info("Взлет")
rospy_proxy.navigate(x=0, y=0, z=0.5, speed=0.5, frame_id='body', auto_arm=True)

logger.info("Задержка")
time.sleep(8)

logger.info("Посадка")
land_wait()
