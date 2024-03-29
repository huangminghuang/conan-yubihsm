#!/usr/bin/env python
# -*- coding: utf-8 -*-


from cpt.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager(build_policy="missing")
    builder.add_common_builds(pure_c=True)
    builder.run()