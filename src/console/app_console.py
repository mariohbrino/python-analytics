import click

from commands.find_data import find_data
from commands.get_data import get_data
from commands.group_by_data import group_by_data
from commands.order_by_data import order_by_data


@click.group(name="analytics", help="Analytics CLI Example")
def app_console() -> None:
    pass


app_console.add_command(get_data)
app_console.add_command(find_data)
app_console.add_command(group_by_data)
app_console.add_command(order_by_data)
