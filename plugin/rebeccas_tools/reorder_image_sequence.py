import glob
import os


START = 1


def reorder(folder):

    def get_filename(number):
        return os.path.join(folder, f'{number:07}{extension}')

    fnames = os.listdir(folder)
    fnames.sort()
    last, extension = os.path.splitext(fnames[-1])

    # Sanity check: Only allow same file extensions on all files
    pattern = os.path.join(folder, f'*{extension}')
    assert len(fnames) == len(glob.glob(pattern)), 'Found mixed file types'

    last = int(last)
    prev = START

    print('Reorder Image Sequence: %s to %s...' % (get_filename(prev),
                                                   get_filename(last)))

    for i in range(START, last + 1):
        if os.path.exists(get_filename(i)):
            if prev < i:
                os.rename(get_filename(i), get_filename(prev))
            prev += 1

    print('Reorder Image Sequence: Done')
    return len(fnames)
