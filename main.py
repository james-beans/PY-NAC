import pygame
from OpenGL.GL import *
import imgui
from imgui.integrations.pygame import PygameRenderer

# Initialize pygame with an OpenGL context
pygame.init()
window_size = (800, 600)
pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Hello, World Window")

# Initialize imgui and the PygameRenderer
imgui.create_context()
imgui_renderer = PygameRenderer()

# Main loop
running = True
while running:
    # Handle pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        imgui_renderer.process_event(event)

    # Set DisplaySize to the window size before starting a new frame
    imgui.get_io().display_size = window_size

    # Start a new ImGui frame
    imgui.new_frame()

    # Create an ImGui window with "Hello, World" text
    imgui.begin("Hello Window")
    imgui.text("Hello, World")
    imgui.end()

    # Render ImGui content
    glClearColor(0.1, 0.1, 0.1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    imgui.render()
    imgui_renderer.render(imgui.get_draw_data())
    
    # Swap the buffers
    pygame.display.flip()

# Clean up on exit
imgui_renderer.shutdown()
pygame.quit()

