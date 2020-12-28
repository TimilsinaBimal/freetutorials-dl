from youtube_dl import YoutubeDL
import os
import re


def download(course, course_title, output):
    course_title = re.sub(r'[^\w\-_\. ]', '_', course_title)

    if os.path.exists(output) == False:
        print("[freetutorials] Creating dirs:", output)
        os.makedirs(output)

    if os.path.exists(os.path.join(output, course_title)) == False:
        os.mkdir(os.path.join(output, course_title))

    index = 0
    for section in course:
        index += 1
        if os.path.exists(os.path.join(output, course_title, str(index) + ". " + section['section'])) == False:
            os.mkdir(os.path.join(output, course_title,
                                  str(index) + ". " + section['section']))
        print(f"[freetutorials] Section {index}: {section['section']}")

        video_count = 0
        for video in section['videos']:
            video_count += 1
            print(
                f"[freetutorials] title: {str(video_count)}. {video['title']}")
            with YoutubeDL({'outtmpl': os.path.join(output, course_title, str(index) + ". " + section['section'], video['title']) + '.mp4'}) as ytdl:
                ytdl.download([video['url']])
