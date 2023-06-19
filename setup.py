import os
from setuptools import setup


def add_to_bashrc():
    project_path = os.getcwd()
    bashrc_path = os.path.expanduser("~/.bashrc")
    line = f'alias poach="python {project_path}/src/poach/main.py"'

    with open(bashrc_path, "a") as f:
        f.write(f"\n# Added by poach library setup.py\n{line}\n")


def install_requirements():
    requirements_path = os.path.join(os.getcwd(), "requirements.txt")
    os.system(f"pip install -r {requirements_path}")


if __name__ == "__main__":
    add_to_bashrc()
    install_requirements()

    setup(
        name="poach",
        version="1.0",
        packages=[],
        scripts=[],
    )
