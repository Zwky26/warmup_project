# Warmup_project

## Drive in a Square
  1. High-Level Description: The Turtlebot just needs to do three possible commands: drive forward, turn, and stop. We can lump the "stop" command in with the other two. We define two methods for the node, that will run in order of: drive, turn, drive, turn, drive, turn, drive. These methods will publish to cmd_vel with corresponding vectors.
   
  2. Code Explanation: We have four functions: init, go_forward, turn, and run. Init is the same as many of our other programs. It creates a node using rospy, establishes a Publisher to cmd_vel, and sets a default speed of 0 (stopped). When the node is first created, Turtlebot should not be moving. go_forward defines a rospy rate of 2 hertz, and constantly sends a signal to move straight forward at a speed of 0.3. After 5 seconds, it publishes a twist to stop moving. turn is similar; we define a rospy rate of 2 hertz, and constantly publish a signal to rotate at a speed of pi/8. After 4 seconds, we publish a twist to stop moving. run is called when the program is rosrun'd, in which "go_forward then turn" is called 4 times. This causes Turtlebot to drive in a square.

  3. ![Drive_square_gif](https://github.com/Zwky26/warmup_project/blob/main/gifs/drive_square.gif)

## Person Follower

1. High-Level Description: The Turtlebot needs to move in response to data from the scan. We find the closest object detected by the scan, and using the angle given, determine how to turn and move forward. To do this we define two error terms, one for the absolute distance from the object and one for the trajectory/angle towards the object. 
2. Code Explanation: We execute this using two main functions: init and scan_callback. Init does what many other init functions do, defining a subscriber for the /scan topic and a publisher to the cmd_vel topic. Scan_callback is similar to the callback function used in the stop_at_wall exercise from class. We read all the data from the list "ranges", and find the minimum. If the minimum is infinity, no object is detected, so we publish an empty twist (halt any movement). If this distance is finite, the index of the minimum indicates the closest/most direct angle towards the object. We consider three cases, depending on the index. If the min is in the first or last ten indices of ranges, that indicates the object is (roughly) in front of Turtlebot, so we set angular velocity to 0. If the min is between 11 and 179, the object is on the left so we set angular veloctiy to a positive 0.3. Otherwise, the object is to Turtlebot's right, and we set angular velocity to -0.3. Using these two error terms, we can self correct the course of Turtlebot to always "home in" on the object.
3. ![Person_follow_gif](https://github.com/Zwky26/warmup_project/blob/main/gifs/person_follow.gif)

## Wall Follower

1. High-Level Description: Following a wall involves two basic conditions. We need to verify if the closest wall is in fact on our right (although it could also be left, imagine British vs American sidewalks). We also need to verify that the distance between the Turtlebot and wall is some set distance away. Once these two qualities are verified we drive forward. We can use a distance and angle error term to correct the current position of the Turtlebot to meet these conditions. 
2. Code Explanation:
3. ![Wall_follow_gif](https://github.com/Zwky26/warmup_project/blob/main/gifs/wall_follower.gif)

## Challenges

I think the biggest challenge for me was the transition to heuristic programming. I am used to deterministic results, so when my Drive_Square program kept changing results, despite minor adjustments, I felt confused. I tried debugging using rostpoic echo, and other printing statements, but soon realized they reported the same thing each time. After reading more on the Slack channel, I tried trial-and-error debugging, tweaking the velocities and time constants, which ended up being more effective. When programming the Person Follower, I found myself trying to find context/info on the packages and how 360 degree scans worked, when I realized just trying out the program itself would offer more insight to how it works. 

## Future Work

My wall follower solution has the most room for improvement. To get to the point of following the walls, it makes a large, spiral motion that is jerk-y and slow. 
