import click
from pyfiglet import Figlet
from tabulate import tabulate
import os
import sys
import socket

def ipAddressParse():
    formatInt = ""
    interfaces = socket.if_nameindex()
    for i in interfaces:
        formatInt += (i[1]) + ", "
    return formatInt


@click.command()
def sysdetails():
    f = Figlet(font='standard')
    click.echo(f.renderText("System Details"))
    click.echo("=============================================================")
    click.echo("System Details will give you all the details of your system.")
    click.echo("=============================================================")

    osHostname = os.uname()[1]
    osPlatform = os.uname()[0]
    architecture = os.uname()[4]
    kernelVersion = "{} {}".format(osPlatform, os.uname()[2])
    ipAddress = ipAddressParse()

    table = [
        ["Hostname", osHostname],
        ["Platform", osPlatform],
        ["Architecture", architecture],
        ["Kernel", kernelVersion],
        ["IP", ipAddress]
    ]

    print(tabulate(table, '', tablefmt="fancy_grid"))


if __name__=='__main__':
    sysdetails()
