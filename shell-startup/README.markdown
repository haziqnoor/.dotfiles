# Shell startup files

Startup files to make `zsh`, `bash`, and `sh` shells play nicely.
Settings can be shared across all shells, or made specific to
each shell. Inspired by Peter Ward's blog post [Shell startup
scripts](http://blog.flowblok.id.au/2013-02/shell-startup-scripts.html).

## Installation

Symlink few of the files to `~`:

    ln -svf ~/.dotfiles/shell-startup/zsh/interactive ~/.zshrc
    ln -svf ~/.dotfiles/shell-startup/zsh/env ~/.zshenv
    ln -svf ~/.dotfiles/shell-startup/bash/logout ~/.bash_logout
    ln -svf ~/.dotfiles/shell-startup/zsh/zprofile ~/.zprofile
    ln -svf ~/.dotfiles/shell-startup/shell/profile ~/.profile
    ln -svf ~/.dotfiles/shell-startup/bash/bashrc ~/.bashrc
    ln -svf ~/.dotfiles/shell-startup/bash/bash_profile ~/.bash_profile
    ln -svf ~/.dotfiles/shell-startup/shell/inputrc ~/.inputrc

Then you can make changes you normally do using the symlinks:

  bash: `~/.bashrc`, `~/.bash_profile`, `~/bash_logout`.
  zsh: `~/.zshrc`, `~/.zshenv`, `~/.zprofile`.
  `~/.profile`, `~/.inputrc`.

## Customization

To modify `$PATH` and put environment variables that will run on all shells, edit `~/.dotfiles/shell-startup/shell/login`.

To add specific settings for `zsh` or `bash`, edit:

  `~/.zshrc`
  `~/.bashrc`

To auto `startx` during login, edit `~/.profile`:
```
# Hide startx messages:
if [ -z "$DISPLAY" ] && [ -n "$XDG_VTNR" ] && [ "$XDG_VTNR" -eq 1 ]; then
  exec startx
fi
```

To prevent displaying stuff during login (don't need to see them when auto-starting X):

    if [ ! -f ~/.hushlogin ]; then touch ~/.hushlogin; fi
