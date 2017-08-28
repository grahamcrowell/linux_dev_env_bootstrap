import time
import progressbar

bar = progressbar.ProgressBar(redirect_stdout=True)
<<<<<<< Updated upstream
bar2 = progressbar.ProgressBar(redirect_stdout=True)
for i in range(100):
    bar2.update(i)
    print('Some text', i)
    time.sleep(0.1)
    # bar.update(i)
=======
for i in range(100):
    print('Some text', i)
    time.sleep(0.1)
    bar.update(i)
>>>>>>> Stashed changes
