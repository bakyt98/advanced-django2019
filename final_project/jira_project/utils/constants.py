LOW = "LOW"
MEDIUM = "MEDIUM"
HIGH = "HIGH"

PRIORITY =(
    (LOW, "LOW"),
    (MEDIUM, "MEDIUM"),
    (HIGH, "HIGH")
)

MAX_FILE_SIZE = 2 * 1024 * 1024

SOFTWARE = "SOFTWARE"
WEB = "WEB"
APP = "APP"

PROJECT_TYPES = (
    (SOFTWARE, SOFTWARE),
    (WEB, WEB),
    (APP, APP)
)

TODO = 1
INPROGRESS = 2
DONE = 3
NEW = 99

BLOCK_TYPES = (
    (TODO, "TO DO"),
    (INPROGRESS, "In progress"),
    (DONE, "Done"),
    (NEW, "New")
)
