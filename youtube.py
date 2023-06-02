import pytube

video_url = "https://www.youtube.com/watch?v=62g33d7ToWI&list=RDIkDNi7zkogw&index=4"

try:
    yt = pytube.YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download()
    print("Видео успешно скачано!")
except Exception as e:
    print("Произошла ошибка при скачивании видео:", str(e))