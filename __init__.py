import pyautogui, time
import os.path

currentScreenImage = 'images/Screenie.png'
nextButtonImage = 'images/NextButton.png'
greyCircleImage = 'images/GreyCircle.png'
startImage = 'images/Start.png'
homeScreenImage = 'images/HomeScreen.png'
homeScreenStartImage = 'images/HomeScreenStart.png'

screenSize = pyautogui.size()
pyautogui.PAUSE = 1.5

# Finds a image on screen and clicks it
# @Image image to find on the screen
# @Return returns none if image is not found on screen
def LocateAndClick(image):
    locatedImage = pyautogui.locateCenterOnScreen(image)
    if locatedImage is not None:
        pyautogui.leftClick(locatedImage[0], locatedImage[1], duration=3, tween=pyautogui.easeInElastic)
    return locatedImage

while True:
    if not os.path.isfile(currentScreenImage):
        pyautogui.screenshot(region=(0, 0, 0, 0))

    currentScreenShot = pyautogui.locateOnScreen(currentScreenImage)
    pyautogui.screenshot(currentScreenImage)

    if currentScreenShot is not None:
        pyautogui.alert('Video Stopped Playing', 'Alert')

    LocateAndClick(nextButtonImage)

    # Determine if in course section screen then click next course
    if pyautogui.locateOnScreen(greyCircleImage, confidence=0.9) is not None:
        if LocateAndClick(startImage) is None:
            pyautogui.scroll(-750, screenSize[0] / 2, screenSize[1] / 2)
            # TODO: Fix bug with start image returning none after locating startImage
            if LocateAndClick(startImage) is None:
                LocateAndClick(homeScreenImage)
                pyautogui.scroll(-750, screenSize[0] / 2, screenSize[1] / 2)
                LocateAndClick(homeScreenStartImage)

    time.sleep(15)
