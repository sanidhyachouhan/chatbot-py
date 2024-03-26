import os
import io
import json
import pytest
import tempfile
from pathlib import Path
from pytest_httpserver import HTTPServer, URIPattern
from werkzeug.wrappers import Request, Response
from PIL import Image

from ollama._client import Client, AsyncClient


class PrefixPattern(URIPattern):
    def __init__(self, prefix: str):
        self.prefix = prefix

    def match(self, uri):
        return uri.startswith(self.prefix)


def test_client_chat(httpserver: HTTPServer):
    # Test implementation for Client.chat


def test_client_chat_stream(httpserver: HTTPServer):
    # Test implementation for Client.chat with stream


def test_client_chat_images(httpserver: HTTPServer):
    # Test implementation for Client.chat with images


def test_client_generate(httpserver: HTTPServer):
    # Test implementation for Client.generate


def test_client_generate_stream(httpserver: HTTPServer):
    # Test implementation for Client.generate with stream


def test_client_generate_images(httpserver: HTTPServer):
    # Test implementation for Client.generate with images


def test_client_pull(httpserver: HTTPServer):
    # Test implementation for Client.pull


def test_client_pull_stream(httpserver: HTTPServer):
    # Test implementation for Client.pull with stream


def test_client_push(httpserver: HTTPServer):
    # Test implementation for Client.push


def test_client_push_stream(httpserver: HTTPServer):
    # Test implementation for Client.push with stream


def test_client_create_path(httpserver: HTTPServer):
    # Test implementation for Client.create with path


def test_client_create_path_relative(httpserver: HTTPServer):
    # Test implementation for Client.create with relative path


def test_client_create_path_user_home(httpserver: HTTPServer, userhomedir):
    # Test implementation for Client.create with user home directory


def test_client_create_modelfile(httpserver: HTTPServer):
    # Test implementation for Client.create with model file


def test_client_create_modelfile_roundtrip(httpserver: HTTPServer):
    # Test implementation for Client.create with model file roundtrip


def test_client_create_from_library(httpserver: HTTPServer):
    # Test implementation for Client.create from library


def test_client_create_blob(httpserver: HTTPServer):
    # Test implementation for Client.create blob


def test_client_create_blob_exists(httpserver: HTTPServer):
    # Test implementation for Client.create blob exists


@pytest.fixture
def userhomedir():
    # Fixture for user home directory


@pytest.mark.asyncio
async def test_async_client_chat(httpserver: HTTPServer):
    # Test implementation for AsyncClient.chat


@pytest.mark.asyncio
async def test_async_client_chat_stream(httpserver: HTTPServer):
    # Test implementation for AsyncClient.chat with stream


@pytest.mark.asyncio
async def test_async_client_chat_images(httpserver: HTTPServer):
    # Test implementation for AsyncClient.chat with images


@pytest.mark.asyncio
async def test_async_client_generate(httpserver: HTTPServer):
    # Test implementation for AsyncClient.generate


@pytest.mark.asyncio
async def test_async_client_generate_stream(httpserver: HTTPServer):
    # Test implementation for AsyncClient.generate with stream


@pytest.mark.asyncio
async def test_async_client_generate_images(httpserver: HTTPServer):
    # Test implementation for AsyncClient.generate with images


@pytest.mark.asyncio
async def test_async_client_pull(httpserver: HTTPServer):
    # Test implementation for AsyncClient.pull


@pytest.mark.asyncio
async def test_async_client_pull_stream(httpserver: HTTPServer):
    # Test implementation for AsyncClient.pull with stream


@pytest.mark.asyncio
async def test_async_client_push(httpserver: HTTPServer):
    # Test implementation for AsyncClient.push


@pytest.mark.asyncio
async def test_async_client_push_stream(httpserver: HTTPServer):
    # Test implementation for AsyncClient.push with stream


@pytest.mark.asyncio
async def test_async_client_create_path(httpserver: HTTPServer):
    # Test implementation for AsyncClient.create with path


@pytest.mark.asyncio
async def test_async_client_create_path_relative(httpserver: HTTPServer):
    # Test implementation for AsyncClient.create with relative path


@pytest.mark.asyncio
async def test_async_client_create_path_user_home(httpserver: HTTPServer, userhomedir):
    # Test implementation for AsyncClient.create with user home directory


@pytest.mark.asyncio
async def test_async_client_create_modelfile(httpserver: HTTPServer):
    # Test implementation for AsyncClient.create with model file


@pytest.mark.asyncio
async def test_async_client_create_modelfile_roundtrip(httpserver: HTTPServer):
    # Test implementation for AsyncClient.create with model file roundtrip


@pytest.mark.asyncio
async def test_async_client_create
