import pygame

# Initialize Pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

try:
    # Attempt to setup the joystick
    if pygame.joystick.get_count() < 1:
        print("No joystick detected!")
    else:
        joystick = pygame.joystick.Joystick(0)  # Get the first joystick
        joystick.init()

        print(f"Joystick name: {joystick.get_name()}")
        print(f"Number of axes: {joystick.get_numaxes()}")
        print(f"Number of buttons: {joystick.get_numbuttons()}")
        print(f"Number of hats: {joystick.get_numhats()}")

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    print(f"Button {event.button} pressed.")
                elif event.type == pygame.JOYBUTTONUP:
                    print(f"Button {event.button} released.")
                elif event.type == pygame.JOYAXISMOTION:
                    print(f"Axis {event.axis} value: {joystick.get_axis(event.axis):.2f}")
                elif event.type == pygame.JOYHATMOTION:
                    print(f"Hat {event.hat} value: {joystick.get_hat(event.hat)}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit Pygame
    pygame.quit()
