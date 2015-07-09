class DefaultColor:
    """
    This class should have the default colors for every segment.
    Please test every new segment with this theme first.
    """
    USERNAME_FG = 237
    USERNAME_BG = 190
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 225
    HOSTNAME_BG = 23

    INTERFACE_FG = 220
    INTERFACE_BG = 37

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 31  # blueish
    HOME_FG = 15  # white
    PATH_BG = 237
    PATH_FG = 250  # light grey
    CWD_FG = 254  # nearly-white grey
    SEPARATOR_FG = 244

    READONLY_BG = 124
    READONLY_FG = 254

    SSH_BG = 166 # medium orange
    SSH_FG = 254

    REPO_CLEAN_BG = 35  # a light green color
    REPO_CLEAN_FG = 149
    REPO_DIRTY_BG = 129
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 39
    JOBS_BG = 238

    CMD_PASSED_BG = 148
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 1
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = 148
    SVN_CHANGES_FG = 22  # dark green

    VIRTUAL_ENV_BG = 35  # a mid-tone green
    VIRTUAL_ENV_FG = 00

class Color(DefaultColor):
    """
    This subclass is required when the user chooses to use 'default' theme.
    Because the segments require a 'Color' class for every theme.
    """
    pass
