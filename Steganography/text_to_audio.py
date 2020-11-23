
#importing wave pckage for audio processing
import wave

class TextToAudio:
	def encode(self, message, file_path=None):
		self.message = message
		# read wave audio file
		if file_path == None:
			song = wave.open("way.wav", mode='rb')
		else:
			song = wave.open(str(file_path)[5:-2], mode='rb')
		# Read frames and convert to byte array
		frame_bytes = bytearray(list(song.readframes(song.getnframes())))
		#Filling all the bytearrays with our filler variable 
		self.message = self.message + int((len(frame_bytes)-(len(self.message)*8*8))/8) *'$'
		# Convert text to bit array
		bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in self.message])))
		# Replace LSB of each byte of the audio data by one bit from the text bit array
		for i, bit in enumerate(bits):
		    frame_bytes[i] = (frame_bytes[i] & 254) | bit
		# Get the modified bytes
		frame_modified = bytes(frame_bytes)
		# Write bytes to a new wave audio file
		with wave.open('song_embedded.wav', 'wb') as fd:
		    fd.setparams(song.getparams())
		    fd.writeframes(frame_modified)
		song.close()


if __name__ == '__main__':
	# The "secret" text message
	message=input("Enter the text to hide:")
	text_to_audio = TextToAudio()
	text_to_audio.encode(message)