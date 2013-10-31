import os
import pickle
import bwipp_encoders


class Barcode:
	def __init__(self,
	             encoder_name,
	             code,
	             more_option='',
	             position=(50, 50),
	             bwipp=r'data/barcode',
	             header=r'data/header',
	             footer=r'data/footer',
	             encoders=r'data/encoders'):
		self.moveto = position
		self.bwipp = bwipp
		self.header = header
		self.footer = footer
		assert all(map(os.path.exists, (self.bwipp, self.header, self.footer)))
		self.encoders = encoders
		if os.path.exists(self.encoders):
			with open(self.encoders, 'rb') as info:
				self.encoders_info = pickle.load(info)
		else:
			self.encoders_info = bwipp_encoders.gen_encoders(self.bwipp, self.encoders)
		self.full_template = '{bwipp}\n\n{header}\n\n{pos_x} {pos_y} moveto ({code}) ({exop}{more_option})\n/{encoder_name} /uk.co.terryburton.bwipp findresource exec\n\n{footer}'
		self.encoder_name = encoder_name.lower()
		self.code = code
		self.more_option = ' ' + more_option if more_option else ''

	def render(self):
		return self.full_template.format(bwipp=open(self.bwipp).read(),
		                                 header=open(self.header).read(),
		                                 pos_x=self.moveto[0],
		                                 pos_y=self.moveto[1],
		                                 code=self.code,
		                                 exop=self.encoders_info[encoder_name]['exop'],
		                                 more_option=self.more_option,
		                                 encoder_name=self.encoder_name,
		                                 footer=open(self.footer).read())


import sys

encoder_name, code, *more_option = sys.argv[1:]
bCode = Barcode(encoder_name, code, more_option=' '.join(more_option))
sys.stdout.write(bCode.render())
sys.stdout.flush()




