# This is non-functional at the moment.  Needs to be tweaked to
# work on OSX and Ubuntu.  I have no NixOS install to test
# against.
with import <nixpkgs> {}; {
  python3Env = stdenv.mkDerivation rec {
    name = "python3-env";
    version = "0.1";
    src = ./.;
    buildInputs = [
      git
      libxml2
      libxslt
      libzip
      zlib
      stdenv
      python35
      python35Packages.pip
      python35Packages.virtualenv
    ];

    pathsToLink = [ "/include" ];
  };
}
