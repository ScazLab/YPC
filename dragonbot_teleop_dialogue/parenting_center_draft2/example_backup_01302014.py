#!/usr/bin/env python
import roslib; roslib.load_manifest('expeditions_year1')
import rospy
from dialogue_manager import *
from dragonbot_manager import DragonbotManager
from tablet_manager import TabletManager
import yaml


def main():
  dm = DragonbotManager()
  tm = TabletManager()
  with open("parenting_center_dialogue.yaml") as f:
    s = f.read()
  dialogues = yaml.load(s)
  
  dg = DialogueManager(dm, tm, "parenting_center_dialogue", dialogues["parenting_center_dialogue"])

  dm.eye_close()
  tm.change("sleep")
  while not rospy.is_shutdown() and not tm.last_press("/dragon_GUI/sleep") == 1:
    dm.say("intro-05-snore_sleep", wait = False)
    rospy.sleep(6.0)
  dm.express("wakeup")
  dm.eye_open()

  try:
    dg.play_dialogue("introduction_parenting_center")
  except PanicException:
    dm.eye_close()
    tm.change("sleep")
    return 'AHHH PANIC! SOMETHING BAD HAPPENED!'
  except NextStateException:
    return 'I want to end the dialogue, but nothing bad happened'
  except NextPhraseException:
    # Ignore this
    pass
  # When we get to the end of the dialogue, Chilly goes back to sleep
  dm.eye_close()
  tm.change("sleep")
  return "Finished dialogue successfully"

if __name__ == '__main__':
  rospy.init_node("example_dialogue")
  print main()


