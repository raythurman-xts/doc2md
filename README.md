# Document to Markdown Converter

A simple CLI tool that uses Microsoft's [markitdown](https://github.com/microsoft/markitdown) package to convert various document formats to Markdown.

## Installation

1. Install the markitdown package with all optional dependencies:

```bash
pip install 'markitdown[all]'
```

Or install with specific format support only:

```bash
pip install 'markitdown[docx,pdf,pptx]'
```

2. No additional installation needed for this script.

## Usage

Basic usage:

```bash
python doc2md.py input.docx output.md
```

If you don't specify an output file, the markdown content will be printed to stdout:

```bash
python doc2md.py input.docx
```

### Additional Options

- `--plugins`: Enable markitdown plugins
- `--docintel` or `-d`: Use Azure Document Intelligence
- `--endpoint` or `-e`: Specify Azure Document Intelligence endpoint

Example with Azure Document Intelligence:

```bash
python doc2md.py input.pdf output.md --docintel --endpoint "https://your-endpoint.cognitiveservices.azure.com/"
```

## Supported Formats

The script supports all formats that markitdown supports:

- PDF
- Word documents (docx)
- PowerPoint (pptx)
- Excel (xlsx)
- Images (with EXIF metadata and OCR)
- Audio (with EXIF metadata and speech transcription)
- HTML
- Text-based formats (CSV, JSON, XML)
- ZIP files
- YouTube URLs
- EPubs
- And more!

## Why Markdown?

Markdown is extremely close to plain text, with minimal markup or formatting, but still provides a way to represent important document structure. It's ideal for use with LLMs and related text analysis pipelines.
