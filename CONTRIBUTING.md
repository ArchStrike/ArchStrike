# Rules for Pull Requests

* **Descriptive titles.** Pull requests must have a title that gives the package name the PR is for, and a short description about the PR.
* **Detailed description.** The body of the PR must contain a detailed description of what changes are being introduced, and most importantly, *why* this PR should be merged.
* **One package per request.** PRs must be for a single package only.  A PR addressing multiple packages without merit risks having a delayed merge or being closed.
* **Squash commits.** Your commits must be meaningful. If you make incremental changes or fixes, they must [be squashed](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#Squashing-Commits) before the pull request will be merged.
* **Check that your changes build.** Your submission must build using the [clean chroot](https://archstrike.org/wiki/contributing/chroot) method on *all* supported architectures that the package is to be built for.  No exceptions.
* **Work within one PR.** Do not close a PR and open another with new changes.  Amend your commit and force push to your branch to update the changes in the pull request.
* Ensure your PR addresses three of the most common problems:
  * Correctly update the pkgver or pkgrel of the package (see below).
  * Update the checksums if external files have been added or modified.
  * Is the package only for specific architectures?  Set the `buildarch` variable (see [the README](https://github.com/ArchStrike/ArchStrike/blob/master/README.md))

**Pull requests that fail to meet these requirements may be summarily closed without response.**

## Submitting new packages

* If the pull request is for a new package, review the [README](https://github.com/ArchStrike/ArchStrike/blob/master/README.md) to ensure the package is going into the correct repository and meets all the stated requirements.

To make sure the `buildarch` variable is correct on your submitted package, please see below.

  (1) = the default, package will be built for all architectures
  (4) = the package will be built only for armv7h
  (8) = the package will be build only for armv8 (AArch64)
  (16) = the package will be built only for armv6h
  (64) = the package will be built only for i686
  (128) = the package will be built only for x86_64
  (192) = the package will be built for x86_64 and i686
  (212) = the package will be built for armv6h, armv7h, i686 and x86_64
  (220) = the package will be built for armv6h, armv7h, armv8, i686 and x86_64

Please note however, that using 1 and 220 is not interchangable. A `buildarch` of 1 means the package has no differences when installing between arches so the same package will be used for all arches, however a `buildarch` of 220 means the package will be built differently for every arch thus having a different package file for each one of them.

## Updating existing packages

* If you changed the PKGBUILD or related files, detail your changes in the comment header at the top. Review the packages in this repository for examples of what this looks like.

* If you are updating an existing package, you need to change the `pkgver` and `pkgrel` variables accordingly.

* For example, if a package has a new version of 3.0 and the old version is 2.0, change the `pkgver` to 3.0 and make sure `pkgrel` is set back to 1.

* If it is not a new version but a different update such as changing something in the PKGBUILD that will effect the build process of the package, bump the `pkgrel` number by 1 and keep `pkgver` the same.

* Ensure that `buildarch` is set correctly (see above).

## Note about -git packages

When adding a package that pulls the source from a git or svn repository, add a `.gitignore` file containing the name of the cloned repository.

* For example, if something-git clones the repository called `something`, then `echo something > .gitignore` and commit the .gitignore file as well.
