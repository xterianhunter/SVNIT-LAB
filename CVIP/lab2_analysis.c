/*
 * SVNIT Surat - CVIP Lab Assignment 2: PGM/PPM Header Analysis
 * Course: Computer Vision and Image Processing (CSCS111 / CSDS119)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* Simple Image Header & Payload Structure */
typedef struct {
    char magic[3];
    int w, h, max_val;
    int channels;          /* 1 for PGM (P5), 3 for PPM (P6) */
    int bytes_per_sample;  /* 1 if max_val <= 255, else 2 */
    int bytes_per_pixel;   /* channels * bytes_per_sample */
    long long total_pixels;
    long long expected_bytes;
    long header_offset;
    long file_size;
    unsigned char *data;
} ImageHeader;

/* Skip comments ('#') and whitespace in Netpbm header */
static void skip_comments(FILE *fp) {
    int ch;
    while ((ch = fgetc(fp)) != EOF) {
        if (isspace(ch)) continue;
        if (ch == '#') {
            while ((ch = fgetc(fp)) != EOF && ch != '\n');
            continue;
        }
        ungetc(ch, fp);
        break;
    }
}

/* Parse Header and Load Image Payload */
ImageHeader* read_image_header_and_data(const char *filename) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) {
        fprintf(stderr, "Error: Cannot open file '%s'\n", filename);
        return NULL;
    }

    /* 1. Measure total physical file size */
    fseek(fp, 0, SEEK_END);
    long file_size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    /* 2. Read Magic Number */
    char magic[3] = {0};
    if (fscanf(fp, "%2s", magic) != 1) {
        fprintf(stderr, "Error: Invalid header in '%s'\n", filename);
        fclose(fp);
        return NULL;
    }

    if (strcmp(magic, "P5") != 0 && strcmp(magic, "P6") != 0) {
        fprintf(stderr, "Error: Unsupported magic '%s'. Only P5 and P6 supported.\n", magic);
        fclose(fp);
        return NULL;
    }

    /* 3. Read Header Fields with Comment Skipping */
    skip_comments(fp);
    int w = 0, h = 0, max_val = 0;
    if (fscanf(fp, "%d", &w) != 1) { fclose(fp); return NULL; }
    skip_comments(fp);
    if (fscanf(fp, "%d", &h) != 1) { fclose(fp); return NULL; }
    skip_comments(fp);
    if (fscanf(fp, "%d", &max_val) != 1) { fclose(fp); return NULL; }
    fgetc(fp); /* Consume single separator whitespace before binary payload */

    long header_offset = ftell(fp);

    /* 4. Populate Struct & Derived Metrics */
    ImageHeader *img = (ImageHeader *)calloc(1, sizeof(ImageHeader));
    if (!img) { fclose(fp); return NULL; }

    strcpy(img->magic, magic);
    img->w = w;
    img->h = h;
    img->max_val = max_val;
    img->channels = (strcmp(magic, "P6") == 0) ? 3 : 1;
    img->bytes_per_sample = (max_val <= 255) ? 1 : 2;
    img->bytes_per_pixel = img->channels * img->bytes_per_sample;
    img->total_pixels = (long long)w * h;
    img->expected_bytes = img->total_pixels * img->bytes_per_pixel;
    img->header_offset = header_offset;
    img->file_size = file_size;

    /* 5. Dynamically Allocate and Read Pixel Data */
    img->data = (unsigned char *)malloc(img->expected_bytes);
    if (img->data) {
        size_t read_bytes = fread(img->data, 1, img->expected_bytes, fp);
        if (read_bytes != (size_t)img->expected_bytes) {
            fprintf(stderr, "Warning: Expected %lld bytes, read %zu in '%s'\n",
                    img->expected_bytes, read_bytes, filename);
        }
    }

    fclose(fp);
    return img;
}

void free_image_header(ImageHeader *img) {
    if (img) {
        if (img->data) free(img->data);
        free(img);
    }
}

/* Display Detailed Header & Data Analysis */
void analyze_image_file(const char *filename) {
    printf("\n======================================================================\n");
    printf(" HEADER & DATA ANALYSIS: %s\n", filename);
    printf("======================================================================\n");

    ImageHeader *img = read_image_header_and_data(filename);
    if (!img) return;

    /* 1. Format & Magic Number */
    printf("1. Image Format & Magic Number:\n");
    printf("   • Magic Number    : %s (%s)\n", img->magic,
           (strcmp(img->magic, "P5") == 0) ? "Binary Grayscale (PGM)" : "Binary Truecolor RGB (PPM)");
    printf("   • Architectural Meaning : Specifies file structure, raster layout, and color channels.\n");

    /* 2. Header Dimensions & MaxVal */
    printf("\n2. Header Fields:\n");
    printf("   • Width           : %d pixels\n", img->w);
    printf("   • Height          : %d pixels\n", img->h);
    printf("   • MaxVal          : %d (%s-bit depth)\n", img->max_val,
           (img->max_val <= 255) ? "8" : "16");

    /* 3. Pixel & Channel Calculations */
    printf("\n3. Pixel & Channel Calculations:\n");
    printf("   • Total Pixels    : %lld (Width x Height = %d x %d)\n",
           img->total_pixels, img->w, img->h);
    printf("   • Color Channels  : %d (%s)\n", img->channels,
           (img->channels == 1) ? "Grayscale" : "RGB");
    printf("   • Bytes per Sample: %d byte(s) [MaxVal %s 255]\n",
           img->bytes_per_sample, (img->max_val <= 255) ? "<=" : ">");
    printf("   • Bytes per Pixel : %d byte(s) (Channels x Bytes/Sample = %d x %d)\n",
           img->bytes_per_pixel, img->channels, img->bytes_per_sample);

    /* 4. Expected Size Calculation */
    printf("\n4. Expected Image Data Size:\n");
    printf("   • Formula         : Width x Height x Channels x BytesPerSample\n");
    printf("   • Calculation     : %d x %d x %d x %d = %lld bytes\n",
           img->w, img->h, img->channels, img->bytes_per_sample, img->expected_bytes);

    /* 5. File Verification */
    long actual_data_in_file = img->file_size - img->header_offset;
    printf("\n5. File Integrity Verification:\n");
    printf("   • Header Size     : %ld bytes (raster payload offset)\n", img->header_offset);
    printf("   • Total File Size : %ld bytes\n", img->file_size);
    printf("   • Available Data  : %ld bytes (Total File Size - Header Size)\n", actual_data_in_file);
    if (actual_data_in_file == img->expected_bytes) {
        printf("   • Status          : [VERIFIED] Expected data matches actual file payload exactly.\n");
    } else {
        printf("   • Status          : [MISMATCH] File may be truncated, corrupt, or misparsed!\n");
    }

    /* 6. First 10 Pixels Inspection */
    printf("\n6. First 10 Pixel Values:\n   ");
    for (int i = 0; i < 10 && i < img->total_pixels; i++) {
        if (img->channels == 1) {
            if (img->bytes_per_sample == 1) {
                printf("[%d] ", img->data[i]);
            } else {
                int val = (img->data[i * 2] << 8) | img->data[i * 2 + 1];
                printf("[%d] ", val);
            }
        } else {
            if (img->bytes_per_sample == 1) {
                printf("(%d,%d,%d) ", img->data[i * 3], img->data[i * 3 + 1], img->data[i * 3 + 2]);
            } else {
                int r = (img->data[i * 6] << 8) | img->data[i * 6 + 1];
                int g = (img->data[i * 6 + 2] << 8) | img->data[i * 6 + 3];
                int b = (img->data[i * 6 + 4] << 8) | img->data[i * 6 + 5];
                printf("(%d,%d,%d) ", r, g, b);
            }
        }
    }
    printf("\n");
    if (img->bytes_per_sample == 2) {
        printf("   • 16-Bit Interpretation: 2 consecutive bytes per sample in Big-Endian order: (MSB << 8) | LSB.\n");
    }

    free_image_header(img);
}

/* Extension vs Format Justification */
void demonstrate_extension_vs_format(void) {
    printf("\n======================================================================\n");
    printf(" EXTENSION VERSUS FORMAT EVALUATION\n");
    printf("======================================================================\n");
    printf("  • Finding: File extensions (.pgm, .ppm, .dat) are merely OS naming hints.\n");
    printf("  • Authoritative Source: The magic number in the file header (P5 vs P6)\n");
    printf("    is the ONLY reliable identifier that dictates binary decoding rules.\n");
    printf("  • Proof: Renaming 'sample.ppm' to 'sample.pgm' does not change the pixel\n");
    printf("    interleaving (RGB triplets). The header magic number ensures correct parsing.\n");
}

/* Critical Thinking: 640x480 Theoretical Scaling Matrix */
void critical_thinking_analysis(void) {
    printf("\n======================================================================\n");
    printf(" CRITICAL-THINKING ANALYSIS (Dimensions: 640 x 480 = 307,200 pixels)\n");
    printf("======================================================================\n");
    printf("  Configuration                          | Formula (W x H x C x B)    | Expected Data Size\n");
    printf("  ---------------------------------------+----------------------------+-------------------\n");
    printf("  (i)   PGM (MaxVal = 255,   8-bit, 1 ch)| 640 x 480 x 1 x 1          |   307,200 bytes\n");
    printf("  (ii)  PPM (MaxVal = 255,   8-bit, 3 ch)| 640 x 480 x 3 x 1          |   921,600 bytes\n");
    printf("  (iii) PGM (MaxVal = 65535, 16-bit, 1 ch)| 640 x 480 x 1 x 2          |   614,400 bytes\n");
    printf("  (iv)  PPM (MaxVal = 65535, 16-bit, 3 ch)| 640 x 480 x 3 x 2          | 1,843,200 bytes\n");
    printf("  ----------------------------------------------------------------------------------------\n");
    printf("  Scientific Explanation:\n");
    printf("  -> Spatial dimensions (640x480) define only the spatial sampling grid (pixel count).\n");
    printf("  -> Total byte size scales linearly with two orthogonal dimensions:\n");
    printf("     1. Color Channels (C): Grayscale (1) vs RGB Color (3) -> 3x multiplier.\n");
    printf("     2. Quantization Bit Depth (B): 8-bit (1 byte) vs 16-bit (2 bytes) -> 2x multiplier.\n");
    printf("======================================================================\n\n");
}

int main(int argc, char *argv[]) {
    printf("\n######################################################################\n");
    printf("  SVNIT SURAT - CVIP LAB 2: PGM/PPM IMAGE HEADER ANALYSIS IN C\n");
    printf("######################################################################\n");

    const char *pgm_file = (argc > 1) ? argv[1] : "sample_01.pgm";
    const char *ppm_file = (argc > 2) ? argv[2] : "sample_01.ppm";

    analyze_image_file(pgm_file);
    analyze_image_file(ppm_file);

    demonstrate_extension_vs_format();
    critical_thinking_analysis();

    return 0;
}
