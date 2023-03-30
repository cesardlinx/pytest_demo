import json
import pytest

from optimizer import Optimizer

"""
The fixtures are going to replace your setup
the fixtures can be the setup or input to any of your tests
"""

@pytest.fixture
def read_configuration():
    """reads the analsysis configuration"""
    with open("configuration.json") as f:
        config = json.load(f)
    return config


@pytest.fixture
def read_circuit():
    """reads the circuit"""
    with open("circuit.json") as f:
        config = json.load(f)
    return config

@pytest.fixture
def setup_optimizer():
    """instantiates and setups the optimizer object"""
    optimizer = Optimizer()
    optimizer.x = 30
    return optimizer


@pytest.fixture
def setup(read_configuration, read_circuit, setup_optimizer):
    return (read_configuration, read_circuit, setup_optimizer)

