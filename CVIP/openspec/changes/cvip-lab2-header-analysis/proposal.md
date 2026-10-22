## Why

In digital image processing, image files contain essential header metadata that dictates how raw pixel byte streams must be interpreted. For SVNIT CVIP Lab Assignment 2, a simple, dependency-free C program is required to parse PGM (P5) and PPM (P6) image headers directly, compute expected data sizes (accounting for channels and 8-bit vs 16-bit depths), dynamically read and verify image payloads, analyze initial pixel values, test file extension reliability, and answer critical-thinking analytical questions.

## What Changes

- **Add `lab2_analysis.c`**: Implement a concise, self-contained C program (<200 lines) using standard I/O (`fopen`, `fgetc`, `fscanf`, `fread`, `fseek`, `ftell`) and a simple header/image structure.
- **Header Parsing & Validation**: Identify magic numbers (`P5` for PGM grayscale, `P6` for PPM RGB), extract width, height, and MaxVal, ignoring comments (`#`) and whitespace.
- **Dynamic Size & Byte Calculations**: Determine total pixels, channels (1 or 3), bytes per sample (1 for MaxVal $\le 255$, 2 for MaxVal $> 255$), bytes per pixel, and expected byte payload size.
- **Payload Verification & Pixel Inspection**: Read exact calculated data bytes, compare against physical file length using `ftell()`, and print the first 10 pixel samples/triplets.
- **Extension vs. Format & Critical Thinking**: Implement clear automated demonstrations for extension vs magic number validation, as well as the $640 \times 480$ theoretical calculation across 8-bit and 16-bit PGM/PPM images.
- **Sample Generation & Makefile Support**: Generate sample PPM image assets for testing and update `Makefile` to build and run Lab 2.

## Capabilities

### New Capabilities
- `header-analysis`: Parsing PGM (P5) and PPM (P6) headers, computing sample/channel data sizes, reading raw payload bytes, verifying file integrity, inspecting initial pixels, and evaluating header format rules.

### Modified Capabilities
<!-- No modified capabilities. -->

## Impact

- **Affected Code**: Creates `lab2_analysis.c`, creates test PPM image asset (`sample_01.ppm`), and adds `lab2` target to `Makefile`.
- **Dependencies**: Standard C library (`stdio.h`, `stdlib.h`, `string.h`, `ctype.h`) - zero external dependencies.
