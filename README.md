# Warmup_project

## Drive in a Square
  1. High-level Description: The Turtlebot just needs to do three possible commands: drive forward, turn, and stop. We can lump the "stop" command in with the other two. We define two methods for the node, that will run in order of: drive, turn, drive, turn, drive, turn, drive. These methods will publish to cmd_vel with corresponding vectors.
   
  2. Code Explanation: We have four functions: init, go_forward, turn, and run. Init is the same as many of our other programs. It creates a node using rospy, establishes a Publisher to cmd_vel, and sets a default speed of 0 (stopped). When the node is first created, Turtlebot should not be moving. go_forward defines a rospy rate of 2 hertz, and constantly sends a signal to move straight forward at a speed of 0.3. After 5 seconds, it publishes a twist to stop moving. turn is similar; we define a rospy rate of 2 hertz, and constantly publish a signal to rotate at a speed of pi/8. After 4 seconds, we publish a twist to stop moving. run is called when the program is rosrun'd, in which "go_forward then turn" is called 4 times. This causes Turtlebot to drive in a square.

  3. ![Drive_square_gif](https://github.com/Zwky26/warmup_project/blob/main/gifs/drive_square.gif)

## Challenges

I think the biggest challenge for me was the transition to heuristic programming. I am used to deterministic results, so when my Drive_Square program kept changing results, despite minor adjustments, I felt confused. I tried debugging using rostpoic echo, and other printing statements, but soon realized they reported the same thing each time. After reading more on the Slack channel, I tried trial-and-error debugging, tweaking the velocities and time constants, which ended up being more effective. When programming the Person Follower, I found myself trying to find context/info on the packages and how 360 degree scans worked, when I realized just trying out the program itself would offer more insight to how it works. 
