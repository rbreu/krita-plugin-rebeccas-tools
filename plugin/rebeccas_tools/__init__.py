import os

import krita
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from .reorder_image_sequence import reorder
from .crop_to_margins import get_crop_values


class RebeccasToolsExtension(krita.Extension):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(
            'rebeccas_tools_reorder_image_sequence',
            'Reorder Image Sequence...',
            'tools/scripts')
        action.triggered.connect(self.reorder_image_sequence)

        action = window.createAction(
            'rebeccas_tools_crop_to_margins',
            'Crop To Margins',
            'tools/scripts')
        action.triggered.connect(self.crop_to_margins)

    def reorder_image_sequence(self):
        folder = QFileDialog.getExistingDirectory(
            self.parent.activeWindow().qwindow(),
            i18n('Krita Recorder Folder'),
            os.path.expanduser('~'),
        )
        reorder(folder)

    def crop_to_margins(self):
        doc = Application.activeDocument()
        if not doc:
            QMessageBox.warning(
                self.parent.activeWindow().qwindow(),
                i18n('Error'),
                i18n('No document selected.'))
            return

        args = get_crop_values(doc)

        if args is None:
            QMessageBox.warning(
                self.parent.activeWindow().qwindow(),
                i18n('Error'),
                i18n('At least two vertical and two horizantal guides'
                     ' required.'))
            return

        doc.crop(*args)
        doc.waitForDone()


krita_instance = krita.Krita.instance()
krita_instance.addExtension(RebeccasToolsExtension(krita_instance))
