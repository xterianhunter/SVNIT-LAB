## Why

In Part B of Lab 5, standard single-scale cross-correlation at 1.0x scale fails to accurately bound the target product on the shelf because the template image (`product.png`, $39 \times 59$) has a scale mismatch with the instance appearing on the shelf ($22 \times 34$, roughly $0.58\times$ scale). Consequently, unscaled cross-correlation picks an incorrect region. We need a more precise, multi-scale cross-correlation approach that accurately locates the exact product instance with high confidence ($> 96\%$ correlation) and tightly bounds it with the requested blue rectangle.

## What Changes

- Update Part B in `lab5_solution.ipynb`:
  - Implement multi-scale cross-correlation search across template scales (from $0.4\times$ to $1.2\times$).
  - Use normalized correlation coefficient / normalized cross-correlation across color channels or grayscale to identify the true peak response.
  - Accurately draw the blue rectangle around the detected product at coordinates $(247, 235)$ with scale-adjusted dimensions.
  - Update the observations to explain why scale-space search is essential for accurate real-world template matching.

## Capabilities

### New Capabilities
- `lab5-filtering-and-matching`: Implements precise multi-scale cross-correlation template matching to accurately locate and bound the true target item on the shelf.

### Modified Capabilities
<!-- None -->

## Impact

- **Affected Files**: `lab5_solution.ipynb`
- **Dependencies**: Uses existing OpenCV and NumPy libraries already installed; no new external dependencies.
- **Breaking Changes**: None.
