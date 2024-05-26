import logging
import logging.config
import rospy_proxy
import asyncio
from multiprocessing import Process

logging.config.fileConfig('logging.conf')


def run(log_name: str, rospy: rospy_proxy.RospyProxy) -> logging:
    logger = logging.getLogger(log_name)
    logger.info("*" * 20 + "START PROGRAMM" + "*" * 20)
    logger.info("x\ty\tz")

    p = Process(target=run_logging_with_delay, args=(logger, rospy))
    p.start()

    return logger


def run_logging_with_delay(logger: logging, rospy: rospy_proxy.RospyProxy):
    asyncio.run(logging_state_with_delay(logger, rospy))


async def logging_state_with_delay(logger: logging, rospy: rospy_proxy.RospyProxy):
    while True:
        await asyncio.sleep(0.1)
        await logging_state(logger, rospy)


async def logging_state(logger: logging, rospy: rospy_proxy.RospyProxy):
    telemetry = rospy.get_telemetry()
    x = str(telemetry.x).replace(".", ",")
    y = str(telemetry.y).replace(".", ",")
    z = str(telemetry.z).replace(".", ",")

    logger.debug(f"{x}\t{y}\t{z}")
