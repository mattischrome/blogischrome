---
categories: Programming
date: 2022-12-16
layout: post
summary: "I wanted to move between JSON and CSV representations of the same data using R"
tags:
- R
- JSON
- CSV
- Data Manipulation
- Twenty Two
title: JSON and CSV manipulation with 
---

JSON is a decent format for structuring data, particularly when you have lists or tables within a row. However, updating their structure and inserting new information is not always straightforward. This post is about using R to manipulate relational data that ultimately ends up being in a JSON format for use in web pages. I wrote it mostly to remember my processes for next time.

For the purposes of this post, let's consider my three favourite albums of 2022 so far and look at their track lists. We can explore how we might represent the various aspects of this track list in both a CSV and JSON format. (This was not why I was looking into these issues, but it's probably a more interesting example!)

The albums are:
* "Dragon New Warm Mountain I Believe In You" by Big Thief
* "Endless Rooms" by Rolling Blackouts Coastal Fever
* "Alpha Zulu" by Phoenix

Here's a JSON rendering of those three albums' track lists:
```json


```

This formatting works well for working through that data and building a little widget that displays each album along with its track list. Here's a screenshot of something I made to demonstrate this:

![][image-1]

The biggest issue I have with JSON, and I think it's something I share with others, is that it's not very easy to keep up to date. For example, perhaps Phoenix issue a deluxe issue of the album with a couple of remixes added to the end. To update my JSON file I have to navigate to the object representing their album and then edit the track list of the album.

Also, what if the arrays within my JSON become more complicated. I've already got track name and track length in my track list array. What if I also want to add the name of the track's producer or perhaps my rating of each track? The syntax for doing that is simple enough, I can add `, "rating": 5` to the end of each entry of my track list array. But what if I forget a track, or stuff it up? This is not a robust way of adding this data.

However, editing CSVs in Excel is a breeze[^1]. Once you have a CSV you can also import it to R and manipulate rows and columns there.[^2]

[^1]:	I know that invoking Excel is a kind of heresy but I'm all for using right tools for the job. Using VS code with rainbow columms is another option. 

[^2]:	In fact, if I were to get better at using lists in R data frames, I would probably remove the need for most of this post.

[image-1]:	/path/to/screenshot.png "A screenshot of a demo of an album display widget"