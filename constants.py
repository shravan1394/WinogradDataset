import math

# Colors for psychopy experiment
COLOR_RED = [229, 72, 35]
COLOR_GRAY = [57, 48, 42]
COLOR_WHITE = [255, 255, 255]
COLOR_BACKGROUND = [128, 128, 128]
COLOR_DISABLED = [80, 80, 80]

RATING_GREEN = [50, 255, 50]
RATING_RED = [255, 50, 50]

# code for eyelink
EYE_TRACKED = {"Right": 0,
               "Left": 1}

STARTSACC = 5
ENDSACC = 6

# for rating scale
CONFIDENCE = {8: ['HIGHEST', 'HIGH', 'MEDIUM', 'LOW', 'LOW', 'MEDIUM', 'HIGH', 'HIGHEST'],
              4: ['HIGH', 'LOW', 'LOW', 'HIGH']}

# Image props
IMG_HEIGHT = 577
IMAGE_Y_DISPLACEMENT = 100  # Psychopy coordinates
IMAGE_X_DISPLACEMENT = 0  # Psychopy coordinates
BACKGROUND_SIZE = (1024, 1280, 3)

# Cross props
CROSS_SIZE = 45  # pixels

# General
stimuli_dimensions = (
    1024, 800)  # in pixels for a single slice of the 3D volume (columns, rows) or (x,y) instead of (rows, columns)
MONITOR_RESOLUTION = (1280, 1024)
FIXATION_DURATION = 2  # in seconds
num_trials_per_condition = 100
EVENT_PROCEED_KEY = 'space'
RECALIBRATE_KEY = 'c'
GAZE_CHECK_KEY = 'g'
REMOVE_GAZE_CHECK_KEY = 'h'
STIMULI_DURATION = 2.0
QUIT_EXPERIMENT_KEY = 'escape'
OBSERVER_VIEWING_DISTANCE = 750  # in mm

# mm
PIXEL_SIZE = 0.293  # mm 0.1799
FOVEA_VISUAL_ANGLE = 2  # degrees
ATTENTION_SPOT_RADIUS = int(
    math.tan((FOVEA_VISUAL_ANGLE / 2) * math.pi / 180) * (OBSERVER_VIEWING_DISTANCE / PIXEL_SIZE))  # In pixels

# User data action

GET = "get"
UPDATE = "update"
APPEND = "append"

# OpenCV to psychopy conversion
Psych2CV = [int(MONITOR_RESOLUTION[1] / 2) - IMAGE_Y_DISPLACEMENT,
            int(MONITOR_RESOLUTION[0] / 2) + IMAGE_X_DISPLACEMENT]

# Study3 constants

LEFT = 0
RIGHT = 1

# meaning maps
FINE_PATCH_VISUAL_ANGLE = 3
COARSE_PATCH_VISUAL_ANGLE = 7
FINE_PATCH_RADIUS = int(
    math.tan((FINE_PATCH_VISUAL_ANGLE / 2) * math.pi / 180) * (OBSERVER_VIEWING_DISTANCE / PIXEL_SIZE))  # In pixels
COARSE_PATCH_RADIUS = int(
    math.tan((COARSE_PATCH_VISUAL_ANGLE / 2) * math.pi / 180) * (OBSERVER_VIEWING_DISTANCE / PIXEL_SIZE))  # In pixels

FINE_CENTRE_DISTANCE_VISUAL_ANGLE = (58 / 107) * FINE_PATCH_VISUAL_ANGLE
COARSE_CENTRE_DISTANCE_VISUAL_ANGLE = (97 / 247) * COARSE_PATCH_VISUAL_ANGLE
FINE_CENTRE_DISTANCE = int(math.tan((FINE_CENTRE_DISTANCE_VISUAL_ANGLE / 2) * math.pi / 180) * (
            OBSERVER_VIEWING_DISTANCE / PIXEL_SIZE))  # In pixels
COARSE_CENTRE_DISTANCE = int(math.tan((COARSE_CENTRE_DISTANCE_VISUAL_ANGLE / 2) * math.pi / 180) * (
            OBSERVER_VIEWING_DISTANCE / PIXEL_SIZE))  # In pixels
PATCHES_PER_IMAGE_COARSE = 108
PATCHES_PER_IMAGE_FINE = 300

# Model Params

MODEL_VIEWING_DISTANCE = (3000 * PIXEL_SIZE) / math.tan(50 * math.pi/180)   # in mm
IMG_HEIGHT_DEGREES = math.atan((577 * PIXEL_SIZE) / OBSERVER_VIEWING_DISTANCE) * (180/math.pi)
MODEL_IMG_HEIGHT = int(math.tan(IMG_HEIGHT_DEGREES * (math.pi/180)) * (MODEL_VIEWING_DISTANCE/PIXEL_SIZE)) # in pix (567 pix)