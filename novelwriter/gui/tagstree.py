"""
novelWriter – GUI Tags Tree
===========================

File History:
Created: 2024-07-21 [2.6b1] GuiTagsView

This file is a part of novelWriter
Copyright 2018–2024, Veronica Berglyd Olsen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
from __future__ import annotations

import logging

from PyQt5.QtWidgets import QHBoxLayout, QLabel, QTreeWidget, QVBoxLayout, QWidget

from novelwriter import CONFIG, SHARED
from novelwriter.types import QtSizeExpanding

logger = logging.getLogger(__name__)


class GuiTagsView(QWidget):

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

        # Build GUI
        self.tagsTree = GuiTagsTree(self)
        self.tagsBar = GuiTagsToolBar(self)

        # Assemble
        self.outerBox = QVBoxLayout()
        self.outerBox.addWidget(self.tagsBar, 0)
        self.outerBox.addWidget(self.tagsTree, 1)
        self.outerBox.setContentsMargins(0, 0, 0, 0)
        self.outerBox.setSpacing(0)

        self.setLayout(self.outerBox)

        return

    def setTreeFocus(self) -> None:
        """Set the focus to the tree widget."""
        self.tagsTree.setFocus()
        return

    def treeHasFocus(self) -> bool:
        """Check if the tags tree has focus."""
        return self.tagsTree.hasFocus()


class GuiTagsToolBar(QWidget):

    def __init__(self, tagsView: GuiTagsView) -> None:
        super().__init__(parent=tagsView)

        logger.debug("Create: GuiTagsToolBar")

        self.tagsView = tagsView

        mPx = CONFIG.pxInt(2)

        self.setContentsMargins(0, 0, 0, 0)
        self.setAutoFillBackground(True)

        # Widget Label
        self.viewLabel = QLabel(self.tr("Project Tags"), self)
        self.viewLabel.setFont(SHARED.theme.guiFontB)
        self.viewLabel.setContentsMargins(0, 0, 0, 0)
        self.viewLabel.setSizePolicy(QtSizeExpanding, QtSizeExpanding)

        # Assemble
        self.outerBox = QHBoxLayout()
        self.outerBox.addWidget(self.viewLabel)
        self.outerBox.setContentsMargins(mPx, mPx, 0, mPx)
        self.outerBox.setSpacing(0)

        self.setLayout(self.outerBox)

        logger.debug("Ready: GuiTagsToolBar")

        return


class GuiTagsTree(QTreeWidget):

    def __init__(self, tagsView: GuiTagsView) -> None:
        super().__init__(parent=tagsView)

        logger.debug("Create: GuiTagsTree")

        self.tagsView = tagsView

        logger.debug("Ready: GuiTagsTree")

        return
