import copy
from typing import List, Optional, Dict

class TemperatureSensor:
    """ 
    Defines acceptable temperatures for aircrafts 
    Demonstrates ENCAPSULATION. 
    Data (__history) is a private attribute that is hidden from outside access.
    """
    MAX_SAFE_TEMP = 180 #Celsius
    
    def __init__(self, sensor_id: str):
    # type hinting, setting sensor_id to str
    #name mangling to act as private attribute
    self.sensor_id: str = sensor_id
    self.__history: List[float] = []
    
    def record_temperature(self, value: float) ->str:
        """ 
        logs temperature as float without returning a value
        """
        try:
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid telemetry datatype: {type(value)}")
            if value > self.MAX_SAFE_TEMP:
                return(f"[ALARM] Sensor {self.sensor_id}: CRITICAL HEAT DETECTED")
            self.__history.append(float(value))
        except ValueError as e:
            #log Error to a non-volatile system
            return("non critical error suppressed: {e}")