---
title: 'Who Hoards Multimodal Data for Real, Meta, ByteDance, X, and the Visa Plot Twist'
date: 2026-05-08
permalink: /posts/2026/05/multimodal-data-moat-meta-bytedance-x-visa/
tags:
  - AI
  - Multimodal
  - Meta
  - ByteDance
  - TikTok
  - X
  - Twitter
  - Training data
  - Visa
  - LLM
  - VLM
---

Ask which campus actually sits on the best multimodal feedstock for GPT-4V-class perception, Sora-class video, Gemini-scale bundles, and Meta Emu-style image stacks, and the short answer is almost vulgar in how cleanly it splits three big piles. Meta still pulls ahead by a chasm on stills, ByteDance owns the high-velocity short-video river that is really motion plus audio, and X ships the smallest absolute media volume yet the weirdest leverage on tight text-image coupling and live-event semantics.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

I do not have internal ledgers for any of these companies. Everything below is a back-of-the-envelope model, public MAU figures plus daily post cadence, then a sanity pass against how engineers actually talk about training mix. The point is the shape of the curves, not a forensic audit.

## A rough pyramid of visual mass

If you rank raw photo and general visual inventory, Meta leads by a full tier, ByteDance follows with video as the workhorse asset because thirty-to-sixty frames per second is still frames under the hood, and X sits third with a text-first platform where media is a minority share of posts.

Useful definition first. Treat high-quality multimodal training data as image-text or video-text pairs that genuinely move the needle on large perception and generation models. That constraint matters more than vanity MAU.

## Meta as the still-image warehouse

Meta is one of the world’s largest still-image warehouses, and Instagram is a prestige beauty-and-object dataset by accident of product design. Family-of-apps MAU in the three-billion range is the usual public ballpark. Upload-wise, Instagram often gets quoted at one-hundred-million-plus photos or videos per day on conservative estimates, with Stories adding another moon, Facebook adds hundreds of millions of photos per day in the same conversation, and WhatsApp moves billions of images daily. End-to-end encryption means those bits are not a free buffet for model training, yet the public surface of Facebook and Instagram alone is enough to reset expectations for what competitor-scale means.

Historical stock on the order of one hundred billion-plus photos is the kind of round number people say in hallways when they mean orders of magnitude, not accounting precision. Social scenes, faces, everyday objects, tags, short captions glued to pixels, that is the classic recipe for recognition and Emu-class generation. Llama’s multimodal climb and SAM-style segmentation did not drop out of nowhere. The geometry of the data made aggressive supervision easier than average.

## ByteDance as motion and audio

ByteDance’s crown asset is video, time-stamped, audio-locked, dense frame sequences. TikTok plus Douyin plus Toutiao commonly sit in the two-and-a-half-billion MAU conversation. TikTok new uploads land in the twenty-three-to-thirty-four million clips per day band in plenty of outside estimates, Douyin in the same league by order of magnitude.

If a typical clip is fifteen seconds at thirty frames per second, you are already multiplying into ten-billion-plus new frames per day before redundancy pruning. That redundancy is not pure waste for world models, temporal correlation is part of the physics signal people chase with Sora-like simulators. The text-and-image modes inside TikTok and Douyin are catching up on stills, slope matters as much as stock. Tight audio-visual alignment and motion traces are the prize for human motion and video generation heads.

## X as real-time context

X is smallest by mass, yet meme culture and news velocity are not a consolation prize. They are a different training gradient.

MAU five-fifty to six hundred million is the usual quoted window. Roughly five hundred million posts a day, media attachments on the order of ten to fifteen percent, lands around fifty to seventy-five million media objects daily when you want a single number to argue over.

Historical stock counts land in the tens of billions class, far shy of Meta-scale trillions if you count stills. Semantic density is high, glamour is not the point. Screenshots, captioned reaction images, charts, compressed mess, the pixel story is ugly, the caption story is loud.

Grok’s pitch around freshness makes sense against that backdrop. The feed teaches what just happened to a photo in the wild, not how to paint a salon-ready cat.

## Moats beyond headcount

Once you leave parade metrics, the real question is what you are allowed to scale into a pipeline without boiling legal.

Meta juggles private accounts and copyright noise, public extraction alone is already civilization-scale. ByteDance rides a default-public creator culture with its own cross-border friction, and product gravity pushes Doubao-class video and motion-heavy research. X is almost entirely public conversation by design, alignment between tweet and image is often direct commentary, sarcasm included, which is gold for multimodal semantics even when resolution hurts.

Aesthetic leaderboard still tilts Instagram at the top. TikTok and Douyin add heavy filters and aggressive compression. X compresses and screenshots ruthlessly. Training goals mirror the bias, Emu and Llama Vision chase general visual understanding, video-first labs chase world models and embodiment hints, Grok-style stacks lean on OCR plus real-time framing of events.

This is not a single winner podium. It is three different curvature profiles.

## How the three piles close out

Meta is the still-image landlord in the crude sense people mean when they whisper Instagram during a GPU budgeting meeting. If your north star is Midjourney-grade text-to-image or GPT-4V-grade general vision, that hoard is the unfair tangible.

ByteDance holds keys to the physics-and-motion bet. If the industry’s horizon is long-horizon video synthesis plus embodied robotics, causal motion matters more than a single glossy frame, and ByteDance-shaped rivers line up with that hunger.

X wins on the cognitive layer. Smaller media mass, faster refresh, sharper training signal for sarcasm, news screenshots, and why a photo became a punchline today instead of a gallery piece.

---

One more beat from a chat screenshot that floated by. Someone said Visa data is higher quality yet basically untouchable, and that is less gossip than central cast for anyone who builds with behavioral truth.

Social feeds are performance art. Card swipes are revealed preference with money attached. Likes posture, purchases confirm. Compared with scrubbing spam and bot swarms out of text-and-image dumps, a clean transaction row with time, merchant, amount, and location is already halfway to a supervised table for forecasting and risk.

Intent lives in search, interest lives in social, outcome lives in payments. Recommendation models, credit systems, macro pulses, transaction graphs really do feel like god-view data when you phrase it carefully, stitching physical traces to spending power over years.

The moat is also the lock. Financial records sit in the most sensitive tier of personal information. PCI DSS, GDPR-class regimes, and basic fear of catastrophic breach mean these streams live behind thick governance even inside the network operator. Abuse here is not annoyance-scale, it is solvency and identity-scale, so differential privacy, masking, and narrow tooling are the default conversation starter, not naive end-to-end training stories.

Visa-shaped truth is deep, low-noise behavior. Google-shaped scale, think YouTube depth and multimodal reach, is wide information. Depth versus breadth, not the same leaderboard axis as Instagram versus TikTok versus X. Pick the coordinate system before you argue who wins.
