# freetutorials-dl

A utility to download courses/videos from freetutorials.ca by using [Youtube-DL](https://github.com/ytdl-org/youtube-dl)

<hr>

## Installation
Install from pypi.org

#### Windows
```sh
$ pip install freetutorials-dl
```
#### Linux and MacOS

```sh
$ pip3 install freetutorials-dl
```

<hr>

## Usage

The tool can be accesed via `fts-dl` command.
eg.

```sh
$ fts-dl --url https://www.freetutorials.ca/course/some-course
```

> Make sure you provide `--url` or `-u` which is required.

and it will download the whole course.

You can also provide `--output <your-path-here>` to save on your desired directory.

eg.

```sh
$ fts-dl --url https://www.freetutorials.ca/course/some-course --output ~/my_course
```

and it will save in the given path.

## Options
 - ```-u``` or ```--url``` : The Course Url to download(Copy it from Course page)
 - ```-o``` or ```--output``` : Path to save the video
 - ```--help``` : Help


#### License

-   TimilsinaBimal (MIT)

<h4>Huge thanks to <a href="https://github.com/SwapnilSoni1999/learningcrux-dl">Swapnil Soni</a></h4>
