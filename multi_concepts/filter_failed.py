import os
from glob import glob
import numpy as np
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-tag', '--tag', type=str, default="lora", help='tag name'
    )
    args = parser.parse_args()

    subjects = np.loadtxt("./clusters/subjects_test.txt", dtype=str, delimiter=" ")[:, 0]
    subjects = [f"./results/{args.tag}/{outfit}/" for outfit in subjects]

    failed_sd = []
    failed_sds = []

    def lst_to_file (lst, filename):
        
        with open(filename, "w") as f:
            for item in lst:
                item = item.replace(f"./results/{args.tag}/","")
                subject, outfit = item.split('/')[-3:-1]
                f.write(f"{item[:-1]} {subject} {outfit}\n")

    for subject in subjects:
                
        # if not os.path.exists(os.path.join(subject, "unet/adapter_config.json")):
        #     failed_sd.append(subject)
        # else: 
        #     if not os.path.exists(os.path.join(subject, "texture/visualize/texture_ep0100_rgb.mp4")):
        #         failed_sds.append(subject)
                
        if not os.path.exists(os.path.join(subject, "img_logs/05000_step_raw_attn.jpg")):
            failed_sd.append(subject)
        else: 
            if not os.path.exists(os.path.join(subject, "texture/visualize/texture_ep0100_rgb.mp4")):
                failed_sds.append(subject)

    print("Failed SD: ", len(failed_sd))
    print("Failed SDS: ", len(failed_sds))


    lst_to_file(failed_sd, f"./clusters/failed_sd_{args.tag}.txt")
    lst_to_file(failed_sds, f"./clusters/failed_sds_{args.tag}.txt")
            

