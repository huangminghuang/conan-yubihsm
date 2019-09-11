## Package Status

| Bintray | Linux & macOS |
|:--------:|:---------:|:-----------------:|
|[![Download](https://api.bintray.com/packages/huangminghuang/conan/yubihsm%3Ahuangminghuang/images/download.svg) ](https://bintray.com/huangminghuang/conan/yubihsm%3Ahuangminghuang/_latestVersion)|[![Build Status](https://travis-ci.com/huangminghuang/conan-yubihsm.svg?branch=master)](https://travis-ci.com/huangminghuang/conan-yubihsm)|


## Basic setup

    $ conan remote add huang https://api.bintray.com/conan/huangminghuang/conan 
    $ conan install yubihsm/2.0.1@huangminghuang/stable
    
## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    yubihsm/2.0.1@huangminghuang/stable

    [options]
    yubihsm:shared=False
    
    [generators]
    cmake


Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* from the *cmake* generator with all the paths and variables that you need to link with your dependencies.

## CMake setup

*CMakeLists.txt*

    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup(TARGETS)

    add_executable(example example.c)
    target_link_libraries(example CONAN_PKG::yubihsm)
  
```bash
$ mkdir build && cd build
$ conan install ..
$ cmake .. -DCMAKE_BUILD_TYPE=Release
$ cmake --build .
```

