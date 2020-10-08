---
layout: page
title: Math
description: 好记性不如烂键盘
keywords: Math
comments: false
menu: 数学
permalink: /math/
---



<ul class="listing">
{% for math in site.math%}
{% if math.title != "Math Template" %}
<li class="listing-item"><a href="{{ site.url }}{{ math.url }}">{{ math.title }}</a></li>
{% endif %}
{% endfor %}
</ul>
