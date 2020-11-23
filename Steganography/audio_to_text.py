#importing wave pckage for audio processing
import wave

class AudioToText:

	def decode(self, filePath):
		#Reading an audio
		# song = wave.open("song_embedded.wav", mode='rb')
		song = wave.open(str(filePath), mode='rb')

		# Convert audio to byte array
		#frame_bytes stores the list of bytearrays of all frames from the song
		frame_bytes = bytearray(list(song.readframes(song.getnframes())))


		# Extract the LSB of each byte
		extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

		# Convert byte array back to string
		string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

		#Remove fillers from data from string list i.e,"$" that we filled during encoding 
		decoded = string.split("$$$")[0]

		# Print the extracted text
		print("Sucessfully decoded: ",decoded)
		song.close()


if __name__ == '__main__':
	audio_to_text = AudioToText()
	audio_to_text.decode()