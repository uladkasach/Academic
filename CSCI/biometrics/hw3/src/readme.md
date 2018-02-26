Biometrics Homework 3 Report
Uladzimir Kasacheuski
2/16/18

My code and source images are attached as a zip file.

The code can be run by running `python hand_vectors.py <image_choice>` where image choice is from `hand1.jpg` to `hand5.jpg`.

I have written the code to select points from an image with python (using the matplotlib library and the PIL library).
The code successfuly extracts pairs of points (it assumes every two consecutive points are associated), calculates the euclidean distance between the two points, and plots the path between the points on the image. It then generates a vector based on the euclidean distances for every two points that it measures.

However, I have come across a bug that does not enable me to accurately select the points on the image due to my computer.

Though I do not have a computer with which I can complete the image labeling and report the vectors; my code does work as you will be able to verify.


Bug:
My machine is affected by this bug: https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1720219
This bug continuously submits virtual keyboard presses.

This has made it so that i am unable to complete this assignment using the ginput functionality provided by python as it assumes any keyboard press is a request from the user to place a point. (I have attached my best attempt at selecting the points on image one in the report.)

I have not been able to resolve that bug and I have had an error when attempting to install matlab on my machine so I was not able to complete this assignment in that format either.

I have attempted disabling my keyboard and found that it is a virtual problem, as the bug report above documents. I have also searched for an answer as to how I can disable ginput from utilizing keyboard inputs with no avail : https://stackoverflow.com/questions/48837731/disable-key-input-for-ginput-from-matplotlib


Please let me know if I can submit this assignment late after testing on a machine I can aquire tomorrow.


UPDATE 2/21/17:
I have completed this assignemnt on a different machine that was not affected by this bug, as Dr. Tsechpenakis stated he understood the situation and I could submit it late.