# Modular TeXLive release

[The official tarballs of TeXLive](http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2022/)
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

The official tarballs were downloaded, having the following sha256 checksums:

```
00e0d3db152affbfe695016c29c7ecc2ed345efaaeb93b55ac016fda3c66ba8c  texlive-20220321-bin.tar.xz
0284cf368947be8cc7becd61c816432a7d301db3c1e682ddc0a180bd3b6d9296  texlive-20220321-extra.tar.xz
372b2b07b1f7d1dd12766cfc7f6656e22c34a5a20d03c1fe80510129361a3f16  texlive-20220321-texmf.tar.xz
```

They were then decomposed and uploaded as follows:

```
for i in bin extra texmf; do
  tar -xf ~/Downloads/texlive-20220321-$i.tar.xz
done
mkdir output
./create_tarballs.py texlive-20220321-bin
./create_tarballs.py texlive-20220321-extra/tlpkg/TeXLive
./create_tarballs.py texlive-20220321-texmf
(cd output; ls | xargs sha256) > sha256sums-20190410.txt
./upload.sh <GitHub API token> <GitHub release ID>
```

# Licensing

As the files contained in these archives are merely unmodified copies of
the ones provided by TeXLive, please refer to
[the TeXLive page](https://www.tug.org/texlive/copying.html) for
information on licensing.
