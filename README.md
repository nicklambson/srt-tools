# README.md

## Combine SRT

This Python script, combine_srt.py, is a tool for combining two SRT (SubRip Text) subtitle files into one. The combined SRT file will have the subtitles from the first file on top and the subtitles from the second file on the bottom.

### Dependencies

This script requires the following Python packages:

- [pysrt](https://pypi.org/project/pysrt/) for handling SRT files

You can install these packages with pip:

```bash
pip install pysrt
```

### Usage

To use this script, simply run it with Python:

```bash
python combine_srt.py
```

The script will prompt you to select two SRT files to combine. After selecting the files, it will then prompt you to save the combined SRT file.

### Functions

The script contains two main functions:

- `combine_srt(languageA_file, languageB_file)`: This function takes the paths to two SRT files as arguments. It combines the subtitles from the two files into one, with the subtitles from the first file on top and the subtitles from the second file on the bottom.

- `save_combined_srt(combined_subs)`: This function takes a `SubRipFile` object (the combined subtitles) as an argument. It prompts the user to save the combined SRT file.

### Example

Here's an example of how the combined subtitles will look:

```
1
00:00:01,000 --> 00:00:04,000
Hello, world!
Hola, mundo!

2
00:00:05,000 --> 00:00:08,000
Goodbye, world!
Adiós, mundo!
```

In this example, "Hello, world!" and "Goodbye, world!" are subtitles from the first file, and "Hola, mundo!" and "Adiós, mundo!" are subtitles from the second file.