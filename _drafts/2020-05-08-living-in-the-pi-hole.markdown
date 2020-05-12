---
layout: post
title: "Living in the Pi hole 🕳"
categories: "Technology"
tags: [Software, Ads, Economics, Twenty, Internet]
date: "2020-05-08"
---
Ingrid bought me a raspberry pi for my birthday. I've set it up in the lounge connected to the router running the [Pi-hole]() software. This nifty bit of kit intercepts your web requests and purges any ask for material on known ad servers. Essentially it's like ad blocking without the ad blocker being on your computer.

I've written before about why I hate web advertising, and I think since then it's got ever more malign. The use of our web browsing habits to track our every move and sell us crap has gotten way worse. Instagram is *awful* and gets more awful with every amendment that Facebook makes. 

I've recently backed up and then purged my Mac. (Not entirely unconnected to the resumption of posts on this blog.) One of many things I have not reinstalled is an ad blocker, so I thought I'd note down some observations because not everything gets blocked and it's good to understand what exactly the Pi-hole protects you from and what you and I need to do to further protect our online privacy.

Doesn't block youtube video ads as well as the Pi-hole website says it does.

Doesn't block facebook ads and doesn't block in-app ads, at least not ads that appear in feeds or streams. I haven't checked the effect on spammy free games (e.g. Words With Friends) or other iAd using apps.

It does block random spammy ads on webpages. I can compare sites like the Guardian on Safari (which is ad free because I'm a subscriber and am logged in) versus on Firefox (why log in twice?). I can also visit the Guardian on my work laptop because I can't redirect that computer to use the Pi Hole.

I was surprised at what gets blocked. Pi-hole breaks some functionality on sites like comparethemarket.com and the John Lewis website, usually where clicks get harvested to track attention and desire flows. This shows the danger of using third parties to capture this data. I used to use Ghostery, which also alerted you to this kind of data collecting. Pi-hole works better in some sense as it simply cuts the connection and refuses to serve the content. In retrospect, Ghostery was probably watching the watchers, collecting data for the collectors.