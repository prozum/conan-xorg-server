#!/usr/bin/env python

from conans import ConanFile, tools, Meson
import os


class XorgServerConan(ConanFile):
    name            = "xorg-server"
    version         = "1.20.3"
    license         = "MIT"
    default_user = "bincrafters"
    default_channel = "stable"
    url             = "https://github.com/prozum/conan-libdrm.git"
    description     = "Direct Rendering Manager headers and kernel modules"
    settings = "os", "arch", "compiler", "build_type"

    def requirements(self):
        pass

    def source(self):
        tools.get("https://github.com/freedesktop/xorg-xserver/archive/xorg-server-%s.tar.gz" % self.version)

    def build(self):
        args = ["--auto-features=disabled"]
        meson = Meson(self)
        meson.configure(source_folder="xorg-xserver-xorg-server-" + self.version, args=args) #, pkg_config_paths=os.environ['PKG_CONFIG_PATH'].split(":"))
        meson.build()
        meson.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.env_info.PKG_CONFIG_PATH.append(os.path.join(self.package_folder, "lib", "pkgconfig"))
