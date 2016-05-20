# Getting the Environment Up.

*The Nix environment is verified on OSX El Capitan and Ubuntu 16.04, but it should also work in NixOS 16*

- Install Nix package manager (skip this step if you already have it installed)
  - `curl https://nixos.org/nix/install | sh`
- `nix-shell .`
  - You may add `--command "other-shell"` to run another shell, like `nix-shell . --command zsh`
  - The first time you ever run `nix-shell .` on any project, especially in OSX, it will take a bit on OSX because all
    the standard libraries will need to be built.  After this, though, running dev environments should go much quicker,
    and subsequent nix-shell instantiations for the same dev environments should be instantaneous.
- `virtualenv --python=python3 venv`
- `which pip` and then `cp <location of pip> venv/bin/pip`
  - The reason for the above is that it's currently not possible to upgrade Pip from within Nix using Pip, so you have
    to copy the latest Pip over yourself.
- `source venv/bin/activate`
- `pip install --target=venv/lib/python3.5/site-packages -r requirements.txt`
