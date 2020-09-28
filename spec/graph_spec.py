from mamba import description, before, context, it, _it
from expects import expect, equal, raise_error
from unittest.mock import MagicMock, Mock, patch, AsyncMock, call

from bunnyplot.graph import build_rabbitmq_graph

with description(build_rabbitmq_graph) as self:
    with _it("should build a DiGraph"):
        pass

    with _it("should contain the correct nodes and edges"):
        pass