# -*- coding: utf-8 -*-

"""
Advanced sub command example.

- Class = top level command
- Attribute, it is an instance of another class = sub command
- Method in other classes = sub command of sub command
"""

import typing as T
import fire


class S3:
    """
    AWS S3 sub command
    """

    def ls(self):
        """
        List s3 buckets
        """
        print("run: aws s3 ls")


class EC2:
    """
    AWS EC2 sub command
    """

    def list_instances(self):
        """
        List ec2 instances
        """
        print("run: aws ec2 list-instances")

    def list_vpcs(self):
        """
        List ec2 vpc
        """
        print("run: aws ec2 list-vpcs")


class AWS:
    """
    AWS CLI class doc string
    """

    def __init__(self):
        self.s3 = S3()
        self.ec2 = EC2()

    def __call__(self, version: T.Optional[bool] = False):
        """
        AWS CLI
        """
        if version:
            print("0.0.1")
        else:
            print("run: aws")


if __name__ == "__main__":
    fire.Fire(AWS())
