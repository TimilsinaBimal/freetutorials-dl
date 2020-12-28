from freetutorials_dl.course import Course
from freetutorials_dl.downloader import download
import click
import os


@click.command()
@click.option("-u", "--url", required=True, prompt="Please Enter the Url to Download:", help="Course Url link eg. https://www.freetutorials.ca/course/the-complete-2020-web-development-bootcamp")
@click.option("-o", "--output", required=False, help="[optional] The output Path where the material will be downloaded")
def fts(url, output):
    if not output:
        output = os.getcwd()
    course = Course(url)
    download(course.getData(), course.title, output)
