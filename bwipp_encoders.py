import os
import pickle

encoder_begin = '% --BEGIN ENCODER'
encoder_req = '% --REQUIRES'
encoder_desc = '% --DESC:'
encoder_exam = '% --EXAM:'
encoder_exop = '% --EXOP:'
encoder_rndr = '% --RNDR:'


def gen_encoders(bwipp_path, info_path):
	if os.path.exists(bwipp_path):
		encoder_flag = False
		encoders = dict()
		with open(bwipp_path, 'r') as bwipp:
			for line in bwipp.readlines():
				if encoder_begin in line:
					encoder_flag = True
					name = line[len(encoder_begin):].strip().strip('-').lower()
					encoders[name] = dict()
					continue
				if encoder_flag:
					if encoder_req in line:
						requires = line[len(encoder_req):].strip().strip('-')
						encoders[name]['requires'] = requires if requires else None
					elif encoder_desc in line:
						desc = line[len(encoder_desc):].strip().strip('-')
						encoders[name]['desc'] = desc if desc else None
					elif encoder_exam in line:
						exam = line[len(encoder_exam):].strip().strip('-')
						encoders[name]['exam'] = exam if exam else None
					elif encoder_exop in line:
						exop = line[len(encoder_exop):].strip().strip('-')
						encoders[name]['exop'] = exop if exop else None
					elif encoder_rndr in line:
						rndr = line[len(encoder_rndr):].strip().strip('-')
						encoders[name]['rndr'] = rndr if rndr else None
						encoder_flag = False
		with open(info_path, 'wb') as info:
			pickle.dump(encoders, info)
		return encoders