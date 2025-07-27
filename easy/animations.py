from typing import Tuple

class SimpleAnimation:
    """
    A class to create a simple animation using a set of characters.

    Attributes:
        animationSet (Tuple[str, ...]): A tuple containing the characters used for the animation.
        animationIndex (int): The current index in the animation set.
    """

    def __init__(self, startChar: str = '|',
                 animationSet: Tuple[str, ...] = ('|', '/', '-', '\\')):
        """
        Initializes the SimpleAnimation instance.

        Args:
            startChar (str, optional): The character to start the animation with. Defaults to '|'.
            animationSet (Tuple[str, ...], optional): A tuple of characters to use in the animation.
                Defaults to ('|', '/', '-', '\\').
        """
        self.animationSet = animationSet
        self.animationIndex = animationSet.index(startChar)

    def step(self) -> str:
        """
        Advances the animation to the next character in the animation set.

        Returns:
            str: The next character in the animation sequence.
        """
        self.animationIndex += 1
        if (self.animationIndex >= len(self.animationSet)):
            self.animationIndex = 0

        return self.show()

    def show(self) -> str:
        """
        Displays the current character in the animation sequence.

        Returns:
            str: The current character being displayed in the animation.
        """
        return self.animationSet[self.animationIndex]


class LineProgressBar:
    """
    A class to create a line progress bar for visualizing progress in a console application.

    Attributes:
        MaxLength (int): The maximum length of the progress bar.
        currentValue (int): The current value of the progress.
        maxValue (int): The maximum value that the progress can reach.
        text (str): The text to display alongside the progress bar.
        isShowPercent (bool): Flag indicating whether to show the percentage of completion.
        isShowValue (bool): Flag indicating whether to show the current value and maximum value.
    """

    def __init__(self, MaxLength: int, text: str, isShowPercent: bool = False, maxValue: int = 0, isShowValue: bool = False):
        """
        Initializes the LineProgressBar instance.

        Args:
            MaxLength (int): The maximum length of the progress bar.
            text (str): The text to display alongside the progress bar.
            isShowPercent (bool, optional): Flag to indicate if the percentage should be shown. Defaults to False.
            maxValue (int, optional): The maximum value for the progress. Defaults to 0.
            isShowValue (bool, optional): Flag to indicate if the current and maximum values should be shown. Defaults to False.
        """
        self.MaxLength = MaxLength
        self.currentValue = 0
        self.maxValue = maxValue

        self.text = text

        self.isShowPercent = isShowPercent
        self.isShowValue = isShowValue

    def shoveAndUpdate(self, difInValue: int = 1):
        """
        Updates the current value of the progress bar and displays the updated progress.

        Args:
            difInValue (int, optional): The difference to add to the current value. Defaults to 1.
        """
        self.currentValue += difInValue
        x = int(((self.currentValue * self.MaxLength) / self.maxValue))

        print(self.text, "[", end="")

        for i in range(x):
            print("=", end="")
        if (x < self.MaxLength):
            print(">", end="")
            for i in range(self.MaxLength - x):
                print("-", end="")
        print("]", end="")
        if (self.isShowValue):
            print(f"  [{self.currentValue}/{self.maxValue}]", end="")
        if (self.isShowPercent):
            print(f"  [{round((self.currentValue / self.maxValue * 100), 1)}%]", end="")
        print("\r", end="")
        if (self.currentValue == self.maxValue):
            print()
