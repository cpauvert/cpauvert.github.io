Title: LEGOlize DADA2: getting DADA2 into Snakemake
Slug: legolize-dada2
Date: 2020-10-08 12:27
Category: Snakemake
Summary: A (WIP) contribution project to rely on the modularity of Snakemake wrappers to propose a flexible pipeline for processing metabarcoding data.

I finally have the time to properly use the workflow management [Snakemake](https://github.com/snakemake/snakemake) which is great because so many recent developments happened since I've heard of this tool during my master degree. The authors and contributors of Snakemake actually published recently a [preprint](https://doi.org/10.5281/zenodo.4067137) highlighting such features.

Among these features, one could be compared to LEGO&reg; bricks: Snakemake *wrappers*.  They are dedicated Snakemake rule that allow to plug -- much like bricks -- common tools to perform your analysis. These wrappers should pass automatic tests prior to their integration in the repository which safeguard against typos during development that hinders your workflow.

Bricks can even be assembled in dedicated sets, which in the case of Snakemake means that wrappers can be combined to design *meta-wrapper* where a common analysis workflow can be crafted using a selection of wrappers. This convenient idea enables the user to finely tune the level of modularity wished during the design of its Snakemake workflow: from custom rules, wrappers to meta-wrappers[^1].

Snakemake use is rising and there was even recently a [preprint](https://doi.org/10.1101/2020.05.17.095679) for a DADA2 with Snakemake workflow. I was really excited for this huge contribution that, in my opinion, filled a gap. However, I realized that some steps were not parts of my personal workflow (such as the taxonomy) and that instead of this one well running Snakemake workflow -- huge LEGO set --, I'd rather choose from several DADA2 wrappers -- piles of bricks -- to build a more flexible workflow.

It all started when I realised that there were no DADA2 wrappers and even few metabarcoding related wrappers proposed in the repository.  
Last week, I then started writing my first wrappers by mimicking previous R wrappers listed in the [repository](https://snakemake-wrappers.readthedocs.io/en/stable/index.html). I tried to design toy examples to test the wrappers and I even manage to propose a few pull requests on the [Github repository](https://github.com/snakemake/snakemake-wrappers/pulls). However, I realize after going over the corrections proposed by the reviewer that I needed to carefully think ahead my wrapper and their articulations. Indeed, I first proposed wrappers using paired-end reads only which is not truly flexible. Hence some of my wrappers contained duplicated lines of code to cope with the orientation which violates the _don't repeat yourself_ [rule](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
Even worse, it sometimes adds complexity to steps that could be processed unbeknownst of the reads orientation. 

Therefore, I put my pull request on a draft status and will go back to writing properly. I already put on paper the dependency of wrappers to read orientation in order to optimize this workflow. I hope to propose soon these DADA2 wrappers and eventually a DADA2 meta-wrappers as well.

[^1]: Check the [documentation](https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html) for more details on modularisation with Snakemake.
