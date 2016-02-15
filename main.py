from pydub import AudioSegment
import re
import sys
import traceback
# PyDub uses miliseconds, never forget to multiply 
miliseconds = 1000
pattern = "[0-9]{0,2}:?[0-9]{2}:[0-9]{2}"
global_states = []
global_names = []

def pass_to_split(audio_origin, list_txt, global_names) :
	song = AudioSegment.from_mp3(audio_origin)
	global_states = get_array_states(list_txt)
	while len(global_states) >1:
		state = get_next_state(global_states)
		global_states = global_states[1:]
		print state
		name = global_names[0]
		global_names = global_names[1:]
		if(len(state) == 2):
			split(song, name, state[0], state[1])
		else:
			split(song, name, state[0])
			global_states = []

def split(audio, name, init, end):
	new_init = time_in_seconds(init) * miliseconds
	new_end = time_in_seconds(end) * miliseconds
	new_audio = audio[new_init:new_end]
	new_audio.export(name, format ="wav")
	print "Exported " + name

def time_in_seconds(youtube_mark):
	timestr = youtube_mark
	ftr = [3600,60,1]
	return sum([a*b for a,b in zip(ftr, map(int,timestr.split(':')))])

def get_array_states(list_txt):
	array = []
	with open(list_txt, "r") as f:
		for line in f:
			global_names.append(line[10:])
			array.append(line)
	return array

def get_next_state(global_states):
	if(len(global_states)==1):
		try:
			res = re.search(pattern,global_states[0]).group(0)
			global_states = []
			return (res)
		except:
			print traceback.format_exc()
			sys.exit("Alpha says: ay ay ay")			
	else:
		try:
			first = re.search(pattern, global_states[0]).group(0)
			
			second = re.search(pattern, global_states[1]).group(0)
			return (first, second)
		except:
			print traceback.format_exc()
			sys.exit("Alpha says: ay ay ay")

#print time_in_seconds("00:04:23")
#print get_next("nuevo.txt")
#print get_next_state("nuevo.txt")
#global_states = get_array_states("nuevo.txt")
#while len(global_states) != 0 :
	#print get_next_state()

def main():
	pass_to_split(sys.argv[1], sys.argv[2], global_names)
if __name__ == '__main__':
	main()