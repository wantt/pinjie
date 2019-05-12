import os

from pydub import AudioSegment


base_dir = './wav'

for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames:
		if filename.endswith('./wav'):
			tmp = AudioSegment.from_wav(os.path.join(path,filename))
			tmp.set_frame_rate(16000)
			tmp.set_channels(1)
			tmp.set_sample_width(2)
			tmp.export(os.path.join(path,filename))
