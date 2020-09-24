from mamba import description, before, context, it, _it
from expects import expect, equal, raise_error
from unittest.mock import MagicMock, Mock, patch, AsyncMock, call
import asyncio

from bunnyplot.rabbitmq import RabbitMQApi

with description(RabbitMQApi) as self:
    with before.each:
        self.api = RabbitMQApi("http://localhost", "test_username", "test_password")

    with description("#get_definitions"):
        with _it("should make a get request to /api/definitions"):
            pass
        with _it("should authorize using the correct Basic credentials"):
            pass
    
    with description("#get_consumers"):
        with _it("should make a get request to /api/consumers"):
            pass
        with _it("should authorize using the correct Basic credentials"):
            pass
        