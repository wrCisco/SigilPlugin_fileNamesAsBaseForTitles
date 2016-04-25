# sigilPlugin_fileNamesAsBaseForTitles
Add/modify title tags of selected xhtml files of an epub using for each file its filename (without extension) filtered by a custom regex.

If you want to add/overwrite title tags of all xhtml files, just don't select any file in the Book Browser (or select them all, it's the same).

The regular expression you want to use to filter the filenames must be copied to the clipboard: just write it somewhere and copy it with Cmd+C (on Mac) or Ctrl+C right before launching the plugin. If the regex doesn't match anything, the entire filename will be written as title.
