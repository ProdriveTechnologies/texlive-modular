#!/usr/bin/env python3

import os
import stat
import subprocess
import sys

IGNORED_DIRECTORIES = set(["doc", "source"])
IGNORED_FILES = set(
    [
        "README",
        "context-version.pdf",
        "context-version.png",
        "context.rme",
        "ls-R",
        "times.htf",
    ]
)


def collect_files(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        sb = os.lstat(full_path)
        if stat.S_ISDIR(sb.st_mode):
            if entry not in IGNORED_DIRECTORIES:
                for subentry in collect_files(full_path):
                    yield os.path.join(entry, subentry)
        elif stat.S_ISREG(sb.st_mode):
            if entry not in IGNORED_FILES:
                yield entry
        elif not stat.S_ISLNK(sb.st_mode):
            raise Exception("Found non-directory/file/symlink: " + full_path)


def create_tarballs(path):
    # Obtain files and directories at this point.
    directories = []
    files = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        sb = os.lstat(full_path)
        if stat.S_ISDIR(sb.st_mode):
            if entry not in IGNORED_DIRECTORIES:
                directories.append(entry)
        elif stat.S_ISREG(sb.st_mode):
            if entry not in IGNORED_FILES:
                files.append(entry)
        elif not stat.S_ISLNK(sb.st_mode):
            raise Exception("Found non-directory/file/symlink: " + full_path)

    if files:
        for directory in directories:
            for entry in collect_files(os.path.join(path, directory)):
                files.append(os.path.join(directory, entry))
        if len(files) > (3500 if directories else 5000):
            raise Exception(
                "Package %s is too large. It has %d files." % (path, len(files))
            )

        subprocess.check_call(
            [
                "tar",
                "-C",
                path,
                "--mtime=0",
                "--owner=0",
                "--group=0",
                "--numeric-owner",
                "-cJf",
                os.path.join("output", "--".join(path.split("/")) + ".tar.xz"),
            ]
            + sorted(files)
        )
    else:
        for entry in directories:
            create_tarballs(os.path.join(path, entry))


create_tarballs(sys.argv[1])
