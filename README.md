**Project Title: Digit Match Game**


This OpenGL-based project showcases an interactive graphical simulation where digits (0-9) are randomly generated, one at a time. Each digit is enclosed within a circular boundary. The primary goal of this project is to display dynamic, animated digits inside a graphical circle, demonstrating digit recognition and basic shape drawing using computer graphics principles.

Features:

  Digit Rendering: Each digit (0-9) is generated with a seven-segment display style and displayed within a circle. The project uses OpenGL to render each segment and shape.

  Circular Enclosure: A circle is dynamically drawn around the digits, symbolizing an enclosure around each generated number. The circle is redrawn for each digit with slight incremental movement for animation purposes.

  Animation: The digits move vertically upwards, with smooth transitions achieved using OpenGL’s animation loop. The project supports continuous digit generation with animation frames updated every 16 milliseconds.

  User Interaction:

  1. Mouse Interaction: Clicking the left mouse button toggles the animation (play/pause). The right mouse button restarts the display.
  2. Keyboard Input: Users can press digit keys (0-9) to check if the displayed digit matches the key pressed. Correct matches increase the score and continue the animation. Wrong matches stop the animation, and a red cross is displayed.
  3. Scoring System: A scoring system tracks the user's progress. Correctly matching the digits with keyboard input increments the score.

Key OpenGL Concepts Used:

  1. Midpoint Circle Algorithm: Used to draw circles around the digits with precision and symmetry.
  2. Midpoint Line Algorithm: Utilized for rendering the seven-segment lines that form the digits.
  3. Coordinate Transformation: Functions to convert and transform coordinates between different zones, enabling efficient rendering of lines and shapes.

Potential Use Cases:

This project is ideal for understanding basic OpenGL rendering, animation principles, and user interaction in 2D graphical applications. It could serve as an educational tool for learning computer graphics algorithms such as line and circle drawing, along with simple game mechanics like score-keeping and input validation.

How to Run:

  1. Install necessary dependencies, such as OpenGL libraries (PyOpenGL for Python).
  2. Run the main script to open the window and start the animation.
  3. Use the keyboard and mouse to interact with the animation and test the digit matching feature.
![Before](https://github.com/user-attachments/assets/4aa85894-33ac-458d-ac1d-ec84d1596b29)
![After](https://github.com/user-attachments/assets/5b1ab002-fcc4-4b4d-8ee9-7a33dac9c27a)
![Random In-Game Snap](https://github.com/user-attachments/assets/ba5c37b8-c1f7-4781-8c8b-4f46a9480103)
![Wrong](https://github.com/user-attachments/assets/f243d665-2789-4da7-9667-0998961d2e87)
