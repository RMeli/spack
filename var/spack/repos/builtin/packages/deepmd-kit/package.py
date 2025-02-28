# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class DeepmdKit(CMakePackage, CudaPackage, ROCmPackage):
    """DeepMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics."""

    homepage = "https://docs.deepmodeling.com/projects/deepmd/"

    url = "https://github.com/deepmodeling/deepmd-kit/archive/refs/tags/v0.0.0.zip"

    maintainers("RMeli")

    license("LGPL-3.0-only", checked_by="RMeli")

    version("3.0.1", sha256="80ef01a93802cb14da3916f1901fbd5fa06577cca5212dc777c7fdd7c5445ebd")

    # TODO: Add TF and  JAX
    variant("backend", values=("pytorch",), description="Deep learning backend", default="pytorch")

    root_cmakelists_dir = "source"

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("git", type="build")
    depends_on("cuda", when="+cuda")

    depends_on("hip", when="+rocm")
    depends_on("hipcub", when="+rocm")

    depends_on("py-torch", when="backend=pytorch")

    def cmake_args(self):
        args = [
            self.define("ENABLE_PYTORCH", self.spec.satisfies("backend=pytorch")),
            self.define_from_variant("USE_CUDA_TOOLKIT", "cuda"),
            self.define_from_variant("USE_ROCM_TOOLKIT", "rocm"),
        ]
        return args
