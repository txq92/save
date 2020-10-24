- platform: rest
  resource: http://IPADDRESS:8000/api/status/display
  name: Calendar Display
  body_on: "on"
  body_off: "off"
  is_on_template: '{{ value == "on" }}'
  
  from flask import Flask,request,make_response
import subprocess
app = Flask(__name__)

@app.route('/api/status/display', methods=['POST'])
def hdmi_change():

	state = None
	state = request.get_data()
#	if state is None:
#		print ("state failure")
#	print ("state is: ", state)

	if state == b'on':
		# Turn on the display
		subprocess.call(['/home/pi/rpi-hdmi.sh', 'on'])
		print ("turning on display")
		return ("on") 
	elif state == b'off':
		# Turn off the display
		subprocess.call(['/home/pi/rpi-hdmi.sh', 'off'])
		print ("turning off the display")
		return ("off")
	else:
		abort (404)



@app.route('/api/status/display', methods=['GET'])
def return_status():
	# Return state 
	proc = subprocess.Popen(['/home/pi/rpi-hdmi.sh', 'status'], stdout=subprocess.PIPE)
	if proc.stdout.read() == b'on\n':
		print ("returning on")
#		response = make_response("on")
		return("on")
	else:
		print ("returning off")
	#	response = make_response("off")
		return("off")
#	response.headers['Content-Type'] = 'text/plain'
#	return response
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
