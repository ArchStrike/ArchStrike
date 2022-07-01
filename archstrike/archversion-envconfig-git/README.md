# ArchVersion Environment Config

A VCS package for ArchVersion that patches in support for runtime configuration using environment variables.

## Environment Variables

The environment variables that can be set for runtime configuration are:

* `XDG_DIRECTORY`: The directory in $XDG_CONFIG_HOME archversion will start in when looking for files with a relative path (default: **archversion**)
* `CONFIG_PACKAGES`: The file containing archversion package definitions (default: **packages.conf**)
* `CONFIG_SENDMAIL`: The file containing configuration for the sendmail command (default: **sendmail.conf**)
* `CACHE_PACKAGES`: The file containing the package version cache (default: **packages.cache**)

Keep in mind that if you are currently in **/tmp** and want to run archversion using **/tmp/other_packages.conf**, the command `CONFIG_PACKAGES=other_packages.conf archversion` will be trying to use **~/.config/archversion/other_packages.conf** if no other variables are set. Instead, you should set the `CONFIG_PACKAGES` variable using an absolute path like this `CONFIG_PACKAGES=/tmp/other_packages.conf archversion`

## Credits

Released by the [ArchStrike](https://github.com/ArchStrike) team

* Original package and upstream project by [Sébastien Luttringer](https://github.com/seblu)
* Changes to the original package and the environment config patch by [Kevin MacMartin](https://github.com/prurigro)

## License

This package and its contents are released under the GPLv3

