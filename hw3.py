from helper_classes import *
import matplotlib.pyplot as plt

def render_scene(camera, ambient, lights, objects, screen_size, max_depth):
    width, height = screen_size
    ratio = float(width) / height
    screen = (-1, 1 / ratio, 1, -1 / ratio)  # left, top, right, bottom

    image = np.zeros((height, width, 3))

    for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
        for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
            # screen is on origin
            pixel = np.array([x, y, 0])
            origin = camera
            direction = normalize(pixel - origin)
            ray = Ray(origin, direction)

            color = np.zeros(3)

            # This is the main loop where each pixel color is computed.
            # first, lets find the nearest intersection point and object.
            intersection = ray.nearest_intersected_object(objects)
            if intersection is not None:
                color = get_color(ray, intersection)
            
            image[i, j] = np.clip(color,0,1)
    return image

def get_color(ray, intersection):
    # the color is defined by 1. the light source, 2. the object properties, and 3. the intersection point gemotry
    intersection_point, intersection_t, min_obj = intersection
    color = min_obj.ambient
    return color

# Write your own objects and lights
# TODO
def your_own_scene():
    camera = np.array([0,0,1])
    lights = []
    objects = []
    return camera, lights, objects
