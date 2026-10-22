/*
 * SVNIT Surat - CVIP Lab Assignment 1: Digital Image Analysis
 * Course: Computer Vision and Image Processing (CSCS111 / CSDS119)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

/* Simple Grayscale Image Structure */
typedef struct {
    int w, h;
    unsigned char *data; /* Contiguous 1D pixel array */
} Image;

/* Consolidated Statistics Structure */
typedef struct {
    int min, max;
    double mean, variance, std_dev;
    long long total;
    double dark_pct, med_pct, bright_pct;
    long long dark_cnt, med_cnt, bright_cnt;
} Stats;

/* Memory Management */
Image* create_image(int w, int h) {
    Image *img = (Image *)malloc(sizeof(Image));
    if (!img) return NULL;
    img->w = w;
    img->h = h;
    img->data = (unsigned char *)malloc((size_t)w * h);
    if (!img->data) { free(img); return NULL; }
    return img;
}

void free_image(Image *img) {
    if (img) {
        if (img->data) free(img->data);
        free(img);
    }
}

/* Helper to skip whitespace and comments in PGM header */
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

/* Read PGM Image (P5 Binary) */
Image* read_pgm(const char *filename) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) {
        fprintf(stderr, "Error: Cannot open '%s'\n", filename);
        return NULL;
    }
    char magic[3];
    if (fscanf(fp, "%2s", magic) != 1 || strcmp(magic, "P5") != 0) {
        fprintf(stderr, "Error: '%s' is not a binary P5 PGM\n", filename);
        fclose(fp);
        return NULL;
    }
    skip_comments(fp);
    int w, h, max_val;
    if (fscanf(fp, "%d", &w) != 1) { fclose(fp); return NULL; }
    skip_comments(fp);
    if (fscanf(fp, "%d", &h) != 1) { fclose(fp); return NULL; }
    skip_comments(fp);
    if (fscanf(fp, "%d", &max_val) != 1) { fclose(fp); return NULL; }
    fgetc(fp); /* Consume single separator byte */

    Image *img = create_image(w, h);
    if (img) {
        fread(img->data, 1, (size_t)w * h, fp);
    }
    fclose(fp);
    return img;
}

/* Write PGM Image (P5 Binary) */
int write_pgm(const char *filename, const Image *img) {
    if (!img || !img->data) return 0;
    FILE *fp = fopen(filename, "wb");
    if (!fp) return 0;
    fprintf(fp, "P5\n%d %d\n255\n", img->w, img->h);
    size_t total = (size_t)img->w * img->h;
    size_t written = fwrite(img->data, 1, total, fp);
    fclose(fp);
    return written == total;
}

/* Compute Image Statistics and Intensity Range Distribution */
Stats compute_stats(const Image *img) {
    Stats s = {255, 0, 0.0, 0.0, 0.0, (long long)img->w * img->h, 0, 0, 0, 0, 0, 0};
    double sum = 0.0;
    for (long long i = 0; i < s.total; i++) {
        unsigned char val = img->data[i];
        if (val < s.min) s.min = val;
        if (val > s.max) s.max = val;
        sum += val;
        if (val <= 85) s.dark_cnt++;
        else if (val <= 170) s.med_cnt++;
        else s.bright_cnt++;
    }
    s.mean = sum / s.total;

    double var_sum = 0.0;
    for (long long i = 0; i < s.total; i++) {
        double diff = img->data[i] - s.mean;
        var_sum += diff * diff;
    }
    s.variance = var_sum / s.total;
    s.std_dev = sqrt(s.variance);

    s.dark_pct = (s.dark_cnt * 100.0) / s.total;
    s.med_pct = (s.med_cnt * 100.0) / s.total;
    s.bright_pct = (s.bright_cnt * 100.0) / s.total;
    return s;
}

/* Print Compact 16-Interval Histogram */
void print_histogram(const Image *img, const char *title) {
    int hist[256] = {0};
    size_t total = (size_t)img->w * img->h;
    for (size_t i = 0; i < total; i++) hist[img->data[i]]++;

    printf("\n--- Histogram (16-Interval Summary): %s ---\n", title);
    printf("  Range       | Count       | Percentage\n");
    printf("  --------------------------------------\n");
    for (int g = 0; g < 16; g++) {
        int cnt = 0;
        for (int b = 0; b < 16; b++) cnt += hist[g * 16 + b];
        printf("  [%3d - %3d] | %11d | %6.2f%%\n", g * 16, g * 16 + 15, cnt, (cnt * 100.0) / total);
    }
}

/* Analyze Region of Interest (ROI) */
void analyze_roi(const Image *img, int rx, int ry, int rw, int rh, const char *name) {
    long long count = (long long)rw * rh;
    int min_v = 255, max_v = 0;
    double sum = 0.0;
    long long dark = 0, med = 0, bright = 0;

    for (int y = ry; y < ry + rh; y++) {
        for (int x = rx; x < rx + rw; x++) {
            unsigned char v = img->data[y * img->w + x];
            if (v < min_v) min_v = v;
            if (v > max_v) max_v = v;
            sum += v;
            if (v <= 85) dark++;
            else if (v <= 170) med++;
            else bright++;
        }
    }
    double mean = sum / count;
    double var_sum = 0.0;
    for (int y = ry; y < ry + rh; y++) {
        for (int x = rx; x < rx + rw; x++) {
            double diff = img->data[y * img->w + x] - mean;
            var_sum += diff * diff;
        }
    }
    double std_dev = sqrt(var_sum / count);

    printf("  ROI '%s' [(%d,%d), %dx%d, %lld px]:\n", name, rx, ry, rw, rh, count);
    printf("    Min: %d, Max: %d, Mean: %.2f, StdDev: %.2f\n", min_v, max_v, mean, std_dev);
    printf("    Dark [0-85]: %.2f%% | Medium [86-170]: %.2f%% | Bright [171-255]: %.2f%%\n",
           (dark * 100.0) / count, (med * 100.0) / count, (bright * 100.0) / count);
}

/* Brighten Image with Offset and [0, 255] Clamping */
Image* brighten_image(const Image *img, int offset) {
    Image *out = create_image(img->w, img->h);
    if (!out) return NULL;
    size_t total = (size_t)img->w * img->h;
    for (size_t i = 0; i < total; i++) {
        int v = img->data[i] + offset;
        out->data[i] = (unsigned char)(v > 255 ? 255 : (v < 0 ? 0 : v));
    }
    return out;
}

/* Iso-Mean Demonstration & Segmentation Feasibility */
void demonstrate_iso_mean(void) {
    printf("\n======================================================================\n");
    printf(" ISO-MEAN INVESTIGATION: CAN VISUALLY DIFFERENT IMAGES HAVE SAME MEAN?\n");
    printf("======================================================================\n");
    printf("  Pattern A (Checkerboard: 50%% at 0, 50%% at 254) -> Mean: 127.00, StdDev: 127.00\n");
    printf("  Pattern B (Uniform Gray: 100%% at 127)           -> Mean: 127.00, StdDev:   0.00\n");
    printf("  Conclusion: YES. Average intensity is a 1st-order moment measuring central tendency,\n");
    printf("  completely discarding spatial frequency, arrangement, and 2nd-order variance.\n");
}

void evaluate_segmentation(const Stats *s1, const Stats *s2, const char *f1, const char *f2) {
    printf("\n======================================================================\n");
    printf(" THRESHOLDING & SEGMENTATION SUITABILITY\n");
    printf("======================================================================\n");
    const char *best = (s2->std_dev >= s1->std_dev) ? f2 : f1;
    printf("  Selected Image: '%s'\n", best);
    printf("  Justification:\n");
    printf("    1. Higher Contrast (StdDev: %.2f vs %.2f) yields broader inter-class separation.\n",
           (s2->std_dev >= s1->std_dev ? s2->std_dev : s1->std_dev),
           (s2->std_dev >= s1->std_dev ? s1->std_dev : s2->std_dev));
    printf("    2. Distinct Dark & Bright modes create a clear histogram valley for algorithms\n");
    printf("       like Otsu's method to compute an optimal global segmentation threshold.\n");
    printf("======================================================================\n");
}

int main(int argc, char *argv[]) {
    const char *file1 = (argc > 1) ? argv[1] : "sample_01.pgm";
    const char *file2 = (argc > 2) ? argv[2] : "sample_02.pgm";

    printf("\n======================================================================\n");
    printf(" SVNIT SURAT - CVIP LAB 1: DIGITAL IMAGE ANALYSIS\n");
    printf("======================================================================\n");

    Image *img1 = read_pgm(file1);
    Image *img2 = read_pgm(file2);
    if (!img1 || !img2) {
        fprintf(stderr, "Error loading images. Please provide valid P5 PGM files.\n");
        free_image(img1);
        free_image(img2);
        return 1;
    }

    /* 1. Basic Statistics & Range Distribution */
    Stats s1 = compute_stats(img1);
    Stats s2 = compute_stats(img2);

    printf("\n--- 1. Image Statistics & Range Distribution ---\n");
    printf("Metric                     | Image 1 (%-14s) | Image 2 (%-14s)\n", file1, file2);
    printf("---------------------------+------------------------+------------------------\n");
    printf("Dimensions (W x H)         | %4d x %-4d (%7lld px) | %4d x %-4d (%7lld px)\n",
           img1->w, img1->h, s1.total, img2->w, img2->h, s2.total);
    printf("Min / Max Intensity        | %3d / %-3d              | %3d / %-3d\n", s1.min, s1.max, s2.min, s2.max);
    printf("Dynamic Range (Max - Min)  | %-22d | %-22d\n", s1.max - s1.min, s2.max - s2.min);
    printf("Average (Mean) Intensity   | %-22.2f | %-22.2f\n", s1.mean, s2.mean);
    printf("Variance                   | %-22.2f | %-22.2f\n", s1.variance, s2.variance);
    printf("Contrast (Std Deviation)   | %-22.2f | %-22.2f\n", s1.std_dev, s2.std_dev);
    printf("Dark Pixels   [0  -  85]   | %6.2f%% (%7lld px)   | %6.2f%% (%7lld px)\n", s1.dark_pct, s1.dark_cnt, s2.dark_pct, s2.dark_cnt);
    printf("Medium Pixels [86 - 170]   | %6.2f%% (%7lld px)   | %6.2f%% (%7lld px)\n", s1.med_pct, s1.med_cnt, s2.med_pct, s2.med_cnt);
    printf("Bright Pixels [171- 255]   | %6.2f%% (%7lld px)   | %6.2f%% (%7lld px)\n", s1.bright_pct, s1.bright_cnt, s2.bright_pct, s2.bright_cnt);

    /* 2. Numerical Comparison */
    printf("\n--- 2. Comparative Numerical Evaluation ---\n");
    printf("  • Brightness: %s (Mean: %.2f vs %.2f)\n",
           (s1.mean > s2.mean) ? "Image 1 is BRIGHTER, Image 2 is DARKER" : "Image 2 is BRIGHTER, Image 1 is DARKER",
           s1.mean, s2.mean);
    printf("  • Contrast  : %s (StdDev: %.2f vs %.2f)\n",
           (s1.std_dev > s2.std_dev) ? "Image 1 has HIGHER CONTRAST" : "Image 2 has HIGHER CONTRAST",
           s1.std_dev, s2.std_dev);

    /* 3. Histograms */
    print_histogram(img1, file1);
    print_histogram(img2, file2);

    /* 4. Region of Interest (ROI) Analysis */
    printf("\n--- 3. Region of Interest (ROI) Analysis ---\n");
    printf("[%s]:\n", file1);
    analyze_roi(img1, img1->w / 4, img1->h / 4, img1->w / 2, img1->h / 2, "Center 50%");
    analyze_roi(img1, 0, 0, img1->w / 4, img1->h / 4, "Top-Left Corner");

    printf("\n[%s]:\n", file2);
    analyze_roi(img2, img2->w / 4, img2->h / 4, img2->w / 2, img2->h / 2, "Center 50%");
    analyze_roi(img2, 0, 0, img2->w / 4, img2->h / 4, "Top-Left Corner");

    /* 5. Brightness Modification */
    printf("\n--- 4. Brightness Modification (+40 Offset on Image 1) ---\n");
    Image *img1_bright = brighten_image(img1, 40);
    if (img1_bright) {
        Stats sb = compute_stats(img1_bright);
        printf("  Original Image 1 : Mean = %.2f, StdDev = %.2f (Dark: %.2f%%, Med: %.2f%%, Bright: %.2f%%)\n",
               s1.mean, s1.std_dev, s1.dark_pct, s1.med_pct, s1.bright_pct);
        printf("  Brightened Image : Mean = %.2f (+%.2f), StdDev = %.2f (Dark: %.2f%%, Med: %.2f%%, Bright: %.2f%%)\n",
               sb.mean, sb.mean - s1.mean, sb.std_dev, sb.dark_pct, sb.med_pct, sb.bright_pct);
        const char *out_file = "sample_01_brightened.pgm";
        if (write_pgm(out_file, img1_bright)) {
            printf("  ✓ Saved brightened image to '%s'\n", out_file);
        }
        free_image(img1_bright);
    }

    /* 6. Iso-Mean & Segmentation Analysis */
    demonstrate_iso_mean();
    evaluate_segmentation(&s1, &s2, file1, file2);

    /* Clean Up */
    free_image(img1);
    free_image(img2);
    return 0;
}
