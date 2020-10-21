Title: R with Snakemake: a few hurdles to overcome
Slug: r-with-snakemake-a-few-hurdles-to-overcome
Date: 2020-10-21 15:20:34
Category: Snakemake
Summary: Suggested solutions to issues I dealt with when wrapping R scripts for Snakemake.

When working on the [wrappers for DADA2]({filename}/snakemake/legolize-dada2.md), I had to respect both the grammar of Python/Snakemake and R. Here are some of the hurdles I have encountered.

## Keeping the log

Keeping track of the log is quite easy in Snakemake when the tools can run in the shell. Don't mistake me, R scripts can also be run on the shell using `Rscript` and [Deer and Langer](https://lachlandeer.github.io/snakemake-econ-r-tutorial/logging-output-and-errors.html) showed that you can use the command `Rscript > {log}` to correctly keep track of your script. However, when using wrappers you do not have access to this command because in the [Snakemake grammar](https://snakemake.readthedocs.io/en/stable/snakefiles/writing_snakefiles.html#grammar) instead of the `script:` word you have the `wrapper:` word.

I knew the `sink()` R function to redirect the output of R commands to a file. But when trying to redirect both messages and errors to the file when testing my wrappers it failed. The following [post](https://stackoverflow.com/a/48173272) on stackoverflow provided the solution, which in short needs two invocations of `sink()` to be able to capture both messages. It is now included in the wrappers I wrote.

## Passing parameters to R

Snakemake provide both reproducible and customizable workflows. But providing parameters to R wrappers was harder than I thought. Looking at others R wrappers I saw two approaches. Either be fully explicit (and redundant) by copying all the R arguments of the needed functions into the Snakemake `params:` word. Or be transparent and pass arguments in a character string that would be further interpreted with the R functions `parse()` and `eval()`.

I wanted something more flexible and decided to rely on the R function `do.call()` which enables the execution of a function based on arguments provided as named list (see 6.2.4 from [Hadley's Advanced R](https://adv-r.hadley.nz/functions.html#function-fundamentals)).

Using such structure, I could pass a Python dictionary to Snakemake `params:` that would then be interpreted as a named lists in R. For instance:

	:::python
	rule dada2_filter_trim_pe:
	    # [...]
	    params:
	        {'maxEE':1, 'truncLen': [240,200] }
	    # [...]

Snakemake convert the Python dictionary into a named list which can be directly used for the R function (here `dada2::filterAndTrim()`). Such named list if part of the larger `snakemake` S4 object that we can access in R (more info on [Snakemake docs](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#external-scripts)). 

However, you cannot concatenate the lists provided (`snakemake@input`, `snakemake@output` and `snakemake@params`) and expect `do.call()` to do all the work. No, because Snakemake passes the `input:` as unnumbered list **and** as named list. So for input and output slots I could not do directly `do.call(filterAndTrim, snakemake@input)`. Instead, I needed to prepare the arguments as follow:

	:::r
	args<-list(
	        fwd = snakemake@input[["fwd"]],
	        rev = snakemake@input[["rev"]],
	        filt = snakemake@output[["filt"]],
	        filt.rev = snakemake@output[["filt_rev"]],
	        multithread=snakemake@threads
	)

Most of the submitted Snakemake wrappers can now accept Python dictionaries to customize the underlying DADA2 R functions.

These wrappers are currently under reviews by the team of the Snakemake wrappers repository. Meanwhile I try to design a DADA2 meta-wrapper to be able to nicely assemble these _bricks_.
