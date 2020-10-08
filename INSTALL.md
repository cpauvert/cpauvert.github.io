# Steps for the set up of Pelican website

mamba create -n pelican -c conda-forge pelican markdown
conda activate pelican
sudo apt-get install ghp-import

Start with the distant repo that should contain the website

```
gh repo clone cpauvert/cpauvert.github.io
```

Get in the directory and set the use of Github Pages and especially user pages
```
cd cpauvert.github.io/
pelican-quickstart 
```

Edit the `publishconf.py` file to make sure that the variable `DELETE_OUTPUT_DIRECTORY`  is set to `False`.

Edit the `Makefile` to set the branch name for the output of the website. Do not forget to set this branch in Github to be used for the Github Pages.

```
GITHUB_PAGES_BRANCH=gh-pages
```
Standard commits are created for the newly created Markdown file of the first post

```
touch content/hello-world.md 
make html && make serve # test whether the post if nicely rendered
git add content/hello-world.md 
git commit -m "First post"
```
Before publishing automatically with the `make` rules, I first did it by hand to be sure to set the remote branch

```
git checkout gh-pages 
git push -u origin gh-pages 
git checkout main 
```

For the others pages, the following routine was used:

```
git add content/images/head.jpg content/pages/about.md 
git commit -m "Add About page"
make html
make serve
make publish 
make github 
```
