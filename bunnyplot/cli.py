import asyncio
import click
import logging

import bunnyplot.log
from bunnyplot.graph import build_rabbitmq_graph
from bunnyplot.rabbitmq import RabbitMQApi

logger = logging.getLogger("bunnyplot")


@click.command()
@click.argument("url", envvar="BUNNYPLOT_URL")
@click.argument("output_path", envvar="BUNNYPLOT_OUTPUT")
@click.option(
    "--username", "-u", prompt=True, hide_input=True, envvar="BUNNYPLOT_USERNAME"
)
@click.option(
    "--password", "-p", prompt=True, hide_input=True, envvar="BUNNYPLOT_PASSWORD"
)
def cli(url, output_path, username, password):
    async def main():
        api = RabbitMQApi(url, username, password)

        logger.info("fetching data...")
        consumers, definitions = await asyncio.gather(
            api.get_consumers(), api.get_definitions()
        )

        graph = build_rabbitmq_graph(consumers, definitions)

        logger.info(nx.info(graph))

        logger.info("writing to %s", output_path)
        nx.write_graphml(graph, output_path)

    asyncio.run(main())


if __name__ == "__main__":
    cli()
