import moviepy.editor as ram

change = ram.VideoFileClip('justin.mp4')

change.audio.write_audiofile('Audio.mp3')