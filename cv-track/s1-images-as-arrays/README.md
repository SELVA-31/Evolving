# S1 · Images as arrays · 05 – 18 Oct

**Goal:** Implement grayscale, histogram and thresholding with NumPy only, validated against OpenCV.
**Pass check:** max absolute difference **≤ 1** vs OpenCV for each function.

Folders: `python/` · `images/`

## Results

| Function | My version | OpenCV reference | Max diff | Notes |
|---|---|---|---|---|
| Grayscale | | `cv2.cvtColor` | | |
| Histogram | | `cv2.calcHist` | | |
| Threshold (fixed) | | `cv2.threshold` | | |
| Threshold (Otsu) | | `cv2.threshold` + `THRESH_OTSU` | | |

## Lessons

-
