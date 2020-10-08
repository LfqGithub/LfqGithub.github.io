---
layout: page
title: Quant
description: 好记性不如烂键盘
keywords: Quant
comments: false
menu: 宽客
permalink: /quant/
---



<ul class="listing">
{% for quant in site.quant%}
{% if quant.title != "Quant Template" %}
<li class="listing-item"><a href="{{ site.url }}{{ quant.url }}">{{ quant.title }}</a></li>
{% endif %}
{% endfor %}
</ul>
