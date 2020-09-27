import asyncio
import click
import bunnyplot.log
from bunnyplot.rabbitmq import RabbitMQApi
from base64 import b64encode

@click.command()
@click.option('--password', "-p", prompt=True, hide_input=True, envvar="BUNNYPLOT_PASSWORD")
@click.option('--username', "-u", prompt=True, hide_input=True, envvar="BUNNYPLOT_USERNAME")
@click.argument("output_path", envvar="BUNNYPLOT_OUTPUT")
@click.argument("url", envvar="BUNNYPLOT_URL")
def cli(url, output_path, username, password):
    async def main():
        authorization = b64encode(f"Basic {username}:{password}".encode()).decode()
        api = RabbitMQApi(url, authorization)

        consumers, definitions = await asyncio.gather(api.get_consumers(), api.get_definitions())

        print(consumers)
        print(definitions)

    asyncio.run(main())




if __name__ == "__main__":
    cli()