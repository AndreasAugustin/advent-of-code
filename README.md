# advent-of-code

[Advent of code](https://adventofcode.com/)

## CI

Travis build

[![Build Status](https://travis-ci.org/AndreasAugustin/advent-of-code.svg?branch=master)](https://travis-ci.org/AndreasAugustin/advent-of-code)

## Make

Most development commands are available in `Makefile`.

```bash
$ make help
```

## Starting a Docker session

You can start a shell to work in a Docker container with the following make command

`$ make shell`

This will start a shell in the container. The container also supports TMUX to run a session multiplexer with

`$ make tmux`

This will start a tmux session so you can create multiple windows in the same docker container.
This is especially helpful if you want to run your backend application in one window and have a
second window running your tests.
For more details check out a [quick intro blogpost](https://robots.thoughtbot.com/a-tmux-crash-course).
In case you don't want to use any tmux features though you can treat this like
any other shell window and simply ctrl-d to exit.
