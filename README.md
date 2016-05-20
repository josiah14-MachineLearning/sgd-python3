# Getting the Environment Up.

- Install Nix package manager
  - `curl https://nixos.org/nix/install | sh`
- `nix-shell .`
- `virtualenv venv`
- `which pip` and then `cp <location of pip> venv/bin/pip`
  - The reason for the above is that it's currently not possible to upgrade Pip from within Nix using Pip, so you have
    to copy the latest Pip over yourself.
- `source venv/bin/activate`
- `sudo -H pip install -r requirements.txt`
