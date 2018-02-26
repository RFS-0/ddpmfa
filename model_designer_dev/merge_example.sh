# bootstrap.min.js, jquery.min.js and tether.min.js are not merged into the
# standalone model designer js. These dependencies are not specific to the
# model designer. They are included separately in the Django template.

# 1) Create/clear output file and add a comment

echo "// This file contains the model designer js and model designer specific" > build/modes_standalone.js
echo "// dependencies. It contains the following:" >> build/modes_standalone.js
echo "// "  >> build/modes_standalone.js
echo "// 1) A modified version of jQuery.pan" >> build/modes_standalone.js
echo "//    (https://github.com/mjfisheruk/jquery.pan)" >> build/modes_standalone.js
echo "// 2)  A modified version of jQuery.panzoom" >> build/modes_standalone.js
echo "//    (https://github.com/timmywil/jquery.panzoom)" >> build/modes_standalone.js
echo "// 3)  A modified version of the community edition of jsPlumb" >> build/modes_standalone.js
echo "//    (https://jsplumbtoolkit.com/)" >> build/modes_standalone.js
echo "// 4) The model designer source"  >> build/modes_standalone.js
echo "// "  >> build/modes_standalone.js
echo "// For all modified dependencies: all modifications are marked by" >> build/modes_standalone.js
echo "// comments. Search \"RGM FORK\" to find the modifications."  >> build/modes_standalone.js
echo "// ---------------------------------------------------------------------"  >> build/modes_standalone.js
echo ""  >> build/modes_standalone.js

# 2) Add dependencies to the output file

# 2.1) Add jQuery.pan (https://github.com/mjfisheruk/jquery.pan)
cat lib_modified/jquery.pan_fork.js >> build/modes_standalone.js

# 2.2) Add jQuery.panzoom (https://github.com/timmywil/jquery.panzoom)
cat lib_modified/jquery.panzoom_fork.js >> build/modes_standalone.js

# 2.3) Add jsPlumb community edition (https://jsplumbtoolkit.com/)
cat lib_modified/jsplumb_fork.js >> build/modes_standalone.js

# 3) Add the model designer js

cat src/modes.js >> build/modes_standalone.js
