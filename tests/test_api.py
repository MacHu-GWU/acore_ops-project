# -*- coding: utf-8 -*-

from acore_ops import api


def test():
    _ = api


if __name__ == "__main__":
    from acore_ops.tests import run_cov_test

    run_cov_test(__file__, "acore_ops.api", preview=False)
