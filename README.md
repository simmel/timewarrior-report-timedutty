# timewarrior-report-timedutty

A report plugin for [Timewarrior](https://timewarrior.net/) that reports in
["Timeduty format"](https://timeduty.com/). Well it's probably more like
[PM3](https://pm3.se/) and [ITIL](https://en.wikipedia.org/wiki/ITIL) but who's
keeping track?

## Installation

1. `mkdir -p ~/.timewarrior/extensions/`
1. `pipx install -e git+https://github.com/simmel/timewarrior-report-timedutty.git@master#egg=timewarrior-report-timedutty`
1. `ln -s $(which timewarrior-report-timedutty) ~/.timewarrior/extensions/timedutty`


## Usage

```terminal
$ timew timedutty
Total by Tag

Tag                                            Total
----------------------------------------- ----------
ServiceX Incident                                  2
ServiceY Service request                           1
                                          ----------
Total                                              3

$
```
