
import subprocess

import subprocess

process1 = subprocess.Popen(["python", "twittertrends.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["python", "youtubetrends.py"])
process3 = subprocess.Popen(["python", "cryptotrends.py"])
process4=subprocess.Popen(["python", "merger\merge.py"])
process5=subprocess.Popen(["python", "merger\merge2.py"])
process6=subprocess.Popen(["python", "merger\merge3.py"])
process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()
process3.wait()
process4.wait()
process5.wait()
process6.wait()

