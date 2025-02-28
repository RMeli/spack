# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Vesin(CMakePackage):
    """Vesin: fast neighbor lists for atomistic systems"""

    homepage = "https://luthaf.fr/vesin/latest/index.html"
    url = "https://github.com/Luthaf/vesin/archive/refs/tags/v0.3.2.tar.gz"
    git = "https://github.com/Luthaf/vesin.git"

    maintainers("RMeli")

    license("BSD-3-Clause", checked_by="RMeli")

    version("0.3.2", sha256="33ce057747ba92785ef9f05ee682e50824993a2dc52c6353ebbbbb64fc93139a")

    variant("pytorch", default=False, description="Enable PyTorch support")
    variant("shared", default=False, description="Build shared libraries")

    depends_on("cxx", type="build")

    depends_on("py-torch", when="+pytorch")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("VESIN_TORCH", "pytorch"),
            self.define("VESIN_BUILD_TESTS", self.run_tests),
        ]
        return args
