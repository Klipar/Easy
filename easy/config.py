from easy.message import *
from easy.logger import Logger
from typing import Union, Dict, Any, Callable
import json
import os

class Config:
    """
    A class to manage configuration loading and validation.

    Attributes:
        logger (Logger): Logger instance for logging messages.
        configPath (str): Path to the configuration file.
        configVersion (str): Expected version of the configuration.
        configVersionParameterName (str): Parameter name for the configuration version.
        configTemplate (Dict): Template for the configuration.
        configTemplatePath (str): Path to the configuration template file.
        config (Dict): Loaded configuration data.
    """

    def __init__(self, configPath: str,
                 logger: Logger = None,
                 configVersion: str = None,
                 configVersionParameterName: str = "configVersion",
                 onFailedToLoadConfig: Callable = None,
                 configTemplate: Dict = None,
                 configTemplatePath: str = None):
        """
        Initializes the Config instance.

        Args:
            configPath (str): Path to the configuration file.
            logger (Logger, optional): Logger instance. Defaults to a new Logger instance.
            configVersion (str, optional): Expected version of the configuration. Defaults to None.
            configVersionParameterName (str, optional): Parameter name for the configuration version. Defaults to "configVersion".
            onFailedToLoadConfig (Callable, optional): Callback function to call on failed config load. Defaults to None.
            configTemplate (Dict, optional): Template for the configuration. Defaults to None.
            configTemplatePath (str, optional): Path to the configuration template file. Defaults to "templateConfig.json".
        """
        self.logger: Logger = logger if logger else Logger()
        self.configPath: str = configPath
        self.configVersion: str = configVersion
        self.configVersionParameterName = configVersionParameterName

        self.configTemplate = configTemplate
        self.configTemplatePath = configTemplatePath if configTemplatePath else "templateConfig.json"

        self.logger.inform("Loading config...")

        self.config = self.readConfig(self.configPath)

        if (self.config and self.checkConfigVersion()):
            self.logger.success("Config loaded successfully!")
        else:
            self.config = None
            self.logger.failed("Config loaded unsuccessfully!")

            if (self.configTemplate):
                self.createConfigTemplate()

            if (onFailedToLoadConfig): onFailedToLoadConfig()

    def checkConfigVersion(self, config: Union[Dict[str, Any], None] = None, expectedConfigVersion: str = None) -> bool:
        """
        Checks if the loaded configuration version matches the expected version.

        Args:
            config (Union[Dict[str, Any], None], optional): Configuration to check. Defaults to None.
            expectedConfigVersion (str, optional): Expected configuration version. Defaults to None.

        Returns:
            bool: True if the versions match, False otherwise.
        """
        config = config if config else self.config
        expectedConfigVersion: str = expectedConfigVersion if expectedConfigVersion else self.configVersion

        if (expectedConfigVersion is None):
            return True

        realConfigVersion: str = self.getValue(self.configVersionParameterName)

        if (expectedConfigVersion != realConfigVersion):
            self.logger.failed(f"Version IS INCORRECT. Expected: {expectedConfigVersion}, but got: {realConfigVersion}")
            return False
        else:
            self.logger.success(f"The config version matches.")
            return True

    def refreshConfig(self, configPath: str = None) -> None:
        """
        Refreshes the configuration from the specified path.

        Args:
            configPath (str, optional): Path to the new configuration file. Defaults to the current configPath.
        """
        configPath = configPath if configPath else self.configPath

        tmpConfig = self.readConfig(configPath)

        if (tmpConfig is None):
            self.logger.failed("Failed to refresh config.")
            return

        if (tmpConfig != self.config):
            self.logger.inform("New configuration file found.")
            if (self.checkConfigVersion(config=tmpConfig)):
                self.configPath = configPath
                self.config = tmpConfig

                self.logger.warn("Config was changed!")
        else:
            self.logger.inform("Config wasn't changed, versions not matched.")

    def createConfigTemplate(self):
        """
        Creates a configuration template file based on the provided configTemplate.
        """
        if input("Create a config template? (Yes/No): ").strip().lower() in ('yes', 'y'):
            try:
                self.__checkAndCreateDir(os.path.dirname(self.configTemplatePath))
                with open(self.configTemplatePath, 'w') as f:
                    json.dump(self.configTemplate, f, indent=4)
                success(f"File '{self.configTemplatePath}' created successfully!")

            except Exception as err:
                failed(f"Cant create config file: {err}")

        else:
            inform("The creation of the configuration file has been canceled.")

    def __checkAndCreateDir(self, dir):
        """
        Checks if the specified directory exists and creates it if it does not.

        Args:
            dir (str): The path of the directory to check and create.
        """
        if not os.path.exists(dir):
            try:
                os.makedirs(dir)
            except Exception as err:
                failed(f"Cant create {dir} directory: {err}")
            inform(f"Directory '{dir}' created successfully.")

    def readConfig(self, configPath: str) -> Union[Dict[str, Any], None]:
        """
        Reads the configuration from the specified file path.

        Args:
            configPath (str): The path to the configuration file.

        Returns:
            Union[Dict[str, Any], None]: The loaded configuration as a dictionary, or None if loading failed.
        """
        try:
            with open(configPath, 'r') as file:
                return json.load(file)
        except Exception as e:
            self.logger.failed(f"Can't open config file: {e}")

    def getValue(self, *args: str, config: Union[Dict[str, Any], None] = None) -> Any:
        """
        Retrieves a value from the configuration based on the provided keys.

        Args:
            *args (str): Keys to access the nested value in the configuration.
            config (Union[Dict[str, Any], None], optional): The configuration dictionary to search. Defaults to None.

        Returns:
            Any: The value associated with the provided keys, or None if the value could not be retrieved.
        """
        value = config if config else self.config

        if (value is None):
            self.logger.failed("Failed to get value, config is \"None\"")
            return None

        try:
            for arg in args:
                value = value[arg]
        except Exception as e:
            failed(f"ERROR while reading config: {e}")
            return None

        return value
