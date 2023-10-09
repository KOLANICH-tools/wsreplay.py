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

**We have moved to https://codeberg.org/KOLANICH-tools/wsreplay.py, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in succeeding of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

A simple and **incomplete** (doesn't enforce the same parameters and doesn't take into account params, only path matters) WebSocket server that just replays WebSocket messages recorded earlier either with

* [mitmproxy](https://github.com/mitmproxy/mitmproxy)
* or as [HTTP Archive (aka `HAR`)](https://github.com/ahmadnassri/har-spec)

Usage
-----

```bash
wsreplay ./flow ./dump.har
```
