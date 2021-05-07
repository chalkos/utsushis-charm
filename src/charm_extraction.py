# 547,26 - 628,51
# 27*26

# Skill name size 216*21 # it appears those dimensions cause some slight shifting
# Skill 1: 413, 94
# Skill 2: 413, 144
# Skill 3: 413, 194 -> Jewels were not removed

# Level Size: 12 * 21
# Level 1: 618, 117
# Level 2: 618, 167
# Level 3: 618, 217 -> Jewels were not removed

from .Charm import Charm
from .utils import *
from tqdm import tqdm
from symspellpy.symspellpy import SymSpell
import numpy as np
import logging
import json
import cv2
import os
DEBUG = False


logger = logging.getLogger(__name__)
if DEBUG:
    logger.setLevel(logging.DEBUG)

known_skills = {}

spell = SymSpell(max_dictionary_edit_distance=4)
spell.load_dictionary(get_resource_path("skill_dict"), 0, 1)


known_corrections = {}
with open(get_resource_path('skill_corrections'), encoding='utf-8') as scf:
    for line in scf.readlines():
        line = line.strip()
        w, r = line.split(',')
        known_corrections[w] = r


all_skills = {}
with open(get_resource_path('skill_list')) as slf:
    for line in slf.readlines():
        skill_name = line.strip()
        all_skills[skill_name.lower()] = skill_name


def is_skill(skill_dict, skill_name):
    return skill_name.lower().strip() in skill_dict


def fix_skill_name(skill_dict, skill_name):
    return skill_dict[skill_name.lower()]


def extract_charm(frame_loc, slots, skills):
    logger.debug(f"Starting charm for {frame_loc}")
    has_errored = False
    charm = Charm(slots)
    skill_number = 0
    for skill, level in skills:
        skill_number += 1

        # lwr = skill.lower()
        # if lwr not in known_skills:
        #     known_skills[lwr] = 1
        #     s_f = all_skills[lwr]+f".png"
        #     sp = os.path.join("images", "skills",s_f)
        #     known_skills[lwr] +=1
        #     cv2.imwrite(sp, skill_img)
        #     if len(known_skills) == len(all_skills):
        #         print("=======All skills found========")

        charm.add_skill(fix_skill_name(all_skills, skill), level)

    logger.debug(f"Finished charm for {frame_loc}")
    logger.debug(f"{frame_loc}: {charm.to_dict()}")

    return charm


def extract_charms(frame_dir):
    charms = []
    try:
        with tqdm(list(os.scandir(frame_dir)), desc="Parsing skills")as tqdm_iter:
            for frame_loc in tqdm_iter:
                frame_loc = frame_loc.path
                try:
                    tqdm_iter.set_description(f"Parsing {frame_loc}")
                    frame = cv2.imread(frame_loc)

                    skill_only_im = remove_non_skill_info(frame)
                    slots = get_slots(skill_only_im)

                    inverted = cv2.bitwise_not(skill_only_im)

                    trunc_tr = apply_trunc_threshold(
                        inverted)  # appears to work best

                    skills = get_skills(trunc_tr, True)

                    skill_text = read_text_from_skill_tuple(skills)

                except Exception as e:
                    logger.error(
                        f"An error occured when analysing frame {frame_loc}. Error: {e}")

                try:
                    if any(map(lambda x: x[0] == "Unknown", skills)):
                        logger.warn(
                            f"Unknown skill found on {frame_loc}. Consider creating a Github issue here: https://github.com/chpoit/utsushis-charm/issues/new and upload the frame that causes errors")
                    charm = extract_charm(frame_loc, slots, skills, skill_text)
                    charms.append(charm)
                except Exception as e:
                    logger.error(
                        f"An error occured when extracting charm on {frame_loc}. Error: {e}")

    except Exception as e:
        logger.error(f"Crashed with {e}")

    return set(charms)


def save_charms(charms, charm_json):
    with open(charm_json, "w") as charm_file:
        charms = list(map(lambda x: x.to_dict(), charms))
        json.dump(charms, charm_file)


if __name__ == "__main__":
    frame_dir = "frames"
    charm_json = "charms.json"

    charms = extract_charms(frame_dir)

    save_charms(charms, charm_json)
