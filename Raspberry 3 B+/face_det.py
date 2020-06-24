import io
import os
import numpy as np
import cv2
import time
import picamera
import requests
import json
from imgurpython import ImgurClient

def face_det():
	camera = picamera.PiCamera()
	camera.resolution = (200, 200)
	camera.color_effects = (128,128)

	client_id = YOUR_ID
	client_secret = YOUR_CLIENT_SECRET
	client = ImgurClient(client_id, client_secret)
	authorization_url = client.get_auth_url('pin')

	image_path = 'ha_roy.jpg'
	
	subscription_key = YOUR_KEY
	assert subscription_key

	face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

	headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
		    
	params = {
	    'returnFaceId': 'true',
	    'returnFaceLandmarks': 'false',
	    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
	}

	while True:
		stream = io.BytesIO()
		camera.capture(stream, format='jpeg')

		# Construct a numpy array from the stream
		data = np.fromstring(stream.getvalue(), dtype=np.uint8)

		# "Decode" the image from the array, preserving colour
		image = cv2.imdecode(data, 1)
		equ= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
		equ = cv2.equalizeHist(equ)
		cv2.imwrite('ha_roy.jpg', equ)
		
		image = client.upload_from_path(image_path)

		image_url = image['link']

		response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})

		result = response.json()

		if result != []:
			result = result[0]
			if result['faceAttributes']['smile'] >= 0.5:
				camera.close()
				os.remove('ha_roy.jpg')
				return 1
			elif result['faceAttributes']['emotion']['neutral'] >= 0.5:
				camera.close()
				os.remove('ha_roy.jpg')
				return 2
			else:
				camera.close()
				os.remove('ha_roy.jpg')
				return 0
