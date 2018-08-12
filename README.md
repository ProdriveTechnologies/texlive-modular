# Modular TeXLive release

[The official tarballs of TeXLive](http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/)
are very large in size; approximately 3.5 GB. Most documents created
using TeXLive only depend on a fraction of this data. This makes the
official tarballs unsuitable for use in automated build processes that
download dependencies on demand (e.g., [Bazel](https://bazel.build/) with its
[LaTeX rules](https://github.com/ProdriveTechnologies/bazel-latex)).

This repository provides a copy of the data stored in the official
tarballs, decomposed into many (> 5000) small archives. The
decomposition is performed automatically, based on the directory
structure of the offical tarballs. Every subtree containing at least one
(non-blacklisted) file is stored in a separate tarball. Tarballs are
named after the path of the subtree, where `/` is substituted with `--`.

# How these tarballs were generated

The official tarballs were downloaded, having the following checksums:

```
0b5657c97ff203bd8fadb28986a167c731db9e7947ff65f6680dda57ca4971b7  texlive-20180414-bin.tar.xz
5b4397854723405f20df7172e73a04cee2d3ab712f78b064a7f523d6ab9f0329  texlive-20180414-extra.tar.xz
bae2fa05ea1858b489f8138bea855c6d65829cf595c1fb219c5d65f4fe8b1fad  texlive-20180414-texmf.tar.xz
```

They were then decomposed and uploaded as follows:

```
for i in bin extra texmf; do
  tar -xf ~/Downloads/texlive-20180414-$i.tar.xz
done
mkdir output
./create_tarballs.py texlive-20180414-bin 
./create_tarballs.py texlive-20180414-extra/tlpkg/TeXLive
./create_tarballs.py texlive-20180414-texmf
(cd output; sha256sum *) > sha256sums-20180414.txt
./upload.sh <GitHub API token> <GitHub release ID>
```

# Licensing

As the files contained in these archives are merely unmodified copies of
the ones provided by TeXLive, please refer to
[the TeXLive page](https://www.tug.org/texlive/copying.html) for
information on licensing.
