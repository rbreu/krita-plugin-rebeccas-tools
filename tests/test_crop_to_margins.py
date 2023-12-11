from unittest.mock import MagicMock, patch


@patch.dict('sys.modules', krita=MagicMock())
def test_get_crop_values_with_four_guides():
    from plugin.rebeccas_tools.crop_to_margins import get_crop_values
    doc = MagicMock(
        width=MagicMock(return_value=200),
        height=MagicMock(return_value=400),
        horizontalGuides=MagicMock(return_value=[100, 350]),
        verticalGuides=MagicMock(return_value=[3, 177]))

    assert get_crop_values(doc) == (3, 100, 174, 250)


@patch.dict('sys.modules', krita=MagicMock())
def test_get_crop_values_ignores_guides_order():
    from plugin.rebeccas_tools.crop_to_margins import get_crop_values
    doc = MagicMock(
        width=MagicMock(return_value=200),
        height=MagicMock(return_value=400),
        horizontalGuides=MagicMock(return_value=[350, 100]),
        verticalGuides=MagicMock(return_value=[177, 3]))

    assert get_crop_values(doc) == (3, 100, 174, 250)


@patch.dict('sys.modules', krita=MagicMock())
def test_get_crop_values_ignores_additional_inner_guides():
    from plugin.rebeccas_tools.crop_to_margins import get_crop_values
    doc = MagicMock(
        width=MagicMock(return_value=200),
        height=MagicMock(return_value=400),
        horizontalGuides=MagicMock(return_value=[350, 200, 100]),
        verticalGuides=MagicMock(return_value=[177, 50, 3]))

    assert get_crop_values(doc) == (3, 100, 174, 250)


@patch.dict('sys.modules', krita=MagicMock())
def test_get_crop_values_ignores_guides_out_of_bounds():
    from plugin.rebeccas_tools.crop_to_margins import get_crop_values
    doc = MagicMock(
        width=MagicMock(return_value=200),
        height=MagicMock(return_value=400),
        horizontalGuides=MagicMock(return_value=[350, 100, -1, 500]),
        verticalGuides=MagicMock(return_value=[177, 3, -10, 440]))

    assert get_crop_values(doc) == (3, 100, 174, 250)


@patch.dict('sys.modules', krita=MagicMock())
def test_get_crop_values_not_enough_vertical_guides():
    from plugin.rebeccas_tools.crop_to_margins import get_crop_values
    doc = MagicMock(
        width=MagicMock(return_value=200),
        height=MagicMock(return_value=400),
        horizontalGuides=MagicMock(return_value=[350, 100]),
        verticalGuides=MagicMock(return_value=[177]))

    assert get_crop_values(doc) is None


@patch.dict('sys.modules', krita=MagicMock())
def test_get_crop_values_not_enough_horizontal_guides():
    from plugin.rebeccas_tools.crop_to_margins import get_crop_values
    doc = MagicMock(
        width=MagicMock(return_value=200),
        height=MagicMock(return_value=400),
        horizontalGuides=MagicMock(return_value=[350]),
        verticalGuides=MagicMock(return_value=[177, 3]))

    assert get_crop_values(doc) is None
