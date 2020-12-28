import requests
from bs4 import BeautifulSoup
import re


class Course:
    def __init__(self, course_url):
        if 'freetutorials.ca' not in course_url:
            print("Not a freetutorials url!")
            exit()
        self.course_url = course_url
        self.payload = []
        res = requests.get(course_url, headers={
                           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
        soup = BeautifulSoup(res.content, 'lxml')

        sections = soup.find_all(
            'div', {'class': 'list-brief-content__item'})

        self.course_title = soup.select_one(
            '.bundle-header__about > h1').text.strip()

        print(f'[Course] {self.course_title}')
        print("[freetutorials] Building course json data...")
        for sec in sections:
            section_title = self.section_name(
                sec.find('div', {'class': 'list-brief__top__title'}))

            videos = self.getVideos(sec)
            self.payload.append({
                'section': section_title,
                'videos': videos
            })

    def section_name(self, h2: str):
        h2 = h2.text.replace('\n', '')
        section_title = re.sub(r"Section \d{0,3}:", '', h2)

        # sanitize
        section_title = re.sub(r"[-]{2,}", '', section_title)
        section_title = re.sub(r'[0-9]+', '', section_title)

        return section_title.strip()

    def getVideos(self, section):
        videos = []
        new_sec = section.find('div', {'class': 'list-brief__list'})

        for vid_raw in new_sec.find_all('div', {'class': 'list-brief__item'}):
            # video title
            video_title = vid_raw.find(
                'a', {'class': 'list-brief__item__content'})
            video_title = re.sub(r'[0-9]+', '', video_title)
            video_title = video_title.text.strip()

            # video links
            lenk = "https://learningcrux.com" + \
                vid_raw.find(
                    'a', {'class': 'list-brief__item__content'})['href'].replace('video', 'play') + '/720?type=sort'
            videos.append({
                'title': video_title,
                'url': lenk
            })
        return videos

    def getData(self):
        return self.payload

    @property
    def title(self):
        return self.course_title
