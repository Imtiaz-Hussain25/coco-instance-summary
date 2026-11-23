# COCO Instance Summary

Summarize instance counts and box area in COCO detection exports.

## What this project does

This is an original command-line utility for analyzing or presenting computer vision outputs. It does not include pretrained weights, training code, or copied research implementations.

## Input and output

Input example: `{"categories":[{"id":1,"name":"person"}],"annotations":[{"category_id":1,"image_id":1,"bbox":[0,0,20,30]}]}`

Run: `python main.py annotations.json report.csv`

See `python main.py --help` for positional arguments. Output is written to the requested file, except the neighbor search, which prints ranked results.

## Related tools

Detectron2 or another COCO-format exporter. This project is independent of those implementations and consumes their exported results where applicable.

## Requirements

Python 3.10 or newer. No third-party Python packages are required.

## Limitations

Box area is width times height; this is not segmentation mask area. Model inference is not locally tested. The utility has only been checked for syntax and on small synthetic inputs.


## Why it is useful

COCO exports contain individual annotations but few at-a-glance summaries. This utility counts objects and images by category and computes mean bounding-box area for each category.

## Data contract

Input uses a COCO-style JSON object with `categories` and `annotations`. Each annotation needs `category_id`, `image_id`, and `[x, y, width, height]` in `bbox`. Output is a per-category CSV.

## Reproduce the example

```bash
python main.py examples/annotations.json examples/report.csv
```

The command reads the included sample input. Generated reports in `examples/` can be removed when finished.

## Interpretation

Bounding-box area is an approximation of spatial extent, not mask area. Empty or missing boxes contribute zero area.

## License

MIT. See `LICENSE`.

