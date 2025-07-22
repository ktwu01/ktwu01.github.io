---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* [Add your Ph.D. information here]
* [Add your Master's degree information here]
* [Add your Bachelor's degree information here]

Work Experience
======
* [Current Position]
  * Institution/Organization
  * Responsibilities and achievements
  * Duration

* [Previous Position]
  * Institution/Organization
  * Responsibilities and achievements
  * Duration
  
Research Interests
======
* [Research Area 1]
* [Research Area 2]
* [Research Area 3]

Skills
======
* Programming Languages
  * [List relevant programming languages]
* Software and Tools
  * [List relevant software and tools]
* Languages
  * [List languages you speak]

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and Leadership
======
* [List your service activities, committee memberships, and leadership roles]

Professional Memberships
======
* [List your professional society memberships]

Awards and Honors
======
* [List your awards and honors]
