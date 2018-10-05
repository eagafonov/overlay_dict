from overlay_dict import overlay_dict


class TestConstuctors:
    def test_default(self):
        od = overlay_dict()

        assert od._layers == [{}]
