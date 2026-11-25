CC = mpicc
CFLAGS = -O2 -Wall
TARGETS = tile_matmul sobel_edge

all: $(TARGETS)

tile_matmul: tile_matmul.c
	$(CC) $(CFLAGS) -o tile_matmul tile_matmul.c -lm

sobel_edge: sobel_edge.c
	$(CC) $(CFLAGS) -o sobel_edge sobel_edge.c -lm

clean:
	rm -f $(TARGETS) output_edges.pgm report.aux report.log

run: tile_matmul
	mpirun --oversubscribe -np 4 ./tile_matmul

run_sobel: sobel_edge
	mpirun --oversubscribe -np 4 ./sobel_edge

run_lena: sobel_edge lena.pgm
	mpirun --oversubscribe -np 4 ./sobel_edge lena.pgm

report: report.tex lena.png output_edges.png
	@which pdflatex >/dev/null 2>&1 && pdflatex -interaction=nonstopmode report.tex || echo "Note: pdflatex is not installed on this system. You can compile report.tex on any LaTeX-enabled machine."

clean_report:
	rm -f report.aux report.log report.pdf

get_lena:
	@if [ ! -f lena.pgm ]; then \
		curl -L -s -A "Mozilla/5.0" -o lena.png "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png" && \
		convert lena.png -colorspace Gray lena.pgm && \
		rm -f lena.png; \
	fi

.PHONY: all clean run run_sobel run_lena report clean_report get_lena

