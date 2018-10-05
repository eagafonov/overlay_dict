import pytest
from overlay_dict import overlay_dict


@pytest.fixture
def od():
    return overlay_dict()


class TestGetItems:
    def test_01(self, od):
        od[42] = 'foo'

        assert od[42] == 'foo'

        assert od._layers == [{42: 'foo'}]

        od.push_layer()

        assert od._layers == [{42: 'foo'}, {}]

        # assert od[42] == 'foo'

    def test_multi_layer(self, od):
        od['foo'] = 1
        od.push_layer()
        od['foo'] = 2

        od.push_layer()
        od['foo'] = 3

        assert od._layers == [{'foo': 1},
                              {'foo': 2},
                              {'foo': 3}]

        assert od['foo'] == 3

        od.pop_layer()
        assert od['foo'] == 2

        od.pop_layer()
        assert od['foo'] == 1

    def test_multi_layer_02(self, od):
        od['one'] = 1
        od.push_layer()
        od['two'] = 2

        od.push_layer()
        od['three'] = 3

        assert od['one'] == 1
        assert od['two'] == 2
        assert od['three'] == 3

    def test_key_error_empty(self, od):
        with pytest.raises(KeyError) as e:
            od[42]

        assert e.value.args == (42,)

    def test_key_error_single_layer(self, od):
        od['foo'] = 'bar'

        with pytest.raises(KeyError) as e:
            od[42]

        assert e.value.args == (42,)

    def test_key_error_multi_layer_01(self, od):
        od['foo'] = 'bar'
        od.push_layer()

        with pytest.raises(KeyError) as e:
            od[42]

        assert e.value.args == (42,)

    def test_key_error_multi_layer_02(self, od):
        od['foo'] = 'bar'
        od.push_layer()
        od['bar'] = 'foo'

        with pytest.raises(KeyError) as e:
            od[42]

        assert e.value.args == (42,)
