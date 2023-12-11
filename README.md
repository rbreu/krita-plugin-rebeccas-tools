# Rebecca's Krita Tools

A Krita plugin that installs a couple of small tools. So far:

* **Crop To Margin:** Crop image to margins as defined by guides. The image needs at least two horizontal and two vertical guides. If more guides are present, only the outermost guides are taken into account.
* **Reorder Image Sequence:** Reorder/rename the images created by the Recorder Docker. Useful if you want to remove some of the images before exporting to video.

All Actions can be found under *Tools -> Scripts*.

## Installation

Go to _Tools -> Scripts -> Import Python Plugin From Web_ and copy the URL of this page into it.

## Developer Info

To run unit tests and code checks:

```sh
pip install -r requirements-dev.txt
```

Then run `pytest` and `flake8` in the top level directory.