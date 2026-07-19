---
title: '为什么 S$5.50 的消费在美国信用卡上只显示 US$4.27？'
date: 2026-07-19
permalink: /zh/posts/2026/07/singapore-gst-usd-conversion/
tags:
  - Singapore
  - GST
  - travel
  - credit cards
  - payments
---

在新加坡消费时，一张收据写着 **S$5.50**，但美国信用卡账户只显示 **US$4.27**。另一笔约 S$48 的消费，则显示为约 US$38。与此同时，刷银行卡乘坐公共交通后，交易也没有立刻出现在 pending 中。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

这看起来像三个问题：商家是不是没有收 GST？银行是不是漏扣了钱？公交费是不是没有记账？

答案来自三套同时运行的机制：**货币换算、含税定价和延迟结算。**

## S$5.50 不是 US$5.50

新加坡元和美元都使用符号“$”。新加坡收据使用 SGD，美国信用卡账户通常使用 USD。

这笔交易的隐含汇率约为：

[
5.50\ \text{SGD} / 4.27\ \text{USD} \approx 1.288\ \text{SGD/USD}
]

因此，S$5.50 约等于 US$4.27；S$48 也约等于 US$38。银行没有漏扣或拆单，只是将商家提交的新加坡元金额换算成信用卡的美元记账金额。

如果信用卡不收 foreign transaction fee，账户中通常也不会再出现一笔境外交易手续费。

## GST 已经包含在 S$5.50 中

GST 是 **Goods and Services Tax**，即商品与服务税。新加坡当前 GST 税率为 9%。

美国消费者常看到结账时再加 sales tax。新加坡采用含税显示：[IRAS 的价格显示规则](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/invoicing-price-display-and-record-keeping/displaying-and-quoting-prices)要求 GST 注册商家向公众展示含税价格。

如果最终价格为 S$5.50：

[
\text{税前价格}=5.50/1.09\approx S\$5.05
]

[
\text{GST}=5.50-5.05\approx S\$0.45
]

因此，S$5.50 由约 S$5.05 的税前价格和 S$0.45 GST 构成。信用卡再将整个 S$5.50 换算为约 US$4.27。GST 不会单独形成第二笔信用卡交易。

## “Not subject to GST” 不一定表示整单免税

收据底部有时会打印：

> *Not subject to GST

星号通常是脚注标记，只适用于带星号的项目，而不是整张订单。例如，少辣、更换面型等免费选项可能显示为 FOC（**Free of Charge**），并带有星号。零金额选项不产生 GST，但收费的主商品仍然需要缴税。

判断整单是否含税，应查看主商品、总额以及 “Incl GST 9%” 等字段，而不能只看底部脚注。

## GST Reg No. 是什么？

GST Reg No. 是商家的 **GST Registration Number**，即 GST 注册号。

它不是 GST 金额，也不是订单号。它用于识别负责收取和申报 GST 的注册主体。可以通过 [IRAS GST Registered Business Search](https://www.iras.gov.sg/digital-services/others/gst-registered-business-search) 核验商家的 GST 注册状态。

公开分享收据时，应遮盖 GST 注册号、商户名称、订单号、时间、地点、二维码和支付凭证等可关联信息。

## 为什么公交交易没有立刻 pending？

新加坡银行卡公共交通支付采用账户制处理。读卡器先记录 tap in 和 tap out，系统随后计算距离票价，再向发卡行提交结算。因此，交通交易可能延迟出现，也可能合并多段行程。

[SimplyGo App](https://simplygo.com.sg/simplygo-app/) 可用于查看已绑定银行卡的行程和支付记录。进出站还应使用相同支付介质：实体卡和手机钱包中的同一张卡可能被识别为不同凭证。

## 结论

- 新加坡收据通常使用 **SGD**
- 美国信用卡账户通常使用 **USD**
- 新加坡面向消费者的价格通常已包含 **9% GST**
- 银行将含税总额换算成美元
- 公共交通交易可能延迟或合并结算

所以，S$5.50 显示为 US$4.27，不是折扣、漏扣、拆单或税收漏洞。

只是两个都写作“$”的货币，加上含税定价与延迟结算，让一笔正常交易看起来像支付系统出了 bug。
