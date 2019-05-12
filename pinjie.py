import os

from pydub import AudioSegment
tmp_silence = AudioSegment.silent(duration=2500)

base_dir = './xyxy381'
out_dir = './xyxy381_out/xyxy381.wav'
ii = 0
k = 1;
for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames:
		if k:
			tmp_sound = AudioSegment.from_wav(os.path.join(path,filename))
			ii+=1;
			k = 0;
		else:
			tmp_sound = tmp_sound +tmp_silence+ AudioSegment.from_wav(os.path.join(path,filename))
			print(os.path.join(path,filename))
			ii +=1;
tmp_sound.export(out_dir,format='wav')
print(ii)
