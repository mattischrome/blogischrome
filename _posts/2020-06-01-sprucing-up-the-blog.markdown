---
title: "Sprucing up the blog 🌲"
date: 2020-06-01
layout: post
category: Writing
tags: [Blogging, Writing, Jekyll, Software, Liquid, Rake, zsh, Twenty]
---
This post explains some of the modifications I made to a minimal Jekyll theme to get my blog to how I like it. This blog (currently) uses the excellent [Sidey theme](https://sidey-jekyll.netlify.app/about) by [Ronalds Vilciņš](https://www.ronaldsvilcins.com). His site looks eerily similar to this one, at least at time of writing.

The theme is pretty minimal in terms of features (and appearance) but it scores well on the Google Page Speed test. I added a few extra features that have kept the speed up, though the site does take longer to compile now.

First off, I added links from each to the next and previous posts so you can read the blog and flit through in chronological order. This was very easy thanks to this article by [Marcin Swieczkowski](https://www.bytedude.com) and the CSS in the theme.

This worked so nicely that I also installed the `jekyll-paginate-v2` plugin and also paginated the home page. For normal people this means that instead of the homepage being a list of almost three hundred posts, Jekyll now breaks this up into separate pages with (my choice of) fifty posts per page. Again I reused the CSS suggested by Marcin to create back and forth links. The plugin adds about three or four seconds to the build time, an increase of about 25-30%.

Next, I really wanted each posts to have a set of links to elsewhere in the site. Ideally this would be based on the content of posts but the `lsi` option in Jekyll has never worked for people who have more than about twenty posts. So instead, I rely on a method explained by Sharath on the Webjada blog that loops through a post's tags and matches other posts that match N or more tags. Sharath's post suggests two common tags but I've gone for three as two tags in common seemed little better than just picking the most recent posts as the most relevant ones.

To ensure each post has suggestions for further reading that are approximately contemporaneous, I've tagged each post with the year it was written, and in the case of some of my travel posts, the year that the events occurred in. I also had to include code to handle the case where a post had no other posts in common. Here's my version of the code, which I saved to my post layout:

```
{% assign maxRelated = 4 %}
{% assign minCommonTags =  3 %}
{% assign maxRelatedCounter = 0 %}
{% assign headerUnprinted = TRUE %}
      
{% for post in site.posts %}
  {% assign sameTagCount = 0 %}
  {% assign commonTags = '' %}
  {% for tag in post.tags %}
    {% if post.url != page.url %}
      {% if page.tags contains tag %}
        {% assign sameTagCount = sameTagCount | plus: 1 %}
        {% capture tagmarkup %} <span class="label label-default">{{ tag }}</span> {% endcapture %}
        {% assign commonTags = commonTags | append: tagmarkup %}
      {% endif %}
    {% endif %}
  {% endfor %}
  {% if sameTagCount >= minCommonTags %}
    {% assign maxRelatedCounter = maxRelatedCounter | plus: 1 %}
    {% if headerUnprinted == TRUE and maxRelatedCounter == 1 %}
      <span class="meta">
      <h4>You May Also Enjoy</h4>
      {% assign headerUnprinted = FALSE %}
    {% endif %}
    <div>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h5>
    </div>
    {% if maxRelatedCounter >= maxRelated %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
{% if headerUnprinted == FALSE %}
  </span>
{% endif %}
```

This doubled my build time - but locally this was from 10 seconds to 20 seconds, which isn't too bad. In future my aim is to use a separate Python script that will run through the `_posts` directory and perform a lexical analysis of my posts. The output will be a CSV in the `_data` directory with the nearest neighbours for each post, then there will be less [Liquid](https://shopify.github.io/liquid/) involved in building the site.

My last modification was to find a [boilerplate Rakefile](https://github.com/gummesson/jekyll-rake-boilerplate) and modify that to better suit this site. I've gone a bit further and added new tasks. One runs Jekyll with the `--drafts` and `--future` modifiers so I can have a look at how future posts look when I've finished writing them. Another task creates an extra deploy option, which I've called 'spruce', that prepends `[skip ci]` to the commit message (and a broom emoji to the end!). This means that Netlify won't bother to build that commit of the site: one way to save those precious free build minutes!

In future I will add another task to the Rakefile that runs the Python code that generates the connections between posts, as mentioned above.

If you're using MacOS, I have one final tip about using Rake and zsh together. Add `alias rake="noglob bundle exec rake"` to your `.zshrc` file, as it will help you supply arguments to your various rake tasks. It took me the best part of an afternoon to figure this out, so hopefully this will save you some time.