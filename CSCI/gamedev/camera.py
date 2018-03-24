import mathutils;
import math;
import bge;

print(dir(bge.logic.getCurrentScene().objects));


player = bge.logic.getCurrentScene().objects['Snek']; # get a reference to player object
playerRotationZ = player.localOrientation.to_euler()[2]; # get player direction as X,Y,Z (in radians not degrees)
inverseRotationZ = playerRotationZ + math.pi; # to position camera: calculate opposite direction
cameraDistance = 7.5; # camera will be 7.5 blender units on the XY plane away from player
camera = bge.logic.getCurrentController().owner; # get a reference to camera object
cameraX = player.position[0] + (math.cos(inverseRotationZ)*cameraDistance); # x position of camera
cameraY = player.position[1] + (math.sin(inverseRotationZ)*cameraDistance); # y position of camera
cameraZ = player.position[2] + 1.5; # z position of camera (1.5 units above player)
cameraRotateX = math.pi/2-math.radians(15); # tip camera to look 15 degrees downward
cameraRotateY = 0; # no sideways tilt
cameraRotateZ = playerRotationZ+(math.pi/2*(-1)); # look same way in horizontal plane as player
camera.position = (cameraX,cameraY,cameraZ); # set camera position
camera.localOrientation = (cameraRotateX,cameraRotateY,cameraRotateZ); # set camera orientation
