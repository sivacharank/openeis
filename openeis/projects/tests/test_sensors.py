'''
Created on May 11, 2014

@author: D3M614
'''
import unittest
from schema import sensors
from _ctypes import ArgumentError

class TestSensor(unittest.TestCase):
    
    def test_sensor_error_when_unit_type_not_set(self):
        self.assertRaises(ArgumentError, lambda: sensors.Sensor())


    def test_sensor_instance(self):
        test = sensors.CondenserFanPower()
        
        self.assertEqual("boolean", test.data_type, "Data type isn't boolean")
        self.assertTrue(isinstance(test, sensors.Sensor), "It's not a sensor!")
        self.assertIsNone(test.minimum, "Minimum isn't none!")
        self.assertIsNone(test.maximum, "Maximum isn't none!")
        self.assertIsNotNone(test.sensor_type, 'sensor_type is none!')       

    
    
    

