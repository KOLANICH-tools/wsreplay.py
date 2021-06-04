wsreplay.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===========
~~[wheel (GitLab)](https://gitlab.com/KOLANICH-tools/wsreplay.py/-/jobs/artifacts/master/raw/dist/wsreplay-0.CI-py3-none-any.whl?job=build)~~
[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-tools/wsreplay.py/workflows/CI/master/wsreplay-0.CI-py3-none-any.whl)
~~![GitLab Build Status](https://gitlab.com/KOLANICH/wsreplay.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/wsreplay.py/badges/master/coverage.svg)~~
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH-tools/wsreplay.py.svg)](https://coveralls.io/r/KOLANICH-tools/wsreplay.py)
~~[![GitHub Actions](https://github.com/KOLANICH-tools/wsreplay.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-tools/wsreplay.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-tools/wsreplay.py.svg)](https://libraries.io/github/KOLANICH-tools/wsreplay.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

A simple and **incomplete** (doesn't enforce the same parameters and doesn't take into account params, only path matters) WebSocket server that just replays WebSocket messages recorded earlier either with

* [mitmproxy](https://github.com/mitmproxy/mitmproxy)
* or as [HTTP Archive (aka `HAR`)](https://github.com/ahmadnassri/har-spec)

Usage
-----

```bash
wsreplay ./flow ./dump.har
```
