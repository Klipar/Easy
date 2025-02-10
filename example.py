# easy already installed
from  easy import *
from time import sleep
inform ("Launch the system")
sleep(1)
warn ("Uninstalled modules found, start downloading...")
sleep(1)
bar = LineProgresBar(MaxLength = 50,            # bar line length
                         text = "Loading ",     # text before the bar
                         maxWalue = 200,        # number of iterations up to 100%
                         isShowPersent = True,  # show percentages
                         isShowWalue = True)    # show values 
for i in range (200):
    bar.ShoveAndUpdate(dif_in_walue = 1)        # dif_in_walue - means the step size, standard = 1
    sleep (0.01)
success("All modules are downloaded successfully!")
inform ("check the installed modules...")

bar = LineProgresBar(MaxLength = 50,                # bar line length
                         text = "Check the hash ",  # text before the bar
                         maxWalue = 100,            # number of iterations up to 100%
                         isShowPersent = True,      # show percentages
                         isShowWalue = False)        # show values 
for i in range (100):
    bar.ShoveAndUpdate(dif_in_walue = 1)        # dif_in_walue - means the step size, standard = 1
    sleep (0.05)
    if i == 75:
        failed("The hashes do not match!", st = "\n")
        sleep(0.1)
        inform("Reinstalling the module...")
        sim = SimpleAnimation()
        for j in range (10):
            inform(str = f"Progress: [ {sim.step()} ]\r", en = "")
            sleep(0.2)
        success("The damaged module has been successfully reinstalled!", st = "\n")

success("All necessary modules are installed and tested!")
sleep (0.5)
warn ("Start the main program cycle.")
sim = SimpleAnimation()
for i in range (30):
    inform(str = f"Progress: [ {sim.step()} ]\r", en = "")
    sleep (0.3)
success("the program was completed successfully!", st="\n")
