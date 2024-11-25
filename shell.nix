{ pkgs ? import <nixpkgs> {}}:
let
  fhs = pkgs.buildFHSUserEnv {
    name = "sphinx";

    targetPkgs = pkgs: (with pkgs; [
      micromamba
      #python3.pkgs.pyside6
      python3.pkgs.requests
      python3.pkgs.pip
      python3.pkgs.sphinx
      stdenv.cc xorg.libSM xorg.libICE xorg.libX11 xorg.libXau xorg.libXi xorg.libXrender libselinux libGL zlib xorg.libXcursor
    ]);

    profile = ''
      set -e
      eval "$(micromamba shell hook --shell=posix)"
      export MAMBA_ROOT_PREFIX=~/micromamba
      micromamba activate scqubits
      set +e
    '';
  };
in fhs.env