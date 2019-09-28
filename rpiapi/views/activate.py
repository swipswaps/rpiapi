import json
from RPi import GPIO


def activate(environ, response, parameter = None):
	
	status = "200 OK"
	
	header = [("Content-Type", "application/json")]
	
	try:
	
		pin = int(parameter)
	
		GPIO.output(pin, 1)
		
		result = GPIO.input(pin)
	
	except Exception as e:

		status = "400 Bad Request"

		result = str(e)

	response(status, header)

	return [json.dumps(result).encode()]