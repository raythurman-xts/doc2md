#!/usr/bin/env python3
"""
CLI tool to convert various file formats to Markdown using Microsoft's markitdown.
Usage: python doc2md.py input.docx output.md
"""
import argparse
import os
import sys

from markitdown import MarkItDown


def main():
    parser = argparse.ArgumentParser(description='Convert documents to Markdown using markitdown')
    parser.add_argument('input_path', help='Path to the input file')
    parser.add_argument('output_path', nargs='?', help='Path for the output markdown file. If not provided, output is printed to stdout')
    parser.add_argument('--plugins', action='store_true', help='Enable markitdown plugins')
    parser.add_argument('--docintel', '-d', action='store_true', help='Use Azure Document Intelligence')
    parser.add_argument('--endpoint', '-e', help='Azure Document Intelligence endpoint')

    args = parser.parse_args()

    try:
        markitdown_options = {
            'enable_plugins': args.plugins
        }

        # Add Document Intelligence options if specified
        if args.docintel and args.endpoint:
            markitdown_options['docintel_endpoint'] = args.endpoint

        md = MarkItDown(**markitdown_options)

        result = md.convert(args.input_path)

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        if args.output_path:
            output_path = os.path.join(output_dir, os.path.basename(args.output_path))
        else:
            base_name = os.path.splitext(os.path.basename(args.input_path))[0]
            output_path = os.path.join(output_dir, f"{base_name}.md")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        print(f"Converted {args.input_path} to {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(3)


if __name__ == "__main__":
    main()
