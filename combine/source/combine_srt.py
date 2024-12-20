from tkinter import filedialog, Tk
from pysrt import open as srt_open, SubRipFile, SubRipItem

def combine_srt(languageA_file, languageB_file):
  """
  Combines two SRT files with languageA on top and languageB on bottom.

  Args:
      languageA_file: Path to the languageA SRT file.
      languageB_file: Path to the languageB SRT file.
  """
  languageA_subs = srt_open(languageA_file)
  languageB_subs = srt_open(languageB_file)

  combined_subs = SubRipFile()
  for languageA_sub, languageB_sub in zip(languageA_subs, languageB_subs):
    combined_text = f"{languageA_sub.text}\n{languageB_sub.text}"
    # Create a new SubRipItem with combined text and same timing as languageA subtitle
    combined_sub = SubRipItem(index=len(combined_subs),
                              start=languageA_sub.start,
                              end=languageA_sub.end,
                              text=combined_text)
    combined_subs.append(combined_sub)

  return combined_subs

def save_combined_srt(combined_subs: SubRipFile):
  """
  Prompts user to save the combined SRT file with tkinter.saveasfilename().

  Args:
      combined_subs: The combined subtitles to save.
  """
  Tk().withdraw()
  filepath = filedialog.asksaveasfilename(title="Save combined srt...", defaultextension=".srt")
  combined_subs.save(filepath, encoding='utf-8')

if __name__ == "__main__":
  languageA_file = filedialog.askopenfilename(title="Choose languageA srt...")
  languageB_file = filedialog.askopenfilename(title="Choose languageB srt...")
  combined_subs = combine_srt(languageA_file, languageB_file)
  save_combined_srt(combined_subs)
  print("Combined SRT saved successfully!")