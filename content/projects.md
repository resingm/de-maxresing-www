---
public: true
title: Projects
header:
    title: "My Projects"
    subtitle: "The tip of the iceberg..."
    content:
        Here you can see a very brief selection of the projects I have worked on
        and being involved with. This illustrates just a short selection
        Of course, this is just the tip of the iceberg. If you look for all my
        contributions, I refer to my [Codeberg](https://codeberg.org/resingm)
        and [GitHub](https://github.com/resingm) repositories.
---

# DNS Resilience Dashboard

My current professional involvement is at my University, supporting the
team of the [OpenINTEL](https://openintel.nl). Based on the OpenINTEL
platform, we provide a daily analysis of the DNSSEC landscape in the two
ccTLDs `.ch.` and `.li.`. The Swiss NREN [SWITCH](https://www.switch.ch/en/)
has requested the product and links it to a financial incentive. Since
the start of the project in Summer 2021, the DNSSEC deployment has grown
from under 10% to [36% in April 2022](https://www.nic.ch/statistics/dnssec/).

My involvement in this project includes the data analysis and export as
well as the back- and front-end implementation, deployment and operation
of the DNS resilience dashboard.

**Navigation:**
[DNS Resilience Dashboard](https://dns-resilience.openintel.nl)


***


# yacf - Yet Another Configuration Framework

With advancing Python projects, I realized I tend to parse configuration
files similarly in all projects I have worked on. Thus, I decided to
abstract the logic and wrap it into a package.

*yacf* is a very lightweight and slim configuration framework with very
limited features. It aims to not end up as a bloated and convoluted
framework. Configuration has to be kept simple and maintainable.


**Navigation:**
[Code](https://github.com/resingm/yacf),
[Package](https://pypi.org/project/yacf/)


***


# static.maxresing.de

This service was initially hosted on [webfsd](https://github.com/ourway/webfsd).
It aims to serve static content. My servers are running 24/7 anyway, so I
figured I could also allow other people to host their files on this service.

This is mostly aimed to host resources for friends. However, I am open to invite
anyone if they want to share their resources. I moved away from webfsd at some
point. These days, the service is running on [Nginx](https://www.nginx.com).

**Navigation:**
[Web](https://static.maxresing.de)


***


# Bakkiecounter.com

This web app is aimed to help tracking your coffee consumption. It is
intentionally kept simple. The project is a result of a few days of rapid
development. After finishing the core application, we decided to not spend much
time on it anymore, except of using it.

Feel free to use it as well. It is free of charge.

## Why?

A friend of mine and me decided to track our coffee consumption. We discovered
that there is no open-source app on the market. The app we were using was an
outdated Android application released for Android 2.7. Even if we would not
bother about the UX, the closed-source and the outdated implementation can be
a potential vulnerability. Hence, we started working on our own web application.

**Navigation:**
[Web](https://bakkiecounter.com)
[Code (Backend)](https://codeberg.org/bakkie2go/bakkiecounter-backend)
[Code (Frontend)](https://codeberg.org/bakkie2go/bakkiecounter-frontend)

