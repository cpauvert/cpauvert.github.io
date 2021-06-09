Title: mi-atlas: an interactive and evolving catalogue of microbial interactions
Slug: mi-atlas-catalogue-of-microbial-interactions
Date: 2021-06-09 09:34:23
Category: Visualisation
Summary: Checkout [https://cpauvert.github.io/mi-atlas](https://cpauvert.github.io/mi-atlas)

<img style="float: left; border-radius: 5px; margin: 10px; padding: 0;" width="173" height="200" src="{static}/images/logo-mi-atlas.png"> A couple of weeks ago, I read an article by [Pacheco and Segrè, 2019](https://doi.org/10.1093/femsle/fnz125) in *FEMS Microbiology Letters* regarding microbial interactions and how to go beyond a classification dedicated to ecological outcomes only. Of course, no classification is perfect (just like standards will forever be developed to encompass exceptions, [leading to even more standards](https://xkcd.com/927)).

They propose to encode interactions between microorganisms using several binary (`0/1`) or ternary (`0/1/-1`) *attributes* to build a catalog amenable to quantitative analyses. I thought this was a good idea. But I was frustrated that their (huge) initial effort to describe 74 interactions was "buried" in the Supplementary Material section of their article. Such multivariate table with 33 columns, while suitable for machines is hard to encompass for human. So I started to work on how to improve the visualisation of the catalogue and provide means for others scientists to contribute easily.

In the end, I provided:

* a [website](https://cpauvert.github.io/mi-atlas) 
* a [Shiny application](https://cpauvert.shinyapps.io/mi-atlas)
* and a one [Github](https://github.com/cpauvert/mi-atlas) repository to bring them all (*and in the darkness bind them*)

The [website](https://cpauvert.github.io/mi-atlas) presents their framework and the idea behind my project. The [Shiny application](https://cpauvert.shinyapps.io/mi-atlas) displays the catalogue, allows to interactively focus on one interaction and helps users to encode a new interaction within the framework.
Have a look and do not hesitate to [drop an issue](https://github.com/cpauvert/mi-atlas/blob/main/CONTRIBUTING.md) if you feel like it!
