import os
import subprocess
import click

@click.command()
@click.option('-d', '--dir', default = '.', type = 'str', help= 'Target Path to Scan')
def run(dir):
    is_git = _walk_dir(dir)
    if is_git:
        _run_git_commands()

if __name__ == 'main':
    run()


def _walk_dir(dir):
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isdir(f) and filename.basename == '.git':
            return True
    return False

def _run_git_commands():
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])