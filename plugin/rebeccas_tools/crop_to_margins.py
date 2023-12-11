def get_crop_values(doc):
    hguides = list(filter(
        lambda x: 0 <= x <= doc.height(),
        doc.horizontalGuides()))
    vguides = list(filter(
        lambda x: 0 <= x <= doc.width(),
        doc.verticalGuides()))

    if len(hguides) < 2 or len(vguides) < 2:
        return None

    vguides.sort()
    hguides.sort()

    cropx = int(vguides[0])
    cropw = int(vguides[-1] - cropx)
    cropy = int(hguides[0])
    croph = int(hguides[-1] - cropy)

    return (cropx, cropy, cropw, croph)
