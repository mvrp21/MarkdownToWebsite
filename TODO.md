# TODO

I keep forgetting what to do so I'll save it here temporarily:
Ideally each one will be a commit.

## Not even necessary I think
- [ ] Prettify HTML output

## Could do it now
- [x] Config file
- [x] Auto navigation generation
- [x] Make <head> more SEO friendly
- [ ] "Page" variable for jinja (btw variables inside the markdown are not replaced yet)
- [ ] Better check for skipping compilation

## Meh I'm lazy
- [ ] Base CSS
- [ ] Link checking (pages that do not exist, mayyyybe check links for other websites as well, at least try to see if it's dead)

## I feel lazier with these
- [ ] Classes for links (& codeblocks)
- [ ] Pygments (requires classes for codeblocks I think)

## Even lazier
- [ ] Make file/directory-specific `static/` associations (most likely will end up being a file with a map, maybe even allow regexes? or check page variables/metadata?)
- [ ] Support either inline html or straight up html files instead of markdown (specially useful for the index page, which will be quite different from the other ones)
