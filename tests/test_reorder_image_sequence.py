import os
from unittest.mock import MagicMock, patch


@patch.dict('sys.modules', krita=MagicMock())
def test_reorders_jpgs(tmpdir):
    from plugin.rebeccas_tools.reorder_image_sequence import reorder

    with open(os.path.join(tmpdir, '0000001.jpg'), 'w') as f:
        f.write('a')

    with open(os.path.join(tmpdir, '0000003.jpg'), 'w') as f:
        f.write('b')

    with open(os.path.join(tmpdir, '0000006.jpg'), 'w') as f:
        f.write('c')

    reorder(tmpdir)

    with open(os.path.join(tmpdir, '0000001.jpg')) as f:
        assert f.read() == 'a'

    with open(os.path.join(tmpdir, '0000002.jpg')) as f:
        assert f.read() == 'b'

    with open(os.path.join(tmpdir, '0000003.jpg')) as f:
        assert f.read() == 'c'


@patch.dict('sys.modules', krita=MagicMock())
def test_reorders_when_first_missing(tmpdir):
    from plugin.rebeccas_tools.reorder_image_sequence import reorder

    with open(os.path.join(tmpdir, '0000002.jpg'), 'w') as f:
        f.write('a')

    with open(os.path.join(tmpdir, '0000003.jpg'), 'w') as f:
        f.write('b')

    with open(os.path.join(tmpdir, '0000004.jpg'), 'w') as f:
        f.write('c')

    reorder(tmpdir)

    with open(os.path.join(tmpdir, '0000001.jpg')) as f:
        assert f.read() == 'a'

    with open(os.path.join(tmpdir, '0000002.jpg')) as f:
        assert f.read() == 'b'

    with open(os.path.join(tmpdir, '0000003.jpg')) as f:
        assert f.read() == 'c'


@patch.dict('sys.modules', krita=MagicMock())
def test_reorders_pngs(tmpdir):
    from plugin.rebeccas_tools.reorder_image_sequence import reorder

    with open(os.path.join(tmpdir, '0000001.png'), 'w') as f:
        f.write('a')

    with open(os.path.join(tmpdir, '0000003.png'), 'w') as f:
        f.write('b')

    with open(os.path.join(tmpdir, '0000006.png'), 'w') as f:
        f.write('c')

    reorder(tmpdir)

    with open(os.path.join(tmpdir, '0000001.png')) as f:
        assert f.read() == 'a'

    with open(os.path.join(tmpdir, '0000002.png')) as f:
        assert f.read() == 'b'

    with open(os.path.join(tmpdir, '0000003.png')) as f:
        assert f.read() == 'c'
