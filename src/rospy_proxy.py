# Для использования сервисов, необходимо создать объекты-прокси к ним. 
import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')


class RospyProxy:
    def __init__(self):
        self.get_telemetry = rospy.ServiceProxy(
            'get_telemetry', srv.GetTelemetry)
        self.navigate = rospy.ServiceProxy(
            'navigate', srv.Navigate)
        self.navigate_global = rospy.ServiceProxy(
            'navigate_global', srv.NavigateGlobal)
        self.set_position = rospy.ServiceProxy(
            'set_position', srv.SetPosition)
        self.set_velocity = rospy.ServiceProxy(
            'set_velocity', srv.SetVelocity)
        self.set_attitude = rospy.ServiceProxy(
            'set_attitude', srv.SetAttitude)
        self.set_rates = rospy.ServiceProxy(
            'set_rates', srv.SetRates)
        self.land = rospy.ServiceProxy(
            'land', Trigger)
        # self.set_altitude = rospy.ServiceProxy('set_altitude', srv.SetAltitude)
        # self.self.set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
        # self.set_yaw_rate = rospy.ServiceProxy('set_yaw_rate', srv.SetYawRate)
