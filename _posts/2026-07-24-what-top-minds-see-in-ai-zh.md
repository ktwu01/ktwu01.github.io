---
title: 他们为什么都去了 AI Lab？顶尖头脑看见的，不只是钱
date: 2026-07-24
permalink: /zh/posts/2026/07/what-top-minds-see-in-ai/
redirect_from:
  - /posts/2026/07/what-top-minds-see-in-ai/
lang: zh
tags:
  - artificial-intelligence
  - ai-research
  - talent
  - power
  - hv-analysis
---

> 这是[《颠覆性创新者的思维模式》](/posts/2026/02/mindset-of-disruptive-innovators/)的五个月后续研究。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)
>
> [下载完整 PDF 报告](/research/hv-analysis/顶尖人才为何涌向AI_横纵分析报告.pdf)

{% capture hv_report_raw %}{% include reports/ai-talent-power-hv-report.md %}{% endcapture %}
{% assign hv_report_body = hv_report_raw | remove_first: '# 他们为什么都去了 AI Lab？' | remove_first: '## 顶尖头脑看见的，不只是钱' | remove_first: '> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)' %}
{% assign hv_report_body = hv_report_body | replace: '## ', '__HV_H2__ ' | replace: '# ', '## ' | replace: '__HV_H2__ ', '### ' %}
{% assign hv_report_body = hv_report_body | replace: '### 一句话结论', '## 一句话结论' | replace: '### 研究口径：先把新闻里的“都去了”拆开', '## 研究口径：先把新闻里的“都去了”拆开' %}
{{ hv_report_body | markdownify }}
