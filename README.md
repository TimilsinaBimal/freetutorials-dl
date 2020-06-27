# freetutorials-dl

A utility to download courses/videos from freetutorials.ca by using [Youtube-DL](https://github.com/ytdl-org/youtube-dl)

<hr>

## How to use

install from pypi.org

```sh
$ sudo pip install freetutorials-dl
```

<hr>

## Instructions

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

## Command Docs

| Flag             | Usage                                 |
| ---------------- | ------------------------------------- |
| -u <br> --url    | url of course/video from learningcrux |
| -o <br> --output | Output path                           |

#### License

-   TimilsinaBimal (MIT)

<h4>Huge thanks to <a href="https://github.com/SwapnilSoni1999/learningcrux-dl">Swapnil Soni</a></h4>
