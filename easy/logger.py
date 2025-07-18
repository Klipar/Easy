from massage import *

# Default log levels for various logging functions.
# The keys represent the logging functions,
# and the values represent the minimum log level required
# for messages to be logged by those functions.
DefaultFunctionsLogLevels = {
            failed: 1,
            success: 3,
            inform: 4,
            warn: 2,
            pr: 5,
            test: 5
        }

class Logger:
    """
    A Logger class that dynamically sets logging functions based on specified log levels.

    Attributes:
        logLevel (int): The current logging level for the logger.
        functionsLogLevels (dict): A dictionary mapping function to their respective log levels.

    Parameters:
        logLevel (int): The maximum log level for messages to be logged.
        **kwargs: Additional log levels for specific functions, which will override the default levels.

    Example:
        logger = Logger(logLevel=3, warn=4)
        logger.success("This is a success message.")   # Will log
        logger.warn("This is a warning message.")      # Will not log, as logLevel < funcLogLevel
    """
    def __init__(self, logLevel: int, **kwargs):
        """
        Initializes the Logger with a specified log level and optional custom log levels.

        Args:
            logLevel (int): The minimum log level for logging messages.
            **kwargs: Custom log levels for specific logging functions.
        """
        self.logLevel: int = logLevel
        self.functionsLogLevels = DefaultFunctionsLogLevels

        self.functionsLogLevels.update(kwargs)

        for func, funcLogLevel in self.functionsLogLevels.items():
            setattr(self, func.__name__, self.__SetLogFunctions(func, funcLogLevel))

    def __SetLogFunctions(self, func, funcLogLevel: int):
        def logFunction(self, *args, **kwargs):
            if(self.logLevel >= funcLogLevel):
                return(func(*args, **kwargs))
            return None

        return logFunction.__get__(self)
