Development Source of the Model Designer JS
===========================================

During development we used shell scripts to automatically merge and minify the
JavaScript files for the model designer (sometimes abbreviated "modes").
Therefore the model designer JavaScript file on GitHub (repositiory:
"https://github.com/RFS-0/ddpmfa", file path:
"ddpmfa/dpmfa/static/dpmfa/js/modes_0_1_standalone.js") is a mangled and
minified merge of the model designer source and modified model designer
dependencies.

This directory (the directory containing this README.md) contains the all the
JavaScript files useful for further development of the model designer
JavaScript:

- The unminified source code of the model designer ("src/modes.js")
- The libraries the model designer depends on:
  - The directory "lib_unmodified" contains an unmodified version of each
    library. These are the versions of the libraries as they were downloaded.
  - The directory "lib_modified" contains the libraries including the
    modifications we made to them. These are the versions of the libraries as
    they were used/included in the ddpmfa project. All modifications are marked
    by comments. Search for "RGM FORK" in a file to find the modifications.

The shell script "merge_example.sh" merges all the files in the right order. It
creates the file "build/modes_standalone.js" (which could be included into the
Django app instead of "ddpmfa/dpmfa/static/dpmfa/js/modes_0_1_standalone.js").
The following files are merged:

1. A modified version of jQuery.pan (https://github.com/mjfisheruk/jquery.pan)
   from the file "lib_modified/jquery.pan_fork.js"
2. A modified version of jQuery.panzoom
   (https://github.com/timmywil/jquery.panzoom) from the file
   "lib_modified/jquery.panzoom_fork.js"
3. A modified version of the community edition of jsPlumb
   (https://jsplumbtoolkit.com/) from the file "lib_modified/jsplumb_fork.js"
4. The source of the model designer form the file "src/modes.js"

"bootstrap.min.js", "jquery.min.js" and "tether.min.js" are not merged into the
standalone model designer js. These dependencies are not specific to the model
designer. They are included separately in the Django template.
