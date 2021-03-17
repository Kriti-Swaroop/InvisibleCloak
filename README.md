# InvisibleCloak
Invisible Cloak is made using OpenCV in Python. Here I have used a red coloured cloth as the cloak. Any other coloured cloth can be used, only the HSV values have to be changed accordingly(line 16, 17, 19 and 20). These values will also differ by the illumination of the video and the shade of the cloth(there are different shades of red).

It is made by 4 steps:
  1) Storing the background image
  2) Identifying the red coloured cloth
  3) Segmenting out the red cloth by generating a mask
  4) Displaying the final image

In simple words, we will store the background image, find the red coloured cloth in the video, replace that part with the background image and finallu display the video with replaced part of red cloth.
