import os
import googleapiclient.discovery
from googleapiclient.errors import HttpError

# Установите значение вашего API-ключа
API_KEY = "AIzaSyB2mUhe7_4wdG951qlKPszLW07XrEQNiTo"

def download_captions(video_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)
    
    try:
        captions = youtube.captions().list(part="id", videoId=video_id).execute()
        if captions["items"]:
            caption_id = captions["items"][0]["id"]
            subtitle = youtube.captions().download(id=caption_id, tfmt="vtt").execute()
            return subtitle
        else:
            print("Субтитры не найдены для видео")
            return None
    except HttpError as e:
        print(f"Произошла ошибка при загрузке субтитров: {e}")
        return None

def save_text_to_file(text, output_file):
    with open(output_file, "w") as file:
        file.write(text)

# Введите ссылку на видео на YouTube
video_url = input("Введите ссылку на видео на YouTube: ")

# Извлечение и сохранение субтитров
video_id = os.path.basename(video_url)
captions = download_captions(video_id)

if captions:
    # Преобразование формата субтитров в текст
    text = captions.replace("<c>", "").replace("</c>", "").replace("\n", " ")
    
    # Сохранение текста в файл
    output_file = "transcribed_text.txt"
    save_text_to_file(text, output_file)
    
    print("Распознавание речи завершено. Текст сохранен в файл", output_file)
