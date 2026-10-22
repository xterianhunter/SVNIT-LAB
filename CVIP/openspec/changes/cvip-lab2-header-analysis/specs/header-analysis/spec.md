## Purpose

Provides robust PGM (P5) and PPM (P6) binary image header parsing, channel/sample bit depth determination, expected pixel byte size calculation, dynamic image payload reading, file completeness verification, initial pixel value extraction, and format evaluation using basic C operations.

## ADDED Requirements

### Requirement: Image Format Identification & Magic Number Parsing
The system SHALL inspect the magic number at the beginning of an image file to identify the image type (`P5` for PGM grayscale or `P6` for PPM RGB color) and explain its architectural meaning.

#### Scenario: Identify P5 PGM grayscale image
- **WHEN** a binary PGM file is opened
- **THEN** the system reads magic number `P5`, identifies it as a binary grayscale bitmap, and sets channel count to 1.

#### Scenario: Identify P6 PPM color image
- **WHEN** a binary PPM file is opened
- **THEN** the system reads magic number `P6`, identifies it as a binary RGB color pixmap, and sets channel count to 3.

### Requirement: Header Metadata & Comment Extraction
The system SHALL parse image width, height, and maximum intensity value (`MaxVal`) from the header while correctly skipping intervening whitespace and comment lines starting with `#`.

#### Scenario: Parse header with comments and variable whitespace
- **WHEN** reading an image header containing comments and whitespace
- **THEN** the system extracts positive integers for width, height, and `MaxVal` without parsing errors.

### Requirement: Pixel and Data Size Calculation
The system SHALL determine total pixels, bytes per sample (1 byte for `MaxVal` $\le 255$, 2 bytes for `MaxVal` $> 255$), bytes per pixel (`channels * bytes_per_sample`), and the exact expected image data payload size in bytes (`width * height * channels * bytes_per_sample`).

#### Scenario: Calculate 8-bit PGM size
- **WHEN** analyzing a PGM image with width $W$, height $H$, and `MaxVal` $\le 255$
- **THEN** expected data size is computed as $W \times H \times 1 \times 1$ bytes.

#### Scenario: Calculate 8-bit PPM size
- **WHEN** analyzing a PPM image with width $W$, height $H$, and `MaxVal` $\le 255$
- **THEN** expected data size is computed as $W \times H \times 3 \times 1$ bytes.

#### Scenario: Calculate 16-bit image size
- **WHEN** analyzing an image with `MaxVal` $> 255$ (e.g. 65535)
- **THEN** expected data size uses 2 bytes per sample ($W \times H \times \text{channels} \times 2$ bytes).

### Requirement: Dynamic Payload Read and Integrity Verification
The system SHALL dynamically allocate memory for the expected payload, read the exact byte count from after the header separator, compare actual bytes read with expected bytes, and verify whether the physical file length matches expected data size plus header size.

#### Scenario: Successful full-payload read
- **WHEN** file contains complete pixel payload
- **THEN** the system reads exactly the expected byte count, verifies that no unexpected EOF occurred, and reports file integrity verified.

#### Scenario: Truncated or corrupted file
- **WHEN** file contains fewer bytes than indicated by header dimensions
- **THEN** the system reports a mismatch warning indicating potential file truncation or corruption.

### Requirement: Initial Pixel Inspection
The system SHALL display the first 10 pixel values of the loaded image payload: single grayscale integers for PGM and `(R, G, B)` triplets for PPM, with an explanation of sample bit representation.

#### Scenario: Inspect first 10 pixels of PGM
- **WHEN** inspecting a loaded PGM image
- **THEN** the system outputs the first 10 integer grayscale intensity values.

#### Scenario: Inspect first 10 pixels of PPM
- **WHEN** inspecting a loaded PPM image
- **THEN** the system outputs the first 10 RGB triplet tuples `(R, G, B)`.

### Requirement: Extension vs. Format Justification
The system SHALL evaluate and demonstrate whether a file extension alone determines the true image format, proving that internal header magic numbers are authoritative.

#### Scenario: Verify extension vs header
- **WHEN** evaluating image headers against file extensions
- **THEN** the system explains that file extensions are arbitrary OS naming conventions whereas magic numbers in file headers define actual payload interpretation.

### Requirement: Critical-Thinking Dimensional Scaling Analysis
The system SHALL perform theoretical byte calculation for a $640 \times 480$ image under 8-bit and 16-bit PGM/PPM configurations and provide scientific explanation for byte variations.

#### Scenario: Compute and explain scaling matrix
- **WHEN** analyzing a $640 \times 480$ frame at `MaxVal`=255 and `MaxVal`=65535
- **THEN** the system calculates 307,200 bytes (8-bit PGM), 921,600 bytes (8-bit PPM), 614,400 bytes (16-bit PGM), 1,843,200 bytes (16-bit PPM) and explains the role of channel depth and bit depth.
