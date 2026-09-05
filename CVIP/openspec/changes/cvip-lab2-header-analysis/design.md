## Context

See `proposal.md` for background and motivation. Lab 2 focuses on analyzing PGM and PPM image headers, computing expected payload sizes under varying channel counts and bit depths, dynamically reading and verifying pixel data, and understanding header-driven format decoding without external libraries.

## Goals / Non-Goals

**Goals:**
- Define a single concise struct `ImageHeader` holding header metadata, derived metrics (channels, bytes per sample, bytes per pixel, expected data size), and raw data buffer.
- Parse magic number (`P5`/`P6`), width, height, and `MaxVal` with robust comment skipping.
- Calculate exact pixel and byte sizes for 8-bit ($\le 255$) and 16-bit ($> 255$) images across 1-channel (PGM) and 3-channel (PPM) formats.
- Dynamically allocate and read pixel data using `fread()`, comparing against actual file size using `fseek()` / `ftell()`.
- Display the first 10 pixels (grayscale scalars or RGB triplets).
- Deliver concise automated demonstrations for extension vs format justification and the $640 \times 480$ critical-thinking scaling exercise.
- Keep source code clean, direct, and under 200 lines.

**Non-Goals:**
- Building an interactive GUI or image rendering window.
- Supporting complex compression or non-Netpbm image formats (e.g. JPEG, PNG).

## Decisions

### 1. Minimal Header & Payload Structure
- **Decision**: Use a single `ImageHeader` struct encapsulating all parsed metadata, calculated metrics, and pixel buffer.
- **Rationale**: Keeps all information for a given image together in memory, making analysis and deallocation clean and simple.

### 2. Streamlined Parsing and Comment Handling
- **Decision**: Implement a reusable `skip_comments(FILE *fp)` helper function to ignore leading whitespace and `#` comment lines before header tokens.
- **Rationale**: Standard Netpbm format allows comments anywhere before raster data.

### 3. File Completeness Verification via `fseek`/`ftell`
- **Decision**: Measure physical file size using `fseek(fp, 0, SEEK_END); ftell(fp)` and compare against `header_offset + expected_bytes`.
- **Rationale**: Provides an exact, non-destructive check of file integrity.

### 4. Dynamic First-10 Pixel Formatting
- **Decision**: If `channels == 1` (PGM), print scalar values `pixel[i]`; if `channels == 3` (PPM), print RGB tuples `(R, G, B)`. For 16-bit images, read 2-byte big-endian pairs `(byte0 << 8) | byte1`.

## Risks / Trade-offs

- **[Risk] Missing sample PPM files in repo** → **Mitigation**: Synthesize or convert a sample PPM test image (`sample_01.ppm`) in the workspace so both PGM and PPM paths are validated.
- **[Risk] Trailing whitespace after header MaxVal** → **Mitigation**: Consume exactly one whitespace character after `fscanf` before binary read begins.
