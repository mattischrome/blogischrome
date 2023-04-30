---
title: "How to add new information to a markdown file with Python"
date: "2022-03-20"
layout: post
category: Programming
tags: [Programming, Text processing, Blog, Python, Twenty Two]
summary: "In order to move my blog posts to a new backend and theme, I needed to add some additional YAML keys and values to my blog's markdown files. Here's how I did it."
---
## What are we up to?
In migrating from [Jekyll]() to [Next.js](), the opportunity arose to use [a blog starter theme]() that needed some additional keys in the YAML headers of my markdown files.

Aside for the uninitiated: a [YAML]() header is set of key-value pairs containing the metadata of your blog posts. They look like this:

```yaml
---
title: 'the title of the post'
date: 2022-02-22
layout: post
tags: ['tag 1', 'tag 2']
category: 'Post category'
---
```

The theme I'm using includes an additional `summary:` key in the YAML, which the Jekyll version of the site didn't have. It is meant to provide a short summary of the post. This post explains a program I wrote in Python to batch process my existing markdown files, adding in the extra YAML key and then using the first paragraph of the markdown as the value for that key.

## Alternatives
I didn't really have to use awk for this. But I was already at the command line changing my file extensions from `*.markdown` to `*.md`, so it seemed like a fun game to do it from there.

Nevertheless, I did consider some alternatives. One was to use either sed or awk. These are command line tools popular on Unix-like systems that process text. However, when I tried to conceive how to do this with these tools I couldn't quite grok how to do it!

Python because there is a handy module called grey matter that is nifty at taking apart files with YAML headers. Python is also really nice to program in so repeating the process over 300 odd files would have been super easy. However, a future post will recount a similar technique for another purpose. Watch out for that if Python is one of your interests!

Another approach would be to not change any of my old posts and set up a default value for the `summary:` tag in the YAML header. However, I wasn't convinced it would be very easy to do this in a dynamic way that pulled out the first paragraph of the post out as the summary. However, I like to have my post files uniform and as a result it wasn't really acceptable to me to have some files with this tag and some not. Also, I know that for my existing posts the first paragraph of the post is not always the best summary and that meant I needed a solution that could be edited later. 

Finally, you could also probably use some multi-line regular expressions and the search and replace across multiple files in an editor like Visual Studio Code. If you're on a windows system that might be your best bet. This has been how I've done these sorts of things in the past, but having done it a couple of times now I want to be able to pick up a script and run it from the terminal instead of spending an afternoon looking up the correct regexes.

## Basic approach
1. Import each file using the Frontmatter package
2. Get the first line of text from the body
3. Insert this as the value associated with new `summary` key in the frontmatter using the `__setitem__()`method 
4. Dump the new version of the file - I don't even have to overwrite because I need to change the file extension.

Pretty simple huh?



