import os
from typing import Optional

import click
from click import Command

plugin_folder = os.path.join(os.path.dirname(__file__), "commands")


class MyCLI(click.MultiCommand):
    def list_commands(self, ctx) -> list:

        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                rv.append(filename[:-3])
        rv.sort()
        print(type(rv))
        return rv

    def get_command(self, ctx, name) -> Optional[Command]:
        ns: dict = {}
        fn = os.path.join(plugin_folder, name + ".py")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
        return ns["cli"]


@click.command(cls=MyCLI)
def cli() -> None:
    pass


if __name__ == "__main__":
    cli()
