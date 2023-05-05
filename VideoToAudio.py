import moviepy.editor as mp


location = input("Video location: ")

if location[-3:] != '.mp4':
    location += ".mp4"

my_clip = mp.VideoFileClip(location)

my_clip.audio.write_audiofile(r"audio.mp3")