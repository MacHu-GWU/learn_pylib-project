# -*- coding: utf-8 -*-


from .boto_ses import boto_ses_factory, bsm


def print_boto_ses_factory_bsm():
    print(f"{boto_ses_factory.bsm = }")


def print_bsm():
    print(f"{bsm = }")
