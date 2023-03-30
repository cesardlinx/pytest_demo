def test_configuration_is_correct(read_configuration, read_circuit):
    assert read_configuration == {}
    assert read_circuit == {'id': '123'}


def test_optimizer_x_property_is_correct(setup_optimizer):
    assert setup_optimizer.x == 10


def test_everything(setup):
    read_configuration, read_circuit, setup_optimizer = setup
    assert read_configuration == {}

def test_everything2(setup):
    read_configuration, read_circuit, setup_optimizer = setup
    assert read_configuration == {}

def test_everything3(setup):
    read_configuration, read_circuit, setup_optimizer = setup
    assert read_configuration == {}

def test_everything4(setup):
    read_configuration, read_circuit, setup_optimizer = setup
    assert read_configuration == {}
