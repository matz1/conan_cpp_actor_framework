from pathlib import Path
from conans import ConanFile, CMake, tools

class ActorFramework(ConanFile):
    name="actorframework"
    description="c++ actor framework"
    version="1.0.0"
    homepage="https://www.actor-framework.org"
    generators="cmake", "virtualenv"
    settings="os", "arch", "compiler", "build_type"
    exports_sources="*"
    sources_name="actor-framework-0.17.4"

    def source(self):
        tools.get("https://github.com/actor-framework/actor-framework/archive/0.17.4.tar.gz")
 
    def package_info(self):
        self.cpp_info.libs = []
        self.cpp_info.libs.extend(["caf_io", "caf_core", "caf_openssl"])

    def build(self):
        cmake = CMake(self)
        cmake.configure(
          source_dir=str(Path(self.source_folder) / self.sources_name)
        )
        cmake.build()
        cmake.install()

