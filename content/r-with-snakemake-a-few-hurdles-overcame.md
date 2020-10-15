Title: R with Snakemake: a few hurdles overcame
Slug: r-with-snakemake-a-few-hurdles-overcame
Date: 2020-10-15 08:27:48

When working on the wrapper for DADA2, I had to respect the grammar of both Python/Snakemake and R.
Here are some of the hurdles I have encountered.

* Keeping the log

Especially when you don't have access to a command `Rscript > {log}` when developping wrappers.

TODO: Find the source of the stackoverflow post

* Passing parameters to R

Either be fully explicit (and redundant) by copying all R functions arguments into Snakemake params.
Or be transparent and pass arguments in a character string that would be further interpreted with the R functions `parse()` and `eval()`

I wanted something more flexible and decided to rely on the R function `do.call()` TODO link advanced R hadley
This way I could pass a Python dictionary from Snakemake that would be interpreted as a named lists in Python. 

However, Snakemake passes the input as unumbered list and as named list so for input/output slots I could not do `do.call(foo, snakemake@unput)`

* Keeping the wildcards with the input names when using expand

I decided to split the issue. First focus on the wrapper aim. Sample names **can** be dirty as long as they are explicit. Nicely formatting names is a downstream rule. It can be done either by R (with RDS modification) or Python (with csv modification).

* Transforming the list of $n$ lists obtained with `expand` into one list of $n$ elements.

```
sapply(snakemake@input,c)
```

