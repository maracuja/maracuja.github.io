---
title: Bfi Player
date: 2014-10-11 00:00:01 Z
layout: post
client: BFI
project: BFI Player
class: bfi
---

BFI Player is the revamped video rental site for the BFI using the our in-house VoD
platform Skylark. I lead the team developing the player site and the Skylark platform
through to delivery.

Architecture-wise the site is a python/django website using a python/django based API.
Both are served behind their own infrastructure on AWS. Static assets are served via S3
with videos coming from the OVP's CDN.

Entitlements and eCommerce transactions and 3rd
party synchronisation is handled using a RabbitMq server with dedicated workers for each
of the concerns.
