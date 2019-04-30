# Modular TeXLive release

[The official tarballs of TeXLive](http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2019/)
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
571a9b681ef85b7b5de5ead5c655ab1a1f5f366207a6761423b11f78e73d7d1d  texlive-20190410-bin.tar.xz
488233d728b274952f7770e24f4a0cfa6976cd15dec44951d8985a629570cc8e  texlive-20190410-extra.tar.xz
c2ec974abc98b91995969e7871a0b56dbc80dd8508113ffcff6923e912c4c402  texlive-20190410-texmf.tar.xz
```

They were then decomposed and uploaded as follows:

```
for i in bin extra texmf; do
  tar -xf ~/Downloads/texlive-20190410-$i.tar.xz
done
mkdir output
./create_tarballs.py texlive-20190410-bin
./create_tarballs.py texlive-20190410-extra/tlpkg/TeXLive
./create_tarballs.py texlive-20190410-texmf
(cd output; ls | xargs sha256) > sha256sums-20190410.txt
./upload.sh <GitHub API token> <GitHub release ID>
```

# Licensing

As the files contained in these archives are merely unmodified copies of
the ones provided by TeXLive, please refer to
[the TeXLive page](https://www.tug.org/texlive/copying.html) for
information on licensing.
