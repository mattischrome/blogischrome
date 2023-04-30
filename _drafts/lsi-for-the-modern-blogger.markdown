---
title: "LSI for the modern blogger"
date: 2021-10-29
layout: post
category: Writing
tags: [LSI, Machine Learning, JavaScript, Python, Blogging, Eleventy, Twenty One]
---

One of the things I like to have when blogging is a list of between 3 and 5 links to other posts on this blog at the foot of each page. This is not a feature that is well supported in many static site generators, especially ones that prize fast build times. Nevertheless, it's a good way to create 'sticky' content and an interesting programming problem to get your teeth into. 

I'd [implemented something for the Jekyll version of the site][1] (in Liquid rather than Ruby) but before I shift over to Eleventy, I want to try and implement a better version of this that:

+ runs a classification engine on my posts locally (i.e. something superior to checking the overlap of tags, tagging posts is some sense harder than writing them)
+ saves the resulting information to be pushed as part of the site repository
+ integrates the recommendation data for the posts into the Netlify eleventy build

Ideally this would be written in JavaScript because that integrates nicely with Eleventy. However, because so much machine learning is done in Python, I started out in Python with the aim of converting toJS later. Since the script will only ever be run locally, conversion to Javascript is not strictly necessary but it's an interesting problem to solve a problem in one language and then port it over.

[1]:	https://mattischrome.com/sprucing-up-the-blog