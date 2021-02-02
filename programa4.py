import vrep 
from pedrohj import *

# Configuração (Setup)
arduino = objeto()
motorE = arduino.obter("DynamicLeftJoint")
motorD = arduino.obter("DynamicRightJoint")
sensorEsq = arduino.obter("LeftSensor")
sensorDir = arduino.obter("RightSensor")

# Loop infinito
while True:

	# Se o sensorEsq atuado então ligar MotorD
	if arduino.digitalRead(sensorEsq) == False:
		arduino.velocidade(motorD, 500)
		arduino.velocidade(motorE, 0)

	if arduino.digitalRead(sensorDir) == False:
		arduino.velocidade(motorE, 500)
		arduino.velocidade(motorD, 0)
	

	arduino.delay(10)
	arduino.rodar()
	

	
