# -*- coding: utf-8 -*-

from learn_aws_bedrock import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_aws_bedrock.tests import run_cov_test

    run_cov_test(__file__, "learn_aws_bedrock.api", preview=False)
