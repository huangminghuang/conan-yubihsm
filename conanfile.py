from conans import ConanFile, CMake, tools
import os

class YubihsmConan(ConanFile):
    name = "yubihsm"
    version = "2.0.1"
    description = "C library to expose low- and high-level functions to interact with a YubiHSM"
    topics = ("conan", "libyubihsm")
    url = "http://github.com/huangminghuang/conan-yubihsm"
    homepage = "https://github.com/Yubico/yubihsm-shell"
    author = "Huang-Ming Huang <huangh@objectcomputing.com>"
    license = "Apache"
    exports_sources = ["package.patch"]
    settings = "os", "compiler", "arch", "build_type"
    
    options = {"shared": [True, False]}
    default_options = "shared=False"
    
    requires = 'OpenSSL/1.1.1c@conan/stable','libcurl/7.64.1@bincrafters/stable','libusb/1.0.22@bincrafters/stable'
    generators = "cmake"
    no_copy_source = True
    build_policy = "missing"
    
    def configure(self):
        # Because this is pure C
        del self.settings.compiler.libcxx
        # self.options["libusb"].enable_udev = False
            
    def source(self):
        tools.get("https://github.com/Yubico/yubihsm-shell/archive/{0}.tar.gz".format(self.version))
        extracted_dir = "yubihsm-shell-{0}".format(self.version)
        os.rename(extracted_dir, "sources")
        # This avoids using the system providied dependencies.
        tools.patch(base_path='sources', patch_file="package.patch")
    
        
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_STATIC"] = "OFF" if self.options.shared else "ON"
        cmake.definitions["BUILD_ONLY_LIB"] = "ON"
        cmake.configure(source_dir=os.path.join(self.source_folder,"sources"))
        return cmake

    def build(self):
        self._configure_cmake().build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="sources")
        CMake(self).install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
            

