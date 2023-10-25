import time
import sys
import inspect
import requests
import json
import math

sys.path.append('/home/pi/.local/lib/python3.9/site-packages')

import speedtest
import serial
import pynmea2

# GPS
serial_port = '/dev/ttyAMA0'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=5.0)
dataout = pynmea2.NMEAStreamReader()

print(inspect.getfile(speedtest))
f = open('./data2.txt', 'a')

try:
    with open('./speed_test_result2.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

def add_measurement(data, wifi_download_speed, wifi_upload_speed, latitude, longitude):
    new_measurement = {
        "wifi_download_speed": wifi_download_speed,
        "wifi_upload_speed": wifi_upload_speed,
        "latitude": latitude,
        "longitude": longitude
    }
    data.append(new_measurement)

wifi = speedtest.Speedtest(secure=True)
#wifi = speedtest.Speedtest()
wifi.get_best_server()

total_download = 0
total_upload = 0
gps_latitude = 0
gps_longitude = 0

loop_num = 1
received_data = "start"

# server_url = 'http://172.21.239.103:4000/'
server_url = 'https://server-kudow.run.goorm.site/'
while(received_data != "end"):
	for j in range(loop_num):
		print("measure start")
		start = time.time()

		download_speed = round(wifi.download()/1000000, 2)
		print("Wifi Download Speed is ", download_speed)
		#f.write(str(download_speed)+'Mbps\n')

		upload_speed = round(wifi.upload()/1000000, 2)
		print("Wifi Upload Speed is ", upload_speed)
		#f.write(str(upload_speed)+'Mbps\n')

		# print("Wifi Ping is ", wifi.results.ping)

		end = time.time()
		print("end")
		print("time : ", end-start)
		
		total_download += download_speed
		total_upload += upload_speed

	print(total_download/loop_num)
	print(total_upload/loop_num)

	f.write(str(total_download/loop_num)+'Mbps\n')
	f.write(str(total_upload/loop_num)+'Mbps\n')
	
	while True:
		gps_read = ser.readline()
		try:
			gps_decode = gps_read.decode('utf-8').strip()
			if gps_decode.startswith('$GPGGA'):
				try:
					gps_read = pynmea2.parse(gps_decode)
					print("Latitude: {} Longitude: {}".format(gps_read.latitude, gps_read.longitude))
					gps_latitude = gps_read.latitude
					gps_longitude = gps_read.longitude
					break
				except pynmea2.ParseError as e:
					print(e)
					pass
		except UnicodeDecodeError as e:
			print("ERROR", e)
			pass
	
	add_measurement(data, total_download/loop_num, total_upload/loop_num, gps_latitude, gps_longitude)
	
	total_download = 0
	total_upload = 0
	
	try:
		response = requests.post(server_url, data='go_or_stop')
		if response.status_code == 200:
			print('send comple')
			received_data = response.text
			print(received_data)
		else:
			print('send not comple')
	except requests.exceptions.RequestException as e:
		print(e)
		
ser.close()
f.close()

file_path = './speed_test_result2.json'
with open(file_path, 'w') as file:
	json.dump(data, file)

with open(file_path, 'r') as file:
	json_data = json.load(file)
print(json_data)

headers = {'Content-type': 'application/json'}

try:
	response = requests.post(server_url, data=json.dumps(json_data), headers=headers)
	response.raise_for_status()
	print('data is successfully uploaded')
except requests.exceptions.RequestException as e:
	print('error occured in upload', str(e)) 
