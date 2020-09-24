from mamba import description, before, context, it, _it
from expects import expect, equal, raise_error
from unittest.mock import MagicMock, Mock, patch, AsyncMock, call
from click.testing import CliRunner
import asyncio

from bunnyplot.cli import cli

with description(cli) as self:
    with before.all:
        self.loop = asyncio.get_event_loop()

    with before.each:
        self.runner = CliRunner()

    with after.all:
        self.loop.close()